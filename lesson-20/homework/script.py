import pandas as pd 
import sqlite3 as sq

#Find the total amount spent by each customer on purchases:

with sq.connect('chinook.db') as conn:
    invoices_table=pd.read_sql_query("Select * from invoices", conn)

with sq.connect('chinook.db') as conn:
    invoices_table_2=pd.read_sql_query("Select * from invoice_items", conn)  

with sq.connect('chinook.db') as conn:
    customers=pd.read_sql_query("Select * from customers", conn) 

merged_table = invoices_table.merge(invoices_table_2, how='inner', on='InvoiceId' )

total_spent_by_each_customer=merged_table.pivot_table(values='Total', index='CustomerId', aggfunc='sum')
total_spent_by_each_customer

# Identify the top 5 customers with the highest total purchase amounts.
top_5 =total_spent_by_each_customer.sort_values('Total', ascending=False).head(5).reset_index()
top_5



# Display the customer ID, name, and the total amount spent for the top 5 customers.
selected = top_5.merge(customers, how='inner',on='CustomerId')
selected = selected[['CustomerId', 'FirstName','LastName','Total']]
selected



import sqlite3
import pandas as pd

def analyze_purchase_preferences(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Create a temporary view for customers who bought complete albums
    conn.execute("""
    CREATE TEMPORARY VIEW album_buyers AS
    SELECT 
        i.CustomerId,
        a.AlbumId,
        COUNT(DISTINCT t.TrackId) AS tracks_purchased
    FROM Invoice i
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
    JOIN Album a ON t.AlbumId = a.AlbumId
    GROUP BY i.CustomerId, a.AlbumId
    HAVING tracks_purchased = (
        SELECT COUNT(*) 
        FROM Track 
        WHERE AlbumId = a.AlbumId
    )
    """)
    
    # Create a temporary view for customers who bought partial albums
    conn.execute("""
    CREATE TEMPORARY VIEW track_buyers AS
    SELECT DISTINCT i.CustomerId
    FROM Invoice i
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
    WHERE NOT EXISTS (
        SELECT 1
        FROM Track t2
        WHERE t2.AlbumId = t.AlbumId
        AND t2.TrackId NOT IN (
            SELECT il2.TrackId 
            FROM InvoiceLine il2 
            JOIN Invoice i2 ON il2.InvoiceId = i2.InvoiceId
            WHERE i2.CustomerId = i.CustomerId
        )
    )
    EXCEPT
    SELECT CustomerId FROM album_buyers
    """)
    
    # Get total number of customers
    total_customers = conn.execute("SELECT COUNT(DISTINCT CustomerId) FROM Invoice").fetchone()[0]
    
    # Get album buyers count
    album_buyers_count = conn.execute("SELECT COUNT(DISTINCT CustomerId) FROM album_buyers").fetchone()[0]
    
    # Get track buyers count
    track_buyers_count = conn.execute("SELECT COUNT(DISTINCT CustomerId) FROM track_buyers").fetchone()[0]
    
    # Calculate percentages
    album_percentage = (album_buyers_count / total_customers) * 100
    track_percentage = (track_buyers_count / total_customers) * 100
    
    # Create a summary DataFrame
    summary = pd.DataFrame({
        'Preference': ['Full Albums', 'Individual Tracks', 'Mixed/Other'],
        'Customer Count': [album_buyers_count, track_buyers_count, total_customers - album_buyers_count - track_buyers_count],
        'Percentage': [album_percentage, track_percentage, 100 - album_percentage - track_percentage]
    })
    
    # Clean up
    conn.execute("DROP VIEW IF EXISTS album_buyers")
    conn.execute("DROP VIEW IF EXISTS track_buyers")
    conn.close()
    
    return summary

# Usage example
if __name__ == "__main__":
    db_path = "Chinook.db"  # Replace with your database path
    results = analyze_purchase_preferences(db_path)
    print("\nCustomer Purchase Preferences:")
    print(results.to_string(index=False))

# HOMEWORK 1 :

import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')

# Find all questions that were created before 2014

date_filter = df["creationdate"] < "2014-01-01"

print(df[date_filter])

# Find all questions with a score more than 50

score_filter = df["score"] > 50

print(df[score_filter])

# Find all questions with a score between 50 and 100

score_filter_bet = df['score'].between(50,100)

print(df[score_filter_bet])

# Find all questions answered by Scott Boston

scott_boston_filter = df['ans_name'] == 'Scott Boston'

print(df[scott_boston_filter])

# Find all questions answered by the following 5 users

target_users = ['Scott Boston', 'doug', 'Mike Pennington', 'Demitri', 'Avaris']
name_filter = df['ans_name'].isin(target_users)
print(df[name_filter])

# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

date_filter = df["creationdate"].between("2014-03-01","2014-10-31")
name_filter = df['ans_name'] == 'Unutbu'
score_filter = df["score"] < 5

print(df[date_filter & name_filter & score_filter])

# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')

score_filter = df["score"].between(5,10)
view_cnt_filter = df["viewcount"] > 10000

print(df[score_filter | view_cnt_filter])

# Find all questions that are not answered by Scott Boston
 
import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')
 
not_scott = df['ans_name'] != 'Scott Boston'

print(df[not_scott])


# HOMEWORK 2 :

import pandas as pd

df = pd.read_csv('titanic.csv')

# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
extracted_data_f = pd.read_csv("titanic.csv", usecols=['Sex','Pclass','Age'])
gender_filter = extracted_data_f['Sex'] == 'female'
class_filter = extracted_data_f['Pclass'].fillna(0) == 1
age_filter = extracted_data_f['Age'].fillna(0).between(20,30)

print(extracted_data_f[gender_filter & class_filter & age_filter])


#Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

df = pd.read_csv('titanic.csv')

paid_over_100 = df['Fare'] > 100

newdataf = df[paid_over_100]

print(newdataf)

# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

survived = df['Survived'] == 1
sibsp = df['SibSp']  == 0
parch = df['Parch'] == 0

print(df[survived & sibsp & parch])

# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

emb_c = df['Embarked'] == 'C'
paid_over_50 = df['Fare'] > 50

new_dataframe = df[emb_c & paid_over_50]

print(new_dataframe)


# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

has_sibs = df['SibSp']  >= 1
has_parch = df['Parch'] >= 1

print(df[has_sibs & has_parch])


# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

age_filter = df['Age'] <=15
not_survided = df['Survived'] == 0
 
new_df = df[age_filter & not_survided]

print(new_df)

# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

cabins = df['Cabin'].fillna('Unknown') != 'Unknown'
paid_over_200 = df['Fare'] > 200

print(df[cabins & paid_over_200])


# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

odd = df['PassengerId'] % 2 != 0
odd_id_passengers = df[odd]

print(odd_id_passengers)

# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.



dub = df['Ticket'].duplicated(keep=False)

print(df[~(dub)])


#Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

import pandas as pd

df = pd.read_csv('titanic.csv')
miss = df['Name'].str.contains(r'Miss')

miss_df = df[miss]

print(miss_df)

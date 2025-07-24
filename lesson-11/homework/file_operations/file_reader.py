# file_reader.py

def read_file(path: str):
    with open( path, "r") as f :
        
        content = f.read()
        return content
    

print(read_file("text.txt"))

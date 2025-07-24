# file_writer.py

def write_file(path: str, content: str):
    with open( path, "w") as f :
        
        content = f.write(content)
        print("Written successfully !")
    

write_file("text.txt","uzgartirildi ukam! manimcha bo'ldi")

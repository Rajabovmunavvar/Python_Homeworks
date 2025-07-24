# string_utils.py

def  reverse_string(st: str):
    try:
        st = ''.join(reversed(st))
        return st
    except TypeError:
        print(f"Parameter must be string,  not {type(st)}")

def  count_vowels(st: str):
    try:
        
        vowels = "aeiou"
        count = 0
        for char in st.lower():
            if char in vowels:
                count += 1
        return count

    except TypeError:
        print(f"Parameter must be string,  not {type(st)}")
    except AttributeError:
        print(f"Parameter must be string,  not {type(st)}")

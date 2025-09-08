def preLetterCase(name, key):
    
    key_upper = key.upper()
    
    
    result = ""
    
   
    for char in name:
        if char == key:
            result += key_upper
        else:
            result += char
            
    return result
print(preLetterCase("koushik","k"))
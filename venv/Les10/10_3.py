def code(invoerstring):
    output = ''
    for i in invoerstring:
        temp = ord(i)
        temp += 3
        output += chr(temp)
    return(output)

print(code("RutteAlkmaarDen Helder")) 



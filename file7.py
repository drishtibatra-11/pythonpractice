with open('example.txt', 'w') as f:
    f.write('hello,python!\nthis is a file handling example.\n')
with open('example.txt', 'r') as f:
    content = f.read() #to read the content of the file
    print(content)
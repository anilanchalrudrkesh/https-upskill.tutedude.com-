a='output.txt'
b=str(input('Enter text to write to the file :'))
try:
    file= open(f"d:\{a}",'w')
    write_data=file.write(b)
    print(f'Data succesfully writen to {a}')
    file.close()
except FileNotFoundError:
    print(f"Errer: The File {a} was not Found")

c=str(input('Enter Additional text to Append :'))
try:
    file1= open(f"d:\{a}",'a')
    write_data = file1.write("\n")
    write_data=file1.write(c)
    file1.close()
    print(f'data successfully append')
except FileNotFoundError:
    print(f"Errer: The File {a} was not Found")

filer= open(f"d:\{a}",'r')
reading=filer.read()
print(reading)
file.close()

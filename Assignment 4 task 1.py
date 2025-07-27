a='sample.txt'

def create_file():
    content='''This is sample file.
It contane multiple file. \n'''
    with open (f'd:\{a}','w') as file:
        file.write(content)

#create_file()

try:
    file1= open(f"d:\{a}",'r')
    read_file=file1.read()
    print(read_file)
    file1.close
except FileNotFoundError:
    print(f"Errer: The File {a} was not Found")

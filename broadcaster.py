import os
import subprocess
msg = input("hi, welcome to Pootato's AHS message broadcaster\nplease enter your message below:\n")
f = open("728975489072389734289758978782905783745.txt", "x")
f = open("728975489072389734289758978782905783745.txt", "a")
f.write("msg * "+msg)
f.close()
my_file = '728975489072389734289758978782905783745.txt'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.bat')
subprocess.call([r'728975489072389734289758978782905783745.bat'])

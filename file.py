# file=open('sample.txt','r')
# content=file.readline()
# print(content)
# file.close()
# file=open('sample1.txt','w')
# content=file.write("Hello ,this is harshini")

# file.close()
# file=open('sample1.txt','a')
# content=file.write("\ntdfyucy")

# file.close()
file=open('userdetail.txt','w')
username=input("Enter your username:")
password=input("Enter your password:")
content=file.write(f"{username}\n{password}")
file.close()


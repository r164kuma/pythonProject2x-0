#String
#Bunch of char
name = "Rakesh"
name2 = 'Rakesh'
print(name)
print(name2)
print(type(name))
print(type(name2))

dir = "C://abc.txt"
print(dir)
dir = 'C://abc.txt'
print(dir)
dir = 'C:/abc./abc.txt'
print(dir)
dir = 'C://abc.//abc.txt'
print(dir)
dir = 'C://abc.//abc.txt'
print(dir)
dir = 'C:\abc.//abc.txt'
print(dir)
dir = 'C:\nbc.//abc.txt'
print(dir)

#raw string concept
dir = r'C:\nbc.\abc.txt'
print(dir)

#formate string f
s = "Rakesh"
t = "Kumar"
age = 30
isMarried = True
print (f"your name is {s} {t} , your age is {age} and you are {isMarried}")



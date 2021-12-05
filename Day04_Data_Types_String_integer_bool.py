import math

myStr="*******hello world********"
str=myStr.replace("*","---",1)
print(str) #---******hello world********

str_1="%s is %d years old" % ("name", 36)
print(str_1)
# data=("Hodor","Hello")
# str_2="{first} {second}".format_map(data)
# print(str_2)

'''count'''

s="She sells seashells by the seashore"
print("the number of s is :" ,s.count("s")) # the number of s is : 7

int_1=s.lower().count("s",-9,-1)
print(int_1) # 2

'''endswith or startswith'''

myString = "Pyhton is perfect, isn't it?"
print(myString.endswith("?")) # True

print(myString.startswith("P")) # True

myString="hello"
print(myString.center(24, "*")) # *********hello**********

str_01="#"
print("\n",str_01.center(5,"-"),"\n",(3*str_01).center(5,"-"),"\n",(5*str_01).center(5,"-"),"\n",(3*str_01).center(5,"-"),"\n",(str_01).center(5,"-"))

'''encode'''
print("ç".encode("cp857"))
string_01 = "pythön"

print(string_01.encode("ascii","replace"))

'''expandtabs'''

mystring="xyz\tabc\t123"
print(mystring.expandtabs())

'''find & index'''

mystring="hello"
print(mystring.find("lo"), "position of lo is") # 3
print(mystring.index("lo")) # 3

print(mystring.rindex("o")) # 4

astring = "Hello on StackOverflow"
print(astring.find("w")) # 21

print(astring.rfind("o")) # 4

print(astring.find("o", 10, 21)) # 20

data="From murat.akca@techproed.com Sat Jan 4 19:10:16 2011"

start = data.find(" ")
print(start) # 4

end = data.find("@")
print(end) # 15

req=data[start+1:end]
print(req) #murat.akca

strIs="helloword"
print(strIs.isdigit()) # False
print(strIs.isnumeric()) # False
print(strIs.islower()) # True
print(strIs.isalpha()) # False


from string import Template

t=Template("$name is the $title of $company")
strSub=t.substitute(name="global", title="name", company="founder")
print(strSub) # global is the name of founder


'''int'''
print(round(3.145, 2)) # 3.15

print(bool(0)) # False

myInteger =15
print(bool(myInteger)) # True

print(bool(2 > 1)) # True

userName="erdem"
loginName=input("please enter your name : ").lower()
checkEq=bool( loginName==userName)
print("Validity is {}".format(checkEq)) #Validity is True

'''kullanıcıdan alınan bir yarıçap değeri ile dairenin çevresi
 ve alanın hesaplayıp ekrana basan bir program yazalım.'''

radius=input("Please enter a radius : ")
pi=math.pi
perimeter =2*pi*int(radius)
area=pi*int(radius)**2
print("The perimeter of the circle is : {}".format(perimeter))
print("The area of the circle is : {}".format(area))

'''bool'''





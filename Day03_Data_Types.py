import string

b = "Day03"
print(b)
print(b[1])
print(b[-4])
print(len(b))
x = 5
a = 5
print(id(x), id(a), sep=" <==> ")
myBool = False
# input_1 = input("please enter a number")
# input_2 = input("please enter a number")
# print(int(input_1)+int(input_2))

# print(len(6 * "hi"))
# myFruit = "banana"
# print(myFruit[0:7:2])
#
# s1=slice(1,4)
# print(myFruit[s1])
#
# a="this is a string"
# print(a.upper())
# print(a)
# print(a.lower())

# input = input("lutfen adinizi ve soyadinizi giriniz")
# print(input.upper())


'''STRING CLASS'''

str_1 = "this IS A STRING"

print(str_1.swapcase())

print(str_1.lower().title())

'''strip'''

str_2 = "xxxthis is xxx a string xxxx"
print(str_2.strip("x"))  # this is xxx a string
print(str_2.lstrip("x"))  # this is xxx a string xxxx
print(str_2.rstrip("x"))  # xxxthis is xxx a string

''' split '''

str_3 = "*h*e*l*l*o*"
print(str_3.split("*"))  # ['', 'h', 'e', 'l', 'l', 'o', '']

print(" merhaba dunya".split())  # ['merhaba', 'dunya']

smooth_chorus = """And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

myList = smooth_chorus.split("\n")
print(
    myList)  # ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]
print(myList[0])  # And if you said, "This life ain't good enough."

print(
    smooth_chorus.splitlines())  # ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]

'''replace'''

myString = "hello word"
print(myString.replace("o", "i"))  # helli wird
print(myString.replace("o", "iiii"))  # helliiii wiiiird
print(myString.replace("o", "ioi", 1))  # hellioi word ==> 2nci "o" yu degistirmedi

myString_2 = "benim adim \"erdem\""
print(myString_2)  # benim adim "erdem" ==> tirnak icinde tirnak
print("benim adim erdeQ\bm")  # benim adim erdem
print("benim adim\n erdem")  # benim adim
# erdem ==>new line

print("benim adim\t\t\t\t erdem")  # benim adim				 erdem ==>puts tab

'''maketrans'''
enigma = str.maketrans("aeiou", "+-*/?")
myString = "hello word"
myStr_1 = myString.translate(enigma)
print(myStr_1)  # h-ll/ w/rd

enigmaDecoder = str.maketrans("+-*/?", "aeiou")
myStr_2 = myString.translate(enigmaDecoder)
print(myStr_2)  # hello word

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print(max("hello word"))  # w
print(min("-1 hello word"))  # ' '

myString = "hello"
print(myString + " world")  # hello word

MyName = "benim adim {}"
name = "erdem"
print(MyName.format(name))  # benim adim erdem

print("hello {}, welcome to the {} world".format("erdem", "real"))  # hello erdem, welcome to the real world
print("hello {name}, welcome to the {spec} world".format(name="erdem",
                                                         spec="real"))  # hello erdem, welcome to the real world
print("{2}{0}{1}".format(" the real ", "world", "welcome to"))  # welcome to the real world
print("{0}{1}{0}".format("abra", "cad"))  # abracadabra

coord = (3, 5)
print("X:{0[0]}; y:{0[0]}".format(coord))  # X:3; y:3

format_1 = "{:<30}".format("align to left")  # 'align to left                  '
format_2 = "{:>30}".format("align to right")  # '                 align to right'
format_3 = "{:^30}".format("justify the text")  # '        justify the text        '
format_4 = "{:*^30}".format("fill the blanks")  # '*******fill the blanks********'

print(format_1, "\n", format_2, "\n", format_3, "\n", format_4)

myList=["apple", "banana"]
myList[-1]="grapes"
print(myList) # ['apple', 'grapes']
myList=myList+["banana"]
print(myList) # ['apple', 'grapes', 'banana']

myList=["apple", "banana"]

myList.append("hello")

print(myList)
myList.append([1,5,6])
print(myList)

'''Ortalama bulma'''
myList=[1,45,22,5,12,20]
print(myList)
print(sum(myList))
ortalama = sum(myList)/len(myList)
print(ortalama)

print(max(myList))

print(min(myList))

'''List devam'''

myList=["izmir", "Ankara"]
myList_2="Istanbul"
myList.append(myList_2)
print(myList) # ['izmir', 'Ankara', 'Istanbul']

myList[0]="Antalya"
print(myList) # ['Antalya', 'Ankara', 'Istanbul']


'''extend()'''

myList=["a","b","c"]
myList_2=["d","e"]
myList.extend(myList_2) # ['a', 'b', 'c', 'd', 'e']
print(myList)


myList.extend(range(50,70,5)) # '''extends ==> appends one by one, not as a single element'''
print(myList) # ['a', 'b', 'c', 'd', 'e', 50, 55, 60, 65]

myList.append([1,3,5]) # '''appends as an element'''
print(myList) # ['a', 'b', 'c', 'd', 'e', 50, 55, 60, 65, [1, 3, 5]]

'''Insert '''
myList.insert(-1,"hello")
print(myList) # ['a', 'b', 'c', 'd', 'e', 50, 55, 60, 65, 'hello', [1, 3, 5]]

myList.insert(len(myList),"istanbul")
print(myList) # ['a', 'b', 'c', 'd', 'e', 50, 55, 60, 65, 'hello', [1, 3, 5], 'istanbul']

myCity=["Ankara", "izmir", "istanbul"]
myCity2=["Antalya", "Usak"]
myCity.insert(-2,myCity2)
print(myCity) # ['Ankara', ['Antalya', 'Usak'], 'izmir', 'istanbul']

''' remove()'''

myCity.remove(["Antalya","Usak"])
print(myCity) # ['Ankara', 'izmir', 'istanbul']

''' pop()'''
myCity.pop()
print(myCity) # ['Ankara', 'izmir']

cikarilan= myCity.pop()
print(cikarilan) # izmir

myListem=['Ankara', 'izmir', 'istanbul',['Antalya','Usak']]
print(myListem.pop(1)) # izmir

'''clear()'''

myListem.clear()
print(myListem) # [] liste hala duruyor ama bos

'''del()'''
myListem=['Ankara', 'izmir', 'istanbul',['Antalya','Usak']]
del myListem # tamamen siler. liste artik mevcut degil

myListem=['Ankara', 'izmir', 'istanbul',['Antalya','Usak']]
del myListem[2:]
print(myListem) # ['Ankara', 'izmir']


'''sort()'''
harfler = ["a","d","e","c","b"]
harfler.sort()
print(harfler) # ['a', 'b', 'c', 'd', 'e']

harfler.sort(reverse=True)
print(harfler) # ['e', 'd', 'c', 'b', 'a']

# sort icin listedeki tum data tipleri ayni olmali

sayilar=[[1,8,9,10],[1,5,6,6]]
sayilar.sort()
print(sayilar) # [[1, 5, 6, 6], [1, 8, 9, 10]]

sayilar=[[1,8,9,10],[1,5,6,6]]
sayilar.sort(reverse=True)
print(sayilar) # [[1, 8, 9, 10], [1, 5, 6, 6]]

cities=['Ankara', 'izmir', 'istanbul','Antalya','Usak']
cities.sort()
print(cities) # ['Ankara', 'Antalya', 'Usak', 'istanbul', 'izmir']

cities.sort(key=len) # ascii degerine gore degil kelimelerin uzunluklarina gore sort eder
print(cities) # ['Usak', 'izmir', 'Ankara', 'Antalya', 'istanbul']

'''reversed()'''
myNumber=[1,5,9,8,4]
revNumbers=reversed(myNumber)
print(list(revNumbers)) # [4, 8, 9, 5, 1] ==> reversed fonksiyonu reverse ettikten sonra listeyi bir obje ye donusturur. dolayisiyla yenide list cevirmek gerekir

myNumber=[1,5,9,8,4]
myNumber.reverse()
print(myNumber) # [4, 8, 9, 5, 1]

#Not: range() fonksiyonu da tekrar bir listeye cevrilmeyi gerektirir
print(list(range(50,70,2))) # [50, 52, 54, 56, 58, 60, 62, 64, 66, 68]


'''copy()'''
myNumber=[1,5,9,8,4]
myNumber2=myNumber.copy()
print(myNumber2) # [1, 5, 9, 8, 4]

'''count()'''
myNewNumber=[50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
print(myNewNumber.count(64)) # 1


# nameCheck=input("Enter your name please ")
# names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
# finalCount=names.count(nameCheck)
# print("The count of the name you entered is ", finalCount)


'''index()'''
myNewNumber=[42, 34, 26, 18, 10, 10, 11, 10]
print(dir(myNewNumber))

print(myNewNumber.index(10,6)) # 7

'''TUPLES'''

myTuple=(1,5,6,"string",True)
print(myTuple) # (1, 5, 6, 'string', True)
# hem parantezli hem de parantezsiz assign edilebilir
myTuple=5,8,"hello"
print(myTuple) # (5, 8, 'hello')

isimler=("ahmet","mehmet","ayse","fatma")
a,b,c,d=isimler

print(c) # ayse

myTP="string", # ==> virgul olursa data type tuple olur
print(type(myTP)) # <class 'tuple'>

isimlerList=list(isimler)
isimlerList[0]="Ali"
isimler=tuple(isimlerList)
print(isimler)

tuple1=(123,"hello")
tuple2=("world",)
print(tuple1 + tuple2) # (123, 'hello', 'world')

print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')
print(tuple({"a": 1, "b": 2})) # ('a', 'b')

myTuple=tuple(isimler)
print("Ali" in myTuple) # True

print(myTuple.count("Ali")) # 1

print(myTuple.index("Ali")) # 0



'''SET'''

a=[] # type = list
a={} # type = dict
setim=set()
print(type(setim)) # type = set

mySet=set("hello")
print(mySet) # {'e', 'o', 'h', 'l'}

mySet2=set([1,5,6,6])
print(mySet2) # {1, 5, 6}

mySet2.add(20)
print(mySet2) # {1, 20, 5, 6}

lang= {"python","C++","Java","C"}
lang.add("Ruby")
print(lang) # {'Java', 'C', 'python', 'Ruby', 'C++'}

nums={1,5,9,11}
nums2={99,5,88,11}
nums3={100}

nums.update(nums2,nums3)
print(nums) # {1, 99, 100, 5, 9, 11, 88}

numsDict={1:"bir",5:"bes",77:"Yetmisyedi"}

nums.update(numsDict)
print(nums) # {1, 99, 100, 5, 9, 11, 77, 88} ==> sadece key value leri alır.

print(nums.pop()) # 1
nums.add(1)
print(nums)
print(nums.pop()) # 1
nums.add(1)
print(nums.pop())  # 99


fruits = {"apple","banana","cheery"}
fruits.remove("cheery")
print(fruits) # {'apple', 'banana'}

s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8} ==> or = union

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}

print(s1 & s2) # {4, 5} ==> and = intersection

print(s1.intersection(s2)) # {4, 5}

s1.intersection_update(s2)
print(s1) # {4, 5} update etti yeni deger {4,5} oldu

s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1 - s2) # {1, 2, 3}


print(s1.difference(s2)) # {1, 2, 3}

s2.difference_update(s1)
print(s2) # {6, 7, 8}

nums1={1,2,3,4,5}
nums2={4,5,6,7,8}

print(nums1.symmetric_difference(nums2)) # {1, 2, 3, 6, 7, 8}

nums1={1,2,3,4,5}
nums2={4,5,6,7,8}

nums1.symmetric_difference_update(nums2)
print(nums1) # {1, 2, 3, 6, 7, 8}

kume={5,7,"string"}
kume.remove(7)
print(kume) # {5, 'string'}

kume={5,7,"string"}
restrictedkume=frozenset(kume)

print(type(restrictedkume)) # <class 'frozenset'> ==> artık update edilemez

'''Dictionary'''

a={} # ==> empty dictionary

a["Ali"]=20
print(a) # {'Ali': 20}

a["mehmet"]=5
a["Veli"]=25

print(a) # {'Ali': 20, 'mehmet': 5, 'Veli': 25}

a["Ali"]=45
print(a) # {'Ali': 45, 'mehmet': 5, 'Veli': 25}

myDict=dict(a=1,b=5,c=7)
print(myDict) # {'a': 1, 'b': 5, 'c': 7}

myDict=dict([("a",1),("b",5),("c",7)])
print(myDict) # {'a': 1, 'b': 5, 'c': 7}

myVar = dict([("a",1)],b=2,c=3)
print(myVar) # {'a': 1, 'b': 2, 'c': 3}

print(myVar.values()) # dict_values([1, 2, 3])

print(myVar.get("w", "bulunamadi")) # bulunamadi

myDict={"a":[1,5,8],"b":8}
myDict["a"].append(10)
print(myDict) # {'a': [1, 5, 8, 10], 'b': 8}

nested={1:{"a":99,"b":98},2:{"a":2,"b":3}}
print(nested[1]) # {'a': 99, 'b': 98}

nested.pop(1)
print(nested) # {2: {'a': 2, 'b': 3}}

print(nested.pop(10, "bulunamadi")) # bulunamadi

print(nested.popitem()) # (2, {'a': 2, 'b': 3})

car={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car["color"]="blue"

print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue'}

car.setdefault("model","reno")
print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue'}
# varsa degistirmez eger key yoksa yeni deger atar.
# yeni bir sey atamak istiyoruz ama dictionary de var mi yok mu bilmiyorsak bu metodu kullaniriz
print(car["brand"]) # Ford


'''
https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python?utm_campaign=Pmax_feb25&utm_source=google&utm_medium=ppc&utm_content=&utm_term=&eid=5082902844932096&utm_term=&utm_campaign=%5BMar+25%5D+Pmax.+-+Coding+Interview+Prep&utm_source=adwords&utm_medium=ppc&hsa_acc=5451446008&hsa_cam=22344713166&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=22354833079&gbraid=0AAAAADfWLuS70rHftag96Ycol7F2BR5e7&gclid=Cj0KCQiA7rDMBhCjARIsAGDBuEAbxW6G8O4LJe3SPiNOXb2rmkPRbxigtMMlg0jpquQzKRbw4K_YomYaAlj4EALw_wcB

Docstring for DataStructures.All
Python collections are used to store data, for example, lists, dictionaries, sets, and tuples, 
all of which are built-in collections. Let’s understand and discuss the differences between these built-in collections.

List: A list is a collection of ordered data. The lists are declared with square brackets.
Tuples: A tuple is an ordered collection of data. Tuples are enclosed within parentheses.
Sets: A set is an unordered collection. Sets are represented in curly brackets.
Dictionaries: A dictionary is an unordered collection of data that stores data in key-value pairs. 
Dictionaries are enclosed in curly brackets in the form of key-value pairs.
'''
print("******************Create sequence*******************")
# Various ways to create a list
print("List Examples")  
list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))
print(list1)
print(list2)
print(list3)

# Various ways to create a tuple 
print("Tuple Examples")  
tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))
print(tuple1)
print(tuple2)
print(tuple3)

# How to create a set 
print("Set Examples")  
set1={1,2,3,4,5,"hello","tup"}
set2={(1,8,"python",7)}
print(set1)
print(set2)

# How to create a dictionary  
print("Dictionary Examples")  
dict1={"key1":"value1","key2":"value2"}
dict2={}   # empty dictionary
dict3=dict({1:"apple",2:"cherry",3:"strawberry"})
print(dict1)
print(dict2)
print(dict3)

print("**********************Mutable vs. immutable******************")
# List --- Adding, Removing, Ordering
print("List Examples")  
list1=["apple","kiwi","banana","grapes"]
list1.append("strawberry")   # strawberry is added to the list
print(list1)
list1.pop()  # removes the last element from the list
print(list1)
print(list1.sort())

# Tuple --- Adding and Removing
print("Tuples Examples")  
tuple1=(1,2,3,4)
# tuple1.pop()    tuple cannot be modified
# tuple1.append()  tuple cannot be modified
print(tuple1)

# Set --- Adding and Removing
print("Sets Examples")  
set1={"water","air","food"}
set1.add("shelter")   # adds an element to the set at random position
print(set1)
set1.add("clothes")
print(set1)
set1.pop()  # removes random element from the set
print(set1)

# Dictionary --- Adding, Removing, Ordering
print("Dictionary Examples")  
dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
dict1.update({"veg2":"brinjal"})
print(dict1)
dict1.update({"veg3":"chilli"})  # updates the dictionary at the end
print(dict1)
dict1.pop("veg2")
print(dict1)

print("***********index, count, and reverse operations on the built-in collections****************")

#List
print("List Examples:") 
list1=[1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2=[2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,2)) # returns the index value of the element from the particular start position given

#Tuple
print("Tuple Examples:") 
tuple1=(1,3,6,7,9,10)
print(tuple1.index(6))
print(tuple1.index(9))

#Set
print("Set Examples:") 
set1={1,5,6,3,9}
# set1.index()  will throw an error as they are unordered

#Dictionary
print("Dictionary Examples:") 
dict1={"key1":"value1","key2":"value2"}
# dict1.index("key1") will throw an error
print(dict1.get("key1"))
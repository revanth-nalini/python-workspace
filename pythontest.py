#python practice


#simple print

print("Hello Revanth")
#-----------------------------------------------------------------------


#indents

#case 1
if 1>0:
#print("1 is greater than 0") won't work
	print("1 is greater than 0")
		#print("1 is greater than 0 again") won't work
#print("1 is greater than 0 again") won't work
	print("1 is greater than 0 again")

#case 2
if 2>0:
	print("2 is greater than 0")
if 2>0:
		print("2 is greater than 0 again")
#-----------------------------------------------------------------------


#comments

#single line comment

" multi line "
" comment works when string isn't assigned to a variable "

print("comment won't apply till here") # comment works from here
#-----------------------------------------------------------------------


#variables

#case 1 - variable creation
x = 0
print(x)
print(type(x)) # type() is used to get type of variable

#case 2 - variable is not bound to a data type 
x = "name"
print(x)
print(type(x))

#case 3 - casting int(), float(), str()
x = float(1)
print(x)
print(type(x))


#case 4 - string works with " or '
x = 'name'
print(x)

#case 5 - variable is case sensitive
X = 'NAME'
print(X)

# myvar, my_var, _my_var, myVar, MYVAR, myvar2 acceptable variable names
# 2myvar, my-var, my var non acceptable variable names 
# camel case - myVariableName
# pascal case - MyVariableName
# snake case - my_variable_name

#case 6 - assign values to multiple variables in one line
x, y, z = 0, "name", 0.0
print(x,y,z) # output multiple variables

#case 7 - same value to multiple variables
x = y = z = "value"
print(x,y,z)

#case 8 - unpacking
list = ['e0','e1','e2']
x, y, z = list
print(x,y,z)

#case 9 - + operator to output multiple variables 
print(x + " " + y + " " + z) # using + operator with different datatypes (eg:str & int) causes error

#case 10 - global variable
g = "global"
def func():
	print(g + " variable")
func()

#case 11 - global & local variable
g = "global"
def func():
	g = "local"
	print(g + " variable")
func()

#case 12 - creating global variable from function
def func():
	global global0
	global0 = 0
func()
print(global0)

#case 13 - change global variable from function
global1 = 0
def func():
	global global1
	global1 = 1
func()
print(global1)
#-----------------------------------------------------------------------

 
#data types

"Text Type:	str"
"Numeric Types:	int, float, complex"
"Sequence Types:	list, tuple, range"
"Mapping Type:	dict"
"Set Types:	set, frozenset"
"Boolean Type:	bool"
"Binary Types:	bytes, bytearray, memoryview"
"None Type:	NoneType"

#case 1 - casting 
# str() ,int(), float(), complex(), list(()), tuple(()), range(), dict(), set(()), frozenset(()), bool(), bytes(), bytearray(), memoryview(())
#-----------------------------------------------------------------------


#numbers - int float complex

#case 1 - complex number
comp = 0+0j
print(comp)
print(type(comp))

# int - unlimited length postive or negative without decimal
# float - unlimited length postive or negative with decimal

#case 2 - float number
deci = 0e1
print(deci)
print(type(deci))

#case 3 - casting
#cannot convert complex numbers into another number type using casting
print(float(1))
print(int(1.001))

#case 4 - random numbers
import random
print(random.randrange(1,10))
#-----------------------------------------------------------------------


#casting - int(), float(), str() - primitive object constructor

x = int(1)
y = float(1)
z = str(1)
print(x,y,z)
#-----------------------------------------------------------------------


#string

#case 1 - multiline string
multline1 = """line 1
line 2
line 3"""
print(multline1)
multline2 = '''line 4
line 5
line 6'''
print(multline2)

#case 2 - slicing string
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets[0:5])
print(alphabets[:5])
print(alphabets[5:])
print(alphabets[-3:-2])
print(alphabets[-3:])
print(alphabets[:-3])

#case 3 - string methods
alphabetsl = "abcdefghijklmnopqrstuvwxyz"
print(alphabetsl.upper())
alphabetsu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabetsu.lower())
trim = "  abc  "
print(trim.strip())
name = "chotu"
print(name.replace("tu","2"))
greet = "Hello"
print(greet + " " + name)

#case 4 - string format as number type and string cannot be concatenated
one = 1
two = 2
three = 3
number = "one {} two {} three{}"	
print(number.format(one,two,three))
numberindex = "one {2} two {1} three{0}"
print(numberindex.format(three,two,one))	

#case 5 - escape chars \" \' \\ \n \r \t \b \f \ooo \xhh
quote = "He said \"\Hello!\\\" to me"
print(quote)
#-----------------------------------------------------------------------


#boolean


print(0==0)
print(bool(1))
print(bool(0))
print(bool("."))
print(bool(""))
#-----------------------------------------------------------------------


#operators

# case 1 - arithmetic + - * / % ** //
print(2**5)  # 2 power 5
print(11//2) # 11 div 5 as whole no

#case 2 - assignment = += -= *= /= %= //= **= &= |= ^= >>= <<=
#case 3 - comparison == != > < >= <=
#case 4 - logical and or not

#case 5 - identity is is not
mem1 = 0
mem2 = mem1
print(mem1 is mem2)

#case 6 - membership in not in
letter = {'a','b','c'}
print('a' in letter)

#case 7 - bitwise & | ^ ~ << >>
#-----------------------------------------------------------------------


#list

list = ["a","b","c"]
print(list)
print(len(list)) # list length
list = ["a",1,True] # can hold different data types
print(list)
print(type(list)) # <class 'list'> type
# list = list(("a","b","c"))
# print(list)
print(list[0])
print(list[-1]) # -1 is the last element in the list
print(list[1:2]) # 1 is inclusive and 2 is exclusive
print(list[:2]) # exclusive of 2
print(list[1:]) # inclusive of 1
print(list[-3:-1]) # -1 is exclusive. [-1/-2/-3:0] will give []
print(1.0 in list) # True
list[1] = 0 # replace an item
print(list)
list[1:3] = [1,False] # replace range
print(list)
list[1:2] = [0,True] # replace range case 1
print(list)
list[2:4] = [1] # replace range case 2
print(list)
list.insert(3,True) # insert item without replace. any val> 3 will be accepted
print(list)
list.append(False) # insert at end of the list
print(list)
list.extend(["b","c"]) # extend list
list.extend(("b","d")) # extend tuple
print(list)
list.remove("b") # removes first occurance
print(list)
list.pop(6) # removes the index
print(list)
list.pop() # removes the last item
print(list)
del list[5] # removes the 5th item
print(list)
list.clear() # empties the list
print(list)
del list  # deleted the list from memory

list = ["x","y","z"]
for e in list: # for loop
	print(e)
for i in range(len(list)): # indexed for
	print(list[i])
i = 0
while i < len(list): # while loop
	print(list[i])
	i+=1
[print(e) for e in list] # comprehension
newlist = [e for e in list if True]
print(newlist)
newlist = [e for e in range(10) if e<=5]
print(newlist)
newlist = [e.upper() for e in list]
print(newlist)
newlist = [e if e!="z" else "zz" for e in list]
print(newlist)

list = ["b","d","a","c"]
list.sort() # ascending sort
print(list)
list = [5,2,3,1,4]
list.sort() # ascending sort
print(list)
list = [5,2,3,1,4]
list.sort(reverse = True) # descending sort
print(list)
list = [2,3,4,6,7,8]
def sortfunc(n):
	return abs(n-5)
list.sort(key = sortfunc) # custom sort
print(list)
list = ["b","B","D","d","a","A","C","c"]
list.sort(key = str.lower) # case insensitive sort
print(list)
list = ["b","d","a","c"]
list.reverse() # reverse order
print(list)

list = ["a","b","c"]
copylist = list.copy()
print(copylist)
# copylist = list(list)
# print(copylist)

alist = [1,2,3]
blist = ["a","b","c"]
list = alist + blist # join list
print(list)
alist = [1,2,3]
blist = ["a","b","c"]
for l in blist:
	alist.append(l) # join using for
print(alist)
alist = [1,2,3]
blist = ["a","b","c"]
alist.extend(blist) # join using extend
print(alist)
#-----------------------------------------------------------------------


#tuple

tuple = ("a","b","c")
print(tuple)
print(len(tuple)) # list length
tuple=("a",) # for single item comma has to be added at the end
print(tuple)
print(type(tuple)) # <class 'tuple'>
tuple = ("a",1,True) # can hold different data types
print(tuple)
# tuple = tuple(("a",1,True))
print(tuple[0])
print(tuple[-1]) # -1 is the last element in the list
print(tuple[0:3]) # 0 is inclusive and 3 is exclusive
print(tuple[:2]) # exclusive of 2
print(tuple[1:]) # inclusive of 1
print(tuple[-3:-1]) # -1 is exclusive. [-1/-2/-3:0] will give []
print(1 in tuple)

# tuple = ("x","b","c")
# listcopy = list(tuple)
# listcopy[0] = "a" # modify item in tuple
# tuple = tuple(listcopy)
# print(tuple)

# tuple = ("x","b","c")
# listcopy = list(tuple)
# listcopy.append("d") # append item to tuple
# tuple = tuple(listcopy)
# print(tuple)


tuplea = ("a","b")
tupleb = ("c",)
tuplea+=tupleb # append item to tuple
print(tuplea)

# tuple = ("a","b","c","d")
# listcopy = list(tuple)
# listcopy.remove("d") # remove item in tuple
# tuple = tuple(listcopy)
# print(tuple)

del tuple # delete a tuple

tuple = ("a",1)
x,y = tuple # unpacking tuple
print(x)
print(y)

tuple = ("a","b","c")
for x in tuple: # for loop
	print(x)
for i in range(len(tuple)): # indexed for
	print(tuple[i])
i=0
while i < len(tuple): # while loop
	print(tuple[i])
	i+=1

tuple = ("a","b","c")
tuple = 2*tuple
print(tuple)
#-----------------------------------------------------------------------


#set

set = {"a","b","c"}
print(set)
set = {"a","b","c","a"} # no duplicates allowed {a,b,c}
print(set)
print(len(set)) # length of set
set = {"a",1,True} # can hold different data types + True is considered as 1
print(set)
print(type(set)) # <class 'set'>
# set = set(("a","b","c"))

for e in set: # for loop
	print(e) 
print(True in set) 

set.add(False) # add item to set
print(set)
addset = {"b","c"}
set.update(addset) # add set to existing set
print(set)
addlist = [2,3]
addtuple = (4,5)
set.update(addlist) # add list to set
set.update(addtuple) # add tuple to set
print(set)

set.remove(4) # removes item from set - will raise error if item not present
set.discard(5) # removes item from set - does not raise error if item not present
print(set)
print(set.pop()) # randomly removes element
set.clear() # empties set
print(set)
# del set # deletes set

seta = {"a","b","c"}
setb = {1,2,3}
setc = seta.union(setb) # adds two sets and creates a new set
print(setc)
#-----------------------------------------------------------------------


#dictionary
dict = {"a":0,"b":1,"c":2}
print(dict)
print(dict["a"]) # access value associated with a key
dict = {"a":0,"b":1,"c":2,"a":3} # duplicate values overwrite existing value
print(dict)
print(len(dict)) # length of dictionary
dict = {"a":"a",1:1,False:["a"]} # can hold different data types + False is considered as 0
print(dict)
print(type(dict)) # <class 'dict'>
# dict = dict("a"="a","b"="b","c"="c")
# print(dict)

print(dict.get(False)) # access value associated with a key
print(dict.keys()) # returns list of all keys
dict[1.0] = True # change value of an item
print(dict)
dict.update({0:0}) # change value of an item if key exists or adds item to the dict
print(dict)
dict[0.01] = 0.01 # adds item to dict
print(dict)

dict.pop("a") # removes specified key from dict
print(dict)
dict.popitem() # removes last inserted item from dict
print(dict)
del dict[1] # delted specified key from dict
print(dict)
dict.clear() # empties dict
print(dict)
# del dict # deletes dict

dict = {"a":"a",1:1,False:["a"]}
for e in dict: # for loop
    print(e, dict[e])
for e in dict.keys(): # loop only keys
    print(e)
for e in dict.values(): # loop only values
    print(e)
for k,v in dict.items(): # loop all items
    print(k,v)

dictcopy = dict.copy()
print(dictcopy)
# dictcopy = dict(dict)
# print(dict)

dict = {
    "dict1" : {"name" : "a", "val" : 0},
    "dict2" : {"name" : "b", "val" : 1}
    }
print(dict) # nested dict

dict3 = {"name" : "c", "val" : 2}
dict4 = {"name" : "d", "val" : 3}
dict = {"dict3" : dict3, "dict4" : dict4}
print(dict) # nested dict








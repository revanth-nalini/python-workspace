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





















































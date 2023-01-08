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


#python numbers - int float complex

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













































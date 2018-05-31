''''
my_list=[1,2,3,4]
print(my_list)
my_list.append(5)
print(my_list)
my_list.pop()
print(my_list)
my_list=[1,2,3,4]
#print(help(my_list.insert))
my_list.insert(5,'insert function')
print(my_list)
'''

'''
def say_hello(name='ronaldo'):
	
	#simple fucntion to say hello 
	
	print('hello' + name)
say_hello()
'''
'''

def  football(name):
	print( 'UEFA champions are ' + name)
football('real madrid')
'''
################ Function   with R E T U R N function ######
'''
def football(name):
	return 'most goals scored by ' + name
result = football('ronaldo')
print(result)
'''


'''
def add(num1,num2):
	return num1 +num2
result= add(20,500)
print(result)
'''


'''
def dog_present(my_string):
	if 'dog' in my_string:
		return True
	else:
		return False 
result= dog_present('dog saved life')
print(result)
'''
###########to chekc if a particular string is presnt in the given string ########

'''
def dog_check(my_string):
	return 'dog' in my_string.lower():
dog_check('My DOG ran away ')
#print(result)
'''


###############   p i g latin #####################

'''
def pig_latin(word):
	first_letter =word[0]
	if first_letter in 'aeiou':
		pig_word =word+ 'ay'
	else:
		pig_word =word[1:] + first_letter + 'ay'
	return pig_word
result=pig_latin('bpple')
print(result)
'''
'''
def myfunc():
    print('Hello World')
myfunc()
'''

'''
def myfunc(name=' Name'):
    print('Hello'+name)
myfunc()
'''

'''

def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'
result=myfunc(True)
print(result)

'''

'''

def myfunc(x,y,z):
    if z == True:
        return 'x'
    else:
        return 'y'
result=myfunc('hello','howw',True)
print(result)

'''
'''
def is_even(num):
    if num %2 == 0:
        return True
    else:
        return False
result=is_even(10)
print(result)
'''

def is_greater(x,y):
    if (x > y) :
        return True
    else :
        return False
result=is_greater(15,20)
print(result)
















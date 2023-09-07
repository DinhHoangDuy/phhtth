n1 = 9
n2 = 8
str1 = 'Hello World'
arr1 = [1,2,3,4]
arr2 = [1.2, 'Hello']
#===========[For...in]==========
print (str1)

for letter in 'Python':
    print ('Current letter: ', letter)
#=========[If]============
print('................')
num1 = 9
num2 = 15
num3 = -10
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

#===========[While]==========
print('................')
count = 0
while (count <= 9):
    print ('The count is: ', count)
    count += 1
#=========[Definition]============
print('................')
def sum1(a,b):
    sum1 = a+b
    return (sum1)

print ('The sum1 def returns: ', sum1(n1,n2))

def plus(c,d = 10):
    return (c+d)

print ('The plus def returns: ', plus(n1))

print ('The sum1(b,a) def returns: ', sum1(b = 44, a = 10))
#========[String]=============
print('................')
str1 = 'Hello'
str2 = 'World'
str3 = '''Hello

World!!!!'''
print(str3)

str4 = str1 + " " + str2
print(str4)

print(str4[0:4])
print(str4[-3:])
print(str4[6:-3])

print('Lengh of str4: ', len(str4))

str5 = 'Hello World'
str5 = str5.replace('Hello', 'Bye')
print(str5)
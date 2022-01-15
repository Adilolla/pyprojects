# chapter 1
x = 5
y = "John"
# print(x)
# print(y)

# chapter 2
x = 4
x = "sally"
# print(x)

# chapter 3 Casting
x = str(3)
print("x value is ", x)


#chapter 4 strings

print('hello')
print("hello")

a = "Hello,World!"
print(a[1])

#looping through a string

for x in "banana":
    print (x)

#if statements in strings(useful for quiz)

txt = "The best things in life are free"

if "free" in txt:
    print("yes, free is present")

txt = "The best things in life are free"

if "Aditya" not in txt:
    print("No, Aditya is  not present")


#get type
x= 5
y= "John"
print(type(x))
print(type(y))
#CHAPTER 5

x,y,z = "orange","banana","Cherry"

print(x)
print(y)
print(z)


x=y=z = "orange"
print(x)
print(y)
print(z)

##list unpacking
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)


#chapter 7

x = "awesome"
print("python is " + x)
#!/usr/bin/env python
# coding: utf-8

# # Q.1 

# Write a short Python function, is $multiple(n, m)$, that takes two integer values and returns True if $n$ is a multiple of $m$, that is, $n=m \times i$ for some integer $i$, and False otherwise.

# In[11]:


def is_multiply(n,m):
    assert m>1, "m value should be greater than 1"
    if n%m==0:
        return True
    else:
        return False
is_multiply(20,3)


# # Q2

# Write a short Python function, $is even(k)$, that takes an integer value and returns $True$ if $k$ is even, and $False$ otherwise. However, your function cannot use the multiplication, modulo, or division operators.

# In[12]:


# Solution 1 using loop structure
def isEven(n):
    isEven = True;
    for i in range(1, n+1):
        if isEven == True:
            isEven = False;
        else:
            isEven = True;
 
    return isEven;
# execute the function
n = 101;
if isEven(n) == True:
    print ("Even");
else:
    print ("Odd");


# In[13]:


# Solution 2 using bitwise operator
def isEven(n) :
      
    # n&1 is 1, then
    # odd, else even
    return (n & 1);

# execute the code
n = 101;
if(isEven(n) == 0) :
    print ("Even");
else :
    print ("Odd");


# # Q3

# Create a function $EvenList(n)$ that takes a parameter $n$ to input $n$ number from users and returns the list of only even numbers.

# In[15]:


def EvenList(n):
    evenlist = []
    for i in range(n):
        y = int(input('Enter the numbers:'))
        if y % 2 == 0:
            evenlist.append(y)
    return evenlist
#Execute code
ls=EvenList(5)
print(ls)


# # Q4

# Write a short Python function, $minmax(data)$, that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

# In[29]:


def minmax(data):
    min=data[0]
    max=data[0]
    for i in range (1,len(data)):
        if data[i]<min:
            min=data[i]
        if data[i]>max:
            max=data[i]
        
    return min, max
tp=minmax([5,1,6,3,9])
print('Min:%d and Max:%d' %(tp[0],tp[1]))


# # Q5

# Write a short Python function that takes a positive integer $n$ and returns the sum of the squares of all the positive integers smaller than $n$.

# In[33]:


def sumsquares(n):
    Total=0
    for i in range(n):
        Total+=i**2
    return Total

print(sumsquares(4))
        


# # Q6

# Write a short Python function that takes a positive integer $n$ and returns the sum of the squares of all the odd positive integers smaller than $n$.

# In[36]:


def sumoddsquares(n):
    Total=1
    for i in range(n):
        if i>1 and i%2:
            Total+=i**2
    return Total

print(sumoddsquares(4))


# # Q8

# Create a function Unique that takes a list as a parameter and returns a list containing only unique elements i.e. duplicate elements should be removed.

# In[37]:


def Reverse(list):
    print(list[::-1])

Reverse([2,4,6])
    


# # Q9

# Create a function Unique that takes a list as a parameter and returns a list containing only unique elements i.e. duplicate elements should be removed.

# In[38]:


def Unique(lst):
    newlist =[]
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist

lst = [1,2,2,3,4,5,5,6]
x = Unique(lst)
print(x)


# # OOP

# ## Example 1: Creating Class and Object in Python

# In[39]:


class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ### instantiate the Parrot class

# In[40]:


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# ### access the class attributes

# In[41]:


print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))


# ### access the instance attributes

# In[42]:


print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


# ## Example 2 : Creating Methods in Python

# In[43]:


class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)
    
    def set_name(self,na):
        self.name=na

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
blu.set_name("Green")
print("Parrot name is: ",blu.get_name())


# ## Example 3: Use of Inheritance in Python

# In[44]:


# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# ## Encapsulation

# Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

# In[45]:


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# ## Polymorphism

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# 
# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

# In[46]:


class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


# # Animal Class

# In[55]:


class Animal(object):
    def __init__(self,age=0):
        self.newage=age
        self.newname=None
    
    def get_age(self):  
        return self.newage

    def get_name(self):  
        return self.newname

    def set_age(self, newage):  
        self.newage = newage

    def set_name(self, newname=""):
        self.newname = newname  
    
    def __str__(self):
        return "animal:"+str(self.newname)+":"+str(self.newage)

myanimal = Animal()
myanimal.set_name("Cat")
print(myanimal)


# # INHERITANCE: SUBCLASS

# In[56]:


class Cat(Animal):
    def speak(self):
        return "meow"
    def __str__(self):
        return "cat:"+str(self.newage)


# In[57]:


mycat = Cat(3)
mycat.set_name("fluffy")
print(mycat)
print("my cat speaks: "+mycat.speak())


# In[ ]:





# # int

# a = 1
# print("a is of type: ", type(a))

# # float

# a = 1.2
# print("a is of type:",type(a) )


# # string

# a = "rishika"
# print("a is of type:",type(a))

    


# # dictionary
# a = {
#     "rishika": {1,2,3}, 
#      "rishabh": "sharma", 
#      "Radha": {"Lall", "hello"}
#     }
# print("a is of type:",type(a))




# # set
# a = {1,2,3,4}
# print("a is of type:",type(a))


# list
# a = [1,2,3,4] # changeable

# print("a is of type:",type(a))

# list all the elements of a using a for loop

# print(len(a)) # number of elements in the list: 4
# print(range(len(a))) # creates a range from 0(unparameterized) to len(a): 4

# for index in range(len(a)):
#     print(a[index])

# for i in a:
#     print(i)

## pop, append
# a.pop(1) # we give index to pop
# print(a)

# a.append(5) # we give number to insert
# print(a)

# a[1] = 2 # updating the value at index 1
# print(a)


# # # tuple
# b = (1,2,3) # not changeable
# print("b is of type:",type(b))

# for i in range(len(a)):
#     print(a[i])

# # boolean
# a = True
# b = False
# print("a and b are of type:", type(a), type(b))
# print("a:", a, "and b", b, "are of type: ", type(a), "and",type(b))

# make a list of your friends name, and print all the elements of it:

# a = ["Rishika", "Su", "Jessi"]
# for i in a:
#     print(i)

# dict = {
#     "rishika": ["lall", "Indore", "MP"],
#     "su": ["upadhyay", "bhopal", "MP"], 
#     "jessi" : ["castelino", "goa", "goa"]
# }
# # print(dict)
# print(dict.items())

# for key, value in dict.items():
#     print(key)
#     for v in value:
#         print(v)

a = [1,2,3,4,5,6,7,8,9,10]

# a,b = 1,2

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# print the table of 9 using for loop

# for i in a:
#         print(i*9)


# # print the even numbers using a for loop

# for i in a:
#     if i%2 == 0:
#         print(i)

# # print the odd numbers using a for loop

# for i in a:
#     if i%3 == 0:
#         print(i)


# # print multiples of 3 using for loop

# for i in a:
#     if i%3 == 0:
#         print(i)

# append first 20 multiples of 98 in a list
        
def twmultiplesof98(num):
    l = []
    a = range(0,21)
    for i in a:
        l.append(i*num)
    return l
    
# r = twmultiplesof98(98)
# print(r)
     
# list =  twmultiplesof98()
# print(list)

def checkifeven(i):
    if i%2 == 0:
        return True
    else:
        return False
    
# check = checkifeven(9)
# print(check)

def writeTable(number):
    l = []
    a = range(0,11)
    for x in a:
        l.append(x*number)
    return l

# tof2 =  writeTable(2)
# print(tof2)

# write a function to find elements that are repeating in a list
l = [1,1,1,2,3,4,4]

def findrepnumbers(list): # aaj karenge
    # should return numbers that repeat
    occurence = {}
    non_repeat = []
    for i in list:
        if i in occurence:
            occurence[i]+=1
        else:
            occurence[i] = 1
    for key, value in occurence.items():
        if value  == 1:
            non_repeat.append(key)
    return non_repeat

print(findrepnumbers(l))

# write a function to calculate any two numbers

def calculator(n, m, operation):
    #number1 is a number
    #number2 is a number
    #operation is a string
    if operation == "add":
        return n+m
    elif operation == "sub":
        return n-m
    elif operation == "mul":
        return n*m
    elif operation == "div":
        return n/m
    elif operation == "mod":
        return n%m
    elif operation == "equals":
        return n==m


# out = calculator(2,3,"add")
# print(out)
# out = calculator(2,3,"sub")
# print(out)
# out = calculator(2,3,"mul")
# print(out)
# out = calculator(2,3,"div")
# print(out)
# out = calculator(2,3,"mod")
# print(out)
# out = calculator(2,3,"equals")
# print(out)
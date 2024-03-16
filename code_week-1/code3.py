# write a function to iterate over both of the list and calculate m, i.e. slope of the line, the intercept c = 0;
# equation of line y = mx + c
# output should be a list of slopes
x = [10,20,30,40,50,60,80]
y = [15,30,45,60,75,90,120]

def calSlope(x1, y1):
    m = y1/x1
    return m

def slopeList(x, y): # x, y are the arguments
    l = []
    if len(x) == len(y):
        for i in range(len(x)):
            m = calSlope(x[i], y[i])
            l.append(m)
    return l # l is my list which is my output

out = slopeList(x, y)
print(out)

# create a dictionary of 10 key value pairs, the key should be a number and value should be a string.
# then using that dictionary create two lists, one of keys and one of values. use function for this
# iterate through both lists together and prinnt them

Dict = {16: "Rishika", 11: "Rishabh", 12: "Radhika", 22 : "Prathue",24: "Kiru", 28:"Kamal", 10:"Su", 9:"chitra",9:"Stupid", 18:"pagal",}

def Namedob(Dict):
    l1 = []
    l2 = []
    for key, value in Dict.items():
        l1.append(key)
        l2.append(value)
    return l1, l2

out1, out2 = Namedob(Dict)

for i in range(len(out1)):
    print(out1[i], "  ",out2[i])





    
 # function
""" def hello():
    print("hello function")

hello()


# example
def hello1(a):
    print(a)

hello1(100)


# example
def add(a=2, b=3):
    print(a + b)

add(10, 5)
add()


# example
def power(a, b):
    print(a ** b)

power(5, 2)

print(power) 
# example
def student(*a):
    print(a)
    print(type(a))
    print(a[0])

student(1,2,3,4,5)
def marks(*a):
    for i in a:
        print(i)
 
marks(10,20,30,40,50) """
# example

""" def address(a) :
    for i in a :
        for j in i :
            print (j)
address(["Hello","vijay"])
# example
def sum(a,b):
    return a+b
result = (10+20)
print(result) """

# LAMBDA FUNCTION
# [LAMBDA ARGUEMENTS : EXPRESSION]
""" add = lambda x:x
print(add(100))
sum = lambda x,y: x+y
print(sum(10,20))
a = lambda x:x
print(a([10,20,30,40,50]))
# exampele
add = lambda*num: sum(num)
 
print(add(1, 2, 3))
print(add(10, 20, 30, 40)) """
# LIST COMPREHENSION [expression for item is iterable]
""" l = [10,20,30,40,50]
print([l[i] for i in range(len(l))]) """
#
""" l =[10,20,[30,40,50,60]]
print([l[2] for i in range(len(l[2]))])
# list
l = [10,20,30]
print(len(l))
l.append(40)
print(l)
print(l[0])
# example
l = ["hello","python"]
l.append("vijay")
print(l)
print(l[0])
print(l[-1])
#insert
l = [True,False,10,20]
l.insert(1,100)
print(l)
#
l = [10,20,30,{"name":"vijay","address":["jaipur","kukas","home town","friend house"]}]
print(l[3]['address'])
for i in l[3]['address']:
    print(i)
    #example
    l = [10,20,30,[40,50,[60,70,80]]]
    for i in range(len(l[3])-1):
        print(l[3][i]) """
        # DICTIONARY
""" D = {'NAME':'HELLO'}
        D['NAME'] -> HELLO
        D.KEYS () -> ['NAME']
        D.VALUES -> ['HELLO']"""
        #
""" d = {"name": "hello","age": 20}
print(d.keys())
print(d.values())
for i in d.keys():
    print("key=",i)
    print("value=",d[i]) """

d = {
  "Message": "Number of Post office(s) found: 6",
  "Status": "Success",
  "PostOffice": [
    {
      "Name": "Achrol",
      "Description": "",
      "BranchType": "Sub Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Jaitpura Khinchi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kali Pahadi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kant",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Labana",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Rajpurawas Tala",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    }
  ]
}
print(d.keys())
print(d.values())
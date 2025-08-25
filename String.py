from babel.dates import parse_time

x="Shanzid Helal EMon"
y="""Hello I am Shanzid Helal EMon.
I want to be an AI engnieer because i know AI is the future"""#Multiline String using double quation
print(x)
print(y)
#using String of array
h="Shanzid Helal EMon"
z=x[3]
print(z)#so string is array which can be access by index number.
#loop in string
print("List of banana using for loop")
for x in "Banana":
    print(x)
z="Banana"
print(len(z))
#bollean check using in operator
h="Hello guys i'm Shanzid Helal Emon.And i wan to be an AI engineer."
print("faild" in h)
#check in string using ig/else
if("free" in h):
    print("Free in the H")
else:
    print("free is not in H")
#using not in operator in string statement.
z="Hello World"
if("free" not in z):
    print("free is not in h")

u = int(input("please, enter a number"))  #Մուտքագրել թիվ և տպել դրա կրկնաապատիկը։
print(2 * u)

u = int(input("please enter the first umber " "")) #Մուտքագրել երկու թվեր և տպել դրանց գումերը։
p = int(input("please enther the second number "" "))
print(u + p)

u = int(input("please enter any number " " ")) #Մուտքագրել ցանկացած թիվ,որպես ժամ և փոխակերպել այն վայրկյանների։
print(f" your number is {3600*u} in seconds")

u = int(input("please enter your birdth year " "")) #Մուտքագրել ծննդյան տարեթիվը և տպել տարիքը։
print(f"you are {2026-u} years old")

m = int(input("please enter the mass of the object " "")) #Մուտքագրել մարմնի զանգվածը և ծավալը, տպել խտությունը։
v = int(input("please enther the volume of the object"))
print(f"the density of the object is {m/v} kg / meter **3")

a = int(input("please enter the first number " "")) #Մուտքագրել երկու թիվ և տպել դրանց արտադրյալը։
b = int(input("please enter the second number " ""))
print(f"the product of {a} and {b} is {a*b}")

a = int(input("please enter the first number " "")) #Մուտքագրել 4 թիվ և հաշվել դրանց թվաբանական միջինը։b = int(input("pleas enter the second number " ""))
c = int(input("please enter the third number " ""))
d = int(input("please enter the fourth number " ""))
print(f"the mean of {a},{b},{c},{d} is {(a+b+c+d)/4}" )

a = input("please enter your name " "") #Մուտքագրել անուն ազգանուն և տպել դրանք գծիկով։
b = input("please enter your surname " "")
print(f"your full name is {a}-{b}")

a = int(input("please anter any number")) Մուտքագրել թիվ և այդ թվին աջից կցագրել 7։
print(str(a)+"7")

a = int(input("please enter the length of square's side")) #Մուտքագրել քառակուսու կողմի երկարությունը և հաշվել դրա մակերեսը։
print(f"the area of the square is {a ** 2}")

a = int(input("please enter the value of the rectangle's length " "")) #Մուտքագրել ուղղանկյան կայնությունը և երկարությունը , հաշվել դրա պարագիծն ու մակերեսը։
b = int(input("please enter the value of the rectangle's width "" " ))
print(f"the area of the rectangle is {a*b} and the permimeter of the rectangle is {(a+b)*2}")

a = (input("please enter a number """))#Մուտքագրել թիվ և տպել նրա հակադարձը:
print(a[::-1])

n = int(input("enter the temperature in Newtons """)) #Մուտքագրել ջերմաստիճանը Նյուտոնով և փոխակերպել ցելսիուսի։
print(f" the temperature in celsius is {n*100/33} ")

a = int(input("please enter the temperature in delse scale:"))#Մուտքագրել ջերմաստիճանը դելսի չափման միավորով ու փոխակերպելայն ցելսիուսի։
print(f"the temperature in celsius is {2/3*(a+100)}")

s = int(input("please enter the distance between two cities")) #Մուտքագրել երկու քաղաքների միջև եղած հեռավորությունը, մեքենայի ունեցած արագությունը և հաշվել թե մեքենան քանի ժամում կհասնի իր նպատակակետին՝ երկրորդ քաղաք։
v = int(input("please enter the spped of the car"))
print(f"the car will reach its destination {s/v} hours after the start")

v = int(input("please enter the speed in km/h"))#Մուտքագրել արագությունը կմ/ժ ով և փոխակերպել այն մ/վ ի։
print(f"the speed in m/s is {v*1000/3600}")

x1 = int(input("please enter the x coordinate of point A"))#Մուտքադրել երկու կետերի կոորդինատները և որոշել դրանց միջնակետը։
x2 = int(input("please enter the x coordinate of point B"))
y1 = int(input("please enter the y coordinate of point A"))
y2 = int(input("please enter the y coordinate of point B"))
print(f"the midpoint of A and B is ( {(x1+x2)/2} , {(y1+y2)/2} )")

r = int(input("please enter the radious of the circle "" ")) #Մուտքագրել շրջանագծի շառավիղը և հաշվլե դրա երկարությունը։
print(f"the circumference of the circle id {2*3.14*r}")

a = int(input("please enter the price of a product"))
b = int(input("please enter the new price of a product"))

if a > b: #Մուտքագրել ապրանքի հին և նոր գնորը և հաշվել դրանց միջև տոկոսային գնաճը կամ նվազեցումը։
    print(f"the price has decreased by {(a-b)/b *100} %")
else:
    print(f"the price has increased by {(b-a)/a *100} %")

a = int(input("please enter the price of the product"))#Մուտքագրել ապրանքի սկզբնական գինը, զեղչի տոկոսը և հաշվել վերջնական գինը։
b = int(input("please enter the percent of discount"))
print(f"the discounted price of the product is {a*(1-b/100)}")

symbol = input("please enter any symbol: "" ") #Մւտքագրել ցանկացած նշան և տպել քառակուսի 10*10 չափսերով։
for i in range(10):
    print(symbol*10)


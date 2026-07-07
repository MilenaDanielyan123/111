#n = int(input("please enter 1st number " "")) # Մուտքագրել 2 թիվ և գտնել մեկը մյուսի վրա բաժանելիս ստացված մնացորդը։
#m = int(input("please enter 2nd number "" "))
#if n>m:
#    print(n%m)
#else:
#    print(m%n)    

#n = int(input("please enter 1st number " "")) # Մուտքագրել 2 թիվ և գտնել մեկը մյուսի վրա բաժանելիս ստացված քանորդը։
#m = int(input("please enter 2nd number "" "))
#if n>m:
#    print(n//m)
#else:
#    print(m//n)    

#n = int(input("please enter a number")) #Մուտքագրել թիվ և տպել դրա վերջին թվանշանը։
#print(n%10)

#a = float(input("please enter a number"))#Մուտքագրել թիվ և հաշվել այդ թվի քառակուսի արմատը։
#sqrt = a ** 0.5
#print(f"the square root of {a} is {sqrt}")

#a = float(input("please enter a number "" "))#Մուտքագրել 2 թիվ և հաշվել 1-ին թվի 2-րդ թվին համարժեք աստիճանը
#b = float(input("please enter the value of exponent "" "))
#r = a ** b
#print(r)

#x = int(input("please enter the value of x")) #Մուտքագրել թիվ x - ի արժեքի համար և հաշվել y-ի արժեքը որոշակի ֆունկցիայի համար։
#y = 2 * x **3 - 4 *x**2 +17
#print(f"the corresponding value of y to {x} is {y}")

#x = int(input("Enter the first number: "" ")) #Մուտքագրել 2 թիվ և տպել այդ երկու թվերի գումարի տասնավորը։
#y = int(input("Enter the second number "" "))
#print(((x+y)//10)%10)

#x = int(input("Enter the number of chocolates you need to distribute")) #Մուտքագրել քաղցրավենիքի և մարդկանց քնակը, քաղցրավենիքը հավասարապես բաժանել մարդկանց միջև և հասկանալ ավելցուկի քանակը։
#y = int(input("Enter the number of people "" "))
#a = x//y
#b = x - a*y
#print(f"When we distribute {x} candies between {y} people equally, each person recieves {a} chocolates and remains {b}")

#a = int(input("Enter a number wih 3 digits")) #Մուտքագրել որևէ եռանիշ թիվ և առանձին տպել դրա թվերը։
#b = a//100
#c = (a-b*100)//10
#d = a %10
#print(b)
#print(c)
#print(d)


#a= int(input("Enter a number:"))#Մուտքագրել որևէ եռանիշ թիվ և որոշել,թե այն դրական է թե բացասական։
#if a > 0:
#    print(f"{a} is a positive number")
#elif a < 0:
#    print(f"{a} is a negative number")
#else:
#    print(f"{a} is equal to zero")    

#a = int(input("Enter a number:"))#Մուտքագրել որևէ թիվ և համեմատել այն 9 ի հետ։
#if a > 9:
#    print(f"{a} is greather than 9")
#elif a < 9    :
#    print(f"{a} is smaller than 9")
#else:
#    print(f"{a} is equal to 9") 

#a  = int(input("Enter a number:"))
#if a % 3 == 0:
#    print(f"{a} is divisible by 3")
#else:
#   print(f"{a} is not divisible by 3")    

#a = int(input("Enter the first number:"))#Մուտքագրել 2 թիվ և հասկանալե,թե արդյոք առաջին թիվը անմնացորդ բաժանվում է երկրորդի վրա։
#b = int(input("Enter the second number:"))
#if a%b == 0:
#    print(f"{a} is divisible by {b}")
#else:
#    print(f"{a} is not divisible by {b}")    

#a = int(input("Enter a number:"))#Մուտքագրել թիվ և հասկանալ արդյոք այն ավարտվում է 8-ով, թե՝ ոչ։
#if str(a).endswith("8"):
#    print(f"The number {a} ends with 8 ")
#else:
#     print(f"The number {a} does not end with 8 ")    

#a = int(input("Enter a number:"))#Մուտքագրել թիվ, ստուգել արդյոք այն 10-ից մեծ կենտ թիվ է։
#if a >= 10 and a%2  == 1:
#    print(f"{a} is greather than 10 and odd")
#else:
#    print(f"{a} does not satisfy the requirements") 

#a = int(input("Enter a number:"))#Մուտքագրել թիվ և հասկանալ արդյոք այն բաժանվում է 4-ի և 6-ի։
#if a % 4 == 0 and a% 6 == 0:
#    print(f"{a} is divisible by 4 and 6")
#else:
#    print(f"{a} does not meet the requirements")   

#a = int(input("Enter the measure of the angle:"))#Մուտքագրել անկյան աստիճանային չափը և որոշել նրա տեսակը։
#if a > 90:
#    print("The angle is abtuse.")
#elif a < 90:
#    print("The angle is acute.")
#else:
#    print("The angle is right angle.")    

#a = int(input("Enter a number:"))#Մուտքագրել 4 թիվ և հասկանալ արդյոք դրանցից որևէ մեկը 0 է, թե՝ ոչ։
#b = int(input("Enter another number:"))
#c = int(input("Enter another number:"))
#d = int(input("Enter one more number"))

#if a == 0 or b == 0 or c == 0 or d == 0:
#    print("There is a 0 among these numbers")
#else:
#    print("None of these numbers is zero")    

#a = input("Enter some text: "" ")#Մուտքագրել տեքստ և հասկանալ արդյոք դրա երկարությունը 10-ից 24-ի միջակայքում է, թե՝ ոչ։
#if 10 <= len(a)  <=24:
#    print("The length of the text is in the range of 10 and 24.")
#else:
#    print("The length of the text exceeds the limit. ")

#a = input("Enter some text: "" ")#Մուտքագրել 2 տողեր և հասկանալ արդյոք դրանք նույնն են, թե՝ոչ։
#b = input("Enter some text: "" ")
#if a == b:
#    print(f"{a} and {b} are identical.")
#else:
#    print(f"{a} and {b} are not identical.")

#a = input("Enter some text: "" ")#Մուտքագրել տեքստ և հասկանալ,թե արդյոք դա նույնն է ինչ դրա գակառակ վերսիան,թե ՝ոչ։
#if a == a[::-1]:
#    print(f"{a} is identical with its reversed version.")
#else:
#    print(f"{a} is not the same as its reversed version.")    

#a = input("Enter some text: "" ")#Մուտքագրել երկու տող և համեմատել դրանց երկարությունները։
#b = input("Enter some text: "" ")

#if len(a)  == len(b):
#    print(f"The length of {a} is equal to the length of {b}.")
#elif len(a) < len(b)    :
#    print(f"The length of {a} is less than the length of {b}.")
#else:
#    print(f"The length of {a} is more than the length of {b}.")

#a = input("Enter some text: "" ")#Մուտքագրել տող և հասկանալ արդյոք այն սկսվում է A տառով, թե՝ոչ։
#if a.startswith("A") or a.startswith("a"):
#    print("The text you\'ve entered starts with the letter \"A\" or \"a\" "" ")
#else:
#    print("The text you\'ve entered does not start with the letter \"A\" or \"a\" "" ")    

#a = int(input("Enter an integer number:"))#Մուտքագրել թիվ և հասկանալ, թե այն պատկանում է 5։10 կամ 15;30 միջակայքին, թե ՝ոչ։
#if 5 <= a <= 10 or 15 <= a <= 30:
#    print(f"{a} belongs to the range of either [5;10] or [15;30].")
#else:
#    print(f"{a} does not belong to the ranges.")    

#a = int(input("Enter the length:"" "))#Մուտքագրել ուղղանկյունանիստի 3 չափերը և որոշել թե արդյոք լրիվ մակերևույթի մակերեսը փոքր է 500-ից,թե ՝ոչ։
#b = int(input("Enter the width: "" "))
#c = int(input("Enter the height: "" "))
#s = 2*a*b+2*a*c+2*b*c
#if s <= 500:
#    print(f"{s} meets the requirement")
#else:
#    print(f"{s} does not meet the requirement")    

#a = int(input("Enter the length first side of the triangle"))#Մուտքագրել եռանկյան 3 չափումներն ու պարզել,թե արֆժդյք գոյություն ւոնի նման չափերով եռանկյուն,թե՝ոչ։
#b = int(input("Enter the length second side of the triangle"))
#c = int(input("Enter the length third side of the triangle"))

#if a + b > c or a+c > b or b+c > a:
#    print("The triangle can\'t be formed.")
#else:
#    print("The triangle can be succesfully formed.")    

#a = int(input("Enter the first number:"))#Մուտքագրել 4 թիվ և պարզել թե արդյոք հնարավոր է դրանցով կազմել թվաբանական պրոգրեսիա,թե ՝ոչ։
#b = int(input("Enter the second number:"))
#c = int(input("Enter the third number:"))
#d = int(input("Enter the fourth number:"))

#if a-b == b-c and a-b == d-c:
#    print("The progression is valid.")
#else:
#    print("The progression is invalid") 



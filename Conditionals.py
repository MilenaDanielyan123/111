a = input("Enter some text:")#Տրված է տող։ Որոշել՝ առաջին և վերջին սիմվոլները նույնն են, թե ոչ։
if a[0] == a[-1]:
    print("Yes,the first and last symbols are the same.")
else:
    print("No")    

a = input("Enter some text:")#Տրված է տող։ Տպել առաջին և վերջին սիմվոլները։
print(a[0],a[-1])

a = input("Enter some text:")#Տրված է տող։ Տպել առաջին երեք սիմվոլները։ Եթե տողի երկարությունը փոքր է 3-ից, տպել ամբողջ տողը։
print(a[0:3])

a = input("Paste the link:")#Տրված է տող։ Եթե այն սկսվում է "https://" -ով, տպել Secure, հակառակ դեպքում՝ Not Secure։
if a.startswith("https://"):
    print("The link is secure.")
else:
    print("The link is not secure.")

a = input("Paste the link:")#Տրված է URL։ Որոշել՝ այն սկսվում է "http://" -ով, թե "https://" -ով։
if a.startswith("https://"):
    print("The URL starts with https://")
elif a.startswith("http://"):
    print("The Url starts with http://")
else:
    print("The URL is not secure")    


a = input("Enter the name of the file:")#Տրված է ֆայլի անուն։ Որոշել՝ այն ավարտվում է .py ընդլայնմամբ։
if a.endswith(".py"):
    print("The file\'s name ends with .py")
else:
    print("The file\'s name does not end with .py")   

a = input("Enter the name of the file:")#Տրված է ֆայլի անուն։ Եթե այն ավարտվում է .txt-ով, փոխարինել այն .csv-ով։
b = a.replace(".txt",".csv")
print(b)

a = input("Enter the name of the file:")#Տրված է տող։ Փոխարինել բոլոր բացատները "_" նշանով։
b =a.replace("_"," ")
print(b)

a = input("Enter some text:")#Տրված է տող։ Փոխարինել բոլոր "." սիմվոլները ","-ով։
print(a.replace(".",","))

a = input("Enter some text:")#Տրված է տող։ Հեռացնել սկզբի և վերջի բոլոր բացատները։
print(a.strip())

a = input("Enter some text:")#Տրված է տող։ Հեռացնել ձախ կողմի բոլոր բացատները։
print(a.lstrip())

a = input("Enter some text:")#Տրված է տող։ Հեռացնել միայն աջ կողմի բացատները։
print(a.rstrip())

a = input("Enter some text:")#Տրված է տող։ Հաշվել, թե քանի անգամ է հանդիպում "Python" բառը։
print(a.count("Python"))

a = input("Enter some text:")#Տրված է տող։ Հաշվել, թե քանի անգամ է հանդիպում "a" տառը։
print(a.count("a"))

a = input("Enter some text:")#Տրված է տող։ Եթե այն պարունակում է "error" բառը, տպել YES, հակառակ դեպքում՝ NO։
if ("error") in a:
    print("Yes")
else:    
    print("No")

a = input("Enter some text:")#. Տրված է տող։ Եթե այն պարունակում է "admin" բառը, փոխարինել այն "user"-ով։
print(a.replace("admin","user"))

a = input("Enter some text:")# Տրված է տող։ Գտնել առաջին բացատի դիրքը։ Եթե բացատ չկա, տպել -1։
print(a.find(" "))

a = input("Enter some text:")#Տրված է տող։ Գտնել առաջին ":" սիմվոլի դիրքը։
print(a.find(":"))

a = input("Enter some text:")#Տրված է տող։ Գտնել վերջին "․" սիմվոլի դիրքը։
print(a.rfind("."))

a = input("Enter some email:")#Տրված է էլեկտրոնային հասցե։ Տպել @ նշանից առաջ գտնվող մասը։
print(a.split("@")[0])

a = (input("Enter the email:"))#Տրված է էլեկտրոնային հասցե։ Տպել @ նշանից հետո գտնվող մասը։
print(a.split("@")[-1])

a = input("Past the URL:")#Տրված է URL։ Տպել միայն դոմեյնի անունը։
print(a.split("https://")[0])

b = input("Enter the phone number:")# Տրված է հեռախոսահամար +374-XX-XX-XX-XX ձևաչափով։ Հեռացնել + և - նշանները։
print(b.replace("+","").replace("-",""))

a = input("Enter the phone number:")#Տրված է հեռախոսահամար։ Եթե այն սկսվում է 374-ով, տպել Armenia։
if a.startswith("+374"):
    print("Armenia")
else:
    print("Not Armenia")  

a = input("Enter your name and surname:") #Տրված է անուն և ազգանուն փոքրատառերով։ Տպել այնպես, որ յուրաքանչյուր բառ սկսվի մեծատառով։
print(a.title())

a = input("Enter some text:")#Տրված է նախադասություն։ Առաջին տառը դարձնել մեծատառ։
print(a.capitalize())

a = input("Enter some text:")#Տրված է տող։ Եթե այն ամբողջությամբ մեծատառ է, տպել OK, հակառակ դեպքում՝ այն դարձնել մեծատառ։
b = a.upper()
if a == b:
    print("OK")
else:
    print("Invalid")    

a = input("Enter some text:")
if a.isupper():
    print("Ok")
else:
    print(a.upper())   

a = input("Enter some text:")#. Տրված է տող։ Եթե այն ամբողջությամբ փոքրատառ է, տպել OK, հակառակ դեպքում՝ այն դարձնել փոքրատառ։
if a.islower():
    print("OK")
else:
    print(a.lower())   

a = input("Enter some text or digits:")# Տրված է տող։ Եթե այն բաղկացած է միայն թվանշաններից, տպել այդ թիվը կրկնապատկված, հակառակ դեպքում՝ ERROR։
if a.isdigit():
    b = int(a)
    print(b*2)
else:
    print("ERROR")    

a  = input("Enter some text or digits:")# Տրված է տող։ Եթե այն բաղկացած է միայն տառերից, տպել Letters Only, հակառակ դեպքում՝ Invalid։
if a.isalpha():
    print("Letters only")
else:
    print("Invalid")    

a = input("Enter somet text:")# Տրված է տող։ Եթե այն բաղկացած է միայն բացատներից, տպել Empty, հակառակ դեպքում՝ Not Empty։
if a.isspace():
    print("Empty")
else:
    print("Not empty")    

a = input("Enter some text:")#Տրված է տող։ Որոշել՝ այն պարունակում է գոնե մեկ բացատ։
if " " in a:
    print("There is a space in the text")
else:
    print("There is no space in the text")    

a = input("Enter a string:")#Տրված է տող։ Եթե նրա երկարությունը զույգ է, տպել Even, հակառակ դեպքում՝ Odd։

if len(a) % 2 ==0:
    print("Even")
else:
    print("Odd")    

a = input("Enter some text:")#3Տրված է տող։ Եթե նրա երկարությունը մեծ է 10-ից, տպել միայն առաջին 10 սիմվոլը։
print(a[:10])

a = input("Enter some text:")#Տրված է տող։ Եթե նրա երկարությունը փոքր է 5-ից, վերջում ավելացնել այնքան *, մինչև երկարությունը դառնա 5։
while len(a) < 5:
    a += "*"
print(a)

a = input("Enter the password:")#Տրված է գաղտնաբառ։ Որոշել՝ այն ունի՞ առնվազն 8 սիմվոլ, պարունակում է՞ գոնե մեկ մեծատառ և գոնե մեկ թվանշան։
hasu = False
hasd = False
for i in a:
    if i.isupper:
        hasu = True
    if i.isdigit:
        hasd = True
if len(a) >= 8 and hasu == True and hasd == True:
    print("Passed")                
else:
    print("Invalid password")    

a = input("Enter a string:")#Տրված է տող։ Եթե այն միաժամանակ սկսվում է մեծատառով և ավարտվում է "." սիմվոլով, տպել Correct, հակառակ դեպքում՝ Incorrect։
b = a[0]
if a.endswith(".") and b.isupper:
    print("Valid")
else:
    print("Invalid")    


name = input("Enter the text")

if name == "Alice":
    print("Hey there!")
    salary = int(input())
    if salary < 10000:
        print("Sounds good")
    else:
        print("Let's discuss this a little")
   
else:
    print("I don't know you")

x = int(input())
if 90 <= x <= 100:
    print("A")
elif 80 <= x <= 89:
    print("B")
elif 70<= x <= 79:
    print("C")
elif 60 <= x <= 69:
    print("D")
else:
    print("F")


a = int(input("Please enter the value of a " ""))
b = int(input("Please enter the sign of b " ""))
c = int(input("Please enter the value of c " ""))

if (b <= a <= c) or (c <= a <= b):
    print("The median is", a)
elif (a <= b <= c) or (c <= b <= a):
    print("The median is ",b)
else:
    print("The median is", c)
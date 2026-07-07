#a = input("Enter some text:")#Տրված է տող։ Որոշել՝ առաջին և վերջին սիմվոլները նույնն են, թե ոչ։
#if a[0] == a[-1]:
#    print("Yes,the first and last symbols are the same.")
#else:
#    print("No")    

#a = input("Enter some text:")#Տրված է տող։ Տպել առաջին և վերջին սիմվոլները։
#print(a[0],a[-1])

#a = input("Enter some text:")#Տրված է տող։ Տպել առաջին երեք սիմվոլները։ Եթե տողի երկարությունը փոքր է 3-ից, տպել ամբողջ տողը։
#print(a[0:3])

#a = input("Paste the link:")#Տրված է տող։ Եթե այն սկսվում է "https://" -ով, տպել Secure, հակառակ դեպքում՝ Not Secure։
#if a.startswith("https://"):
#    print("The link is secure.")
#else:
#    print("The link is not secure.")

#a = input("Paste the link:")#Տրված է URL։ Որոշել՝ այն սկսվում է "http://" -ով, թե "https://" -ով։
#if a.startswith("https://"):
#    print("The URL starts with https://")
#elif a.startswith("http://"):
#    print("The Url starts with http://")
#else:
#    print("The URL is not secure")    


#a = input("Enter the name of the file:")#Տրված է ֆայլի անուն։ Որոշել՝ այն ավարտվում է .py ընդլայնմամբ։
#if a.endswith(".py"):
#    print("The file\'s name ends with .py")
#else:
#    priont("The file\'s name does not end with .py")   

#a = input("Enter the name of the file:")#Տրված է ֆայլի անուն։ Եթե այն ավարտվում է .txt-ով, փոխարինել այն .csv-ով։
#b = a.replace(".txt",".csv")
#print(b)

#a = input("Enter the name of the file:")#Տրված է տող։ Փոխարինել բոլոր բացատները "_" նշանով։
#b =a.replace("_"," ")
#print(b)

#a = input("Enter some text:")#Տրված է տող։ Փոխարինել բոլոր "." սիմվոլները ","-ով։
#print(a.replace(".",","))

#a = input("Enter some text:")#Տրված է տող։ Հեռացնել սկզբի և վերջի բոլոր բացատները։
#print(a.strip())

#a = input("Enter some text:")#Տրված է տող։ Հեռացնել ձախ կողմի բոլոր բացատները։
#print(a.lstrip())

#a = input("Enter some text:")#Տրված է տող։ Հեռացնել միայն աջ կողմի բացատները։
#print(a.rstrip())

#a = input("Enter some text:")#Տրված է տող։ Հաշվել, թե քանի անգամ է հանդիպում "Python" բառը։
#print(a.count("Python"))

#a = input("Enter some text:")#Տրված է տող։ Հաշվել, թե քանի անգամ է հանդիպում "a" տառը։
#print(a.count("a"))

#a = input("Enter some text:")#Տրված է տող։ Եթե այն պարունակում է "error" բառը, տպել YES, հակառակ դեպքում՝ NO։
#if ("error") in a:
#    print("Yes")
#else:    
#    print("No")

#a = input("Enter some text:")#. Տրված է տող։ Եթե այն պարունակում է "admin" բառը, փոխարինել այն "user"-ով։
#print(a.replace("admin","user"))

#a = input("Enter some text:")# Տրված է տող։ Գտնել առաջին բացատի դիրքը։ Եթե բացատ չկա, տպել -1։
#print(a.find(" "))

#a = input("Enter some text:")#Տրված է տող։ Գտնել առաջին ":" սիմվոլի դիրքը։
#print(a.find(":"))

#a = input("Enter some text:")#Տրված է տող։ Գտնել վերջին "․" սիմվոլի դիրքը։
#print(a.rfind("."))

#a = input("Enter some email:")#Տրված է էլեկտրոնային հասցե։ Տպել @ նշանից առաջ գտնվող մասը։
#print(a.split("@")[0])

#a = (input("Enter the email:"))#Տրված է էլեկտրոնային հասցե։ Տպել @ նշանից հետո գտնվող մասը։
#print(a.split("@")[-1])

#a = input("Past the URL:")#Տրված է URL։ Տպել միայն դոմեյնի անունը։
#print(a.split("https://")[0])

#b = input("Enter the phone number:")# Տրված է հեռախոսահամար +374-XX-XX-XX-XX ձևաչափով։ Հեռացնել + և - նշանները։
#print(b.replace("+","").replace("-",""))

#a = input("Enter the phone number:")#Տրված է հեռախոսահամար։ Եթե այն սկսվում է 374-ով, տպել Armenia։
#if a.startswith("+374"):
#    print("Armenia")
#else:
#    print("Not Armenia")  

#a = input("Enter your name and surname:") #Տրված է անուն և ազգանուն փոքրատառերով։ Տպել այնպես, որ յուրաքանչյուր բառ սկսվի մեծատառով։
#print(a.title())

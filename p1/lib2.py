import datetime
books=[]
subs={}
def f1():
    n=input("Enter book name:")
    print("Subjects:")
    if not subs:print("None")
    k=list(subs.keys())
    i=1
    for s in k:
        print(str(i)+". "+s)
        i+=1
    print(str(i)+". New subject")
    c2=int(input("Choice:"))
    if c2==i:
        sub=input("Enter new subject:")
        if sub not in subs:subs[sub]=0
    else:
        sub=k[c2-1]
    subs[sub]+=1
    bnm=sub[:3].upper()+str(subs[sub]).zfill(3)
    books.append({"n":n,"sub":sub,"bnm":bnm,"st":"a","sn":"","rn":"","di":"","rd":""})
    print("Added. Book number is "+bnm)
def f2():
    bnm=input("Enter book number:")
    for b in books:
        if b["bnm"]==bnm and b["st"]=="a":
            b["st"]="i"
            b["sn"]=input("Student name:")
            b["rn"]=input("Registration number:")
            b["di"]=datetime.date.today()
            b["rd"]=b["di"]+datetime.timedelta(days=14)
            print("Issued. Due date: "+str(b["rd"]))
            break
    else:
        print("Unavailable")
def f3():
    bnm=input("Enter book number:")
    for b in books:
        if b["bnm"]==bnm and b["st"]=="i":
            b["st"]="a"
            b["sn"]=""
            b["rn"]=""
            b["di"]=""
            b["rd"]=""
            print("Returned")
            break
    else:
        print("Invalid")
def f4():
    f=0
    for b in books:
        if b["st"]=="a":
            print(b["bnm"]+"-"+b["n"])
            f=1
    if f==0:print("No available books")
def f5():
    f=0
    for b in books:
        if b["st"]=="i":
            print(b["bnm"]+"-"+b["n"]+" to "+b["sn"])
            f=1
    if f==0:print("No issued books")
def f6():
    t=datetime.date.today()
    f=0
    for b in books:
        if b["st"]=="i" and b["rd"]==t:
            print(b["bnm"]+"-"+b["n"])
            f=1
    if f==0:print("No books due today")
def admin():
    while True:
        print("Enter 1 to add a new book")
        print("Enter 2 to issue a book")
        print("Enter 3 to return a book")
        print("Enter 4 to display all available book")
        print("Enter 5 to display all issued book")
        print("Enter 6 to display all books to be returned by today")
        print("Enter 7 to logout")
        c=input("Enter your choice:")
        match c:
            case "1":f1()
            case "2":f2()
            case "3":f3()
            case "4":f4()
            case "5":f5()
            case "6":f6()
            case "7":break
            case _:print("Invalid")
U="admin"
P="library123"
while True:
    print("Enter 1 to login")
    print("Enter 2 to exit")
    c=input("Enter choice:")
    match c:
        case "1":
            u=input("Enter username:")
            p=input("Enter password:")
            if u==U and p==P:
                print("Logged in")
                admin()
            else:
                print("Enter correct username and password")
        case "2":break
        case _:
            print("Invalid input")
            print("Enter correct choice")
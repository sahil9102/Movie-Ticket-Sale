import math
print(" _       _            _                                       ")
print("( )     ( )          ( )                                      ")
print("| |     | |          | |                                      ")
print("| |     | | ________ | | _______    ___    ________  ________ ")
print("| |     | ||  ____  || ||  _____)  / _ \  /  _  _  \|  ____  |")
print("| |  _  | || |  /___|| || |       / / \ \ | | \/ | || |  /___|")
print("| |_/ \_| || |______ | || |_____ ( (___) )| |    | || |______ ")
print("|_________|\________)(_)\_______) \_____/ (_)    (_)\________)")
print("       ----------------------- -----------------------")
print("                  |||          |||                 |||")
print("                  |||          |||                 |||")
print("                  ---          -----------------------")
print("   ______                                        _________ ")
print("  |  ___ \                                      |  _______)")
print("  | |   \ \ ~_^Book your Movie Ticket ONLINE^_~ | |        ")
print("  | |___/ /     _____  ______  _________  _____ | |_______ ")
print("  |  ___ (     / __  )|  ____)(___   ___)/ __  )|_______  |")
print("  | |   \ \   / /  | || |____     | |   / /  | |        | |")
print("  | |    \ \ / /   | ||____  |    | |  / /   | |        | |")
print("  | |____/ /( (____| | ____| |    | | ( (____| | _______| |")
print("  |_______/  \____,__)(______|    (_)  \____,__)(_________|")
A1="ABCDEFGHIJKLMNO"
AM=162
BO=0
b=0
number=0
tm=0
lt=""
no=0
dic={"A":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        A",
     "B":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        B",
     "C":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        C",
     "D":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        D",
     "E":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        E",
     "F":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        F",
     "G":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        G",
     "H":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        H",
     "I":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        I",
     "J":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        J",
     "K":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        K",
     "L":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        L",
     "M":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        M",
     "N":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        N",
     "O":"   [1] [2] [3] [4] [5]                    [6] [7] [8] [9] [10]         -        O",
     "P":"[1] [2] [3] [4] [5] [6]                 [7] [8] [9] [10] [11] [12]     -        P"}
bollywood=["thugs of hindustan","andhadhun","bazaar","badhai ho","bhaiaji superhit"]
hollywood=["ralph breaks the interent","the girl in the spider's web","fantastic beasts:the crimes of grinderwald","robin hood","green book"]
timings=["9:00-12:00","15:00-18:00","18:00-21:00","21:00-24:00"]
while 1!=0:
    print("Movies that are available are: ")
    print("   In Bollywood")
    print("         Thugs of Hindustan, Andhadhun, Bazaar, Badhai Ho, Bhaiaji Superhit")
    print("   In Hollywood")
    print("         Ralph Breaks the Interent, The Girl in the Spider's Web, Fantastic Beasts:The Crimes of Grinderwald, Robin Hood, Green Book")
    m=input("Enter the movie which you are searching for: ")
    s=""
    for mov in m:
        if mov.isupper():
            mov=mov.lower()
        s=s+mov
    for sob in bollywood:
        if s==sob:
            number=number+1
            print("Timings are 9:00-12:00, 15:00-18:00, 18:00-21:00, 21:00-24:00")
            while 1!=0:
                time=input("Enter the timing: ")
                for ti in timings:
                    if time==ti:
                        tm=tm+1
                        break
                if tm==1:
                    break
                else:
                    print("Your entered timings are wrong")
                    continue
    for soh in hollywood:
        if s==soh:
            number=number+1
            print("Timings are 9:00-12:00, 15:00-18:00, 18:00-21:00, 21:00-24:00")
            while 1!=0:
                time=input("Enter the timing: ")
                for ti in timings:
                    if time==ti:
                        tm=tm+1
                        break
                if tm==1:
                    break
                else:
                    print("Your entered timings are wrong")
                    continue
    if number==1:
        break
    elif number==0:
        print("Movie you are wondering to watch is not available")
        print("Movies that are available are: ")
        print("   In Bollywood")
        print("Thugs of Hindustan, Andhadhun, Bazaar, Badhai Ho, Bhaiaji Superhit")
        print("   In Hollywood")
        print("Ralph Breaks the Interent, The Girl in the Spider's Web, Fantastic Beasts:The Crimes of Grinderwald, Robin Hood, Green Book")
        continue
print((" "*29)+"screen")
print(" "+"_"*63)
print("/"+(" "*63)+"\ ")
print("                          SILVER(100/-)")
print(dic["A"])
print(dic["B"])
print(dic["C"])
print(dic["D"])
print("                           GOLD(118/-)")
print(dic["E"])
print(dic["F"])
print(dic["G"])
print(dic["H"])
print("                         PLATINUM(152/-)")
print(dic["I"])
print(dic["J"])
print(dic["K"])
print(dic["L"])
print(dic["M"])
print(dic["N"])
print(dic["O"])
print("                          PRIME(230/-)")
print(dic["P"])
while 1!=0:
    people=input("Enter the number of people: ")
    if people.isdigit() and int(people)!=0:
        if int(people)>10:
            print("You can only book for 10 persons")
            continue
        else:
            people=int(people)
            break
    else:
        print("Wrong input")
AM=AM-people
pel=1
while people!=0:
    print("For",pel,"person")
    seat=input("Enter the seat number(like A1,B5,J2): ")
    LENGHT=len(seat)
    lt=lt+seat
    string=len(lt)
    start=count=0
    end=string
    while 1!=0:
         pos=lt.find(seat,start,end)
         if pos!=-1:
              count=count+1
              start=pos+LENGHT
         else:
             break
         if start>=string:
              break
    if count>1:
        print("This seat not available")
        lt=lt[0:(len(lt)-len(seat))]
        continue
    else:
        if LENGHT==2:
            if seat[1]=="1" or seat[1]=="2" or seat[1]=="3" or seat[1]=="4" or seat[1]=="5" or seat[1]=="6" or seat[1]=="7" or seat[1]=="8" or seat[1]=="9" or (seat[1]=="1" and seat[2]=="0"):
                if seat[0]=="A" or seat[0]=="B" or seat[0]=="C" or seat[0]=="D":
                    pel=pel+1
                    b=b+100
                    people=people-1
                elif seat[0]=="E" or seat[0]=="F" or seat[0]=="G" or seat[0]=="H":
                    pel=pel+1
                    b=b+118
                    people=people-1
                elif seat[0]=="I" or seat[0]=="J" or seat[0]=="K" or seat[0]=="L" or seat[0]=="M" or seat[0]=="N" or seat[0]=="O":
                    pel=pel+1
                    b=b+152
                    people=people-1
                elif seat[0]=="P":
                    pel=pel+1
                    b=b+230
                    people=people-1
                else:
                    print("This seat not available")
                    lt=lt[0:(len(lt)-len(seat))]
                    continue
            else:
                print("This seat not available")
                lt=lt[0:(len(lt)-len(seat))]
                continue
        elif LENGHT==3:
            if (seat[0]=="A" or seat[0]=="B" or seat[0]=="C" or seat[0]=="D") and (seat[1]=="1" and seat[2]=="0"):
                pel=pel+1
                b=b+100
                people=people-1
            elif (seat[0]=="E" or seat[0]=="F" or seat[0]=="G" or seat[0]=="H") and (seat[1]=="1" and seat[2]=="0"):
                pel=pel+1
                b=b+118
                people=people-1
            elif (seat[0]=="I" or seat[0]=="J" or seat[0]=="K" or seat[0]=="L" or seat[0]=="M" or seat[0]=="N" or seat[0]=="O" or seat[0]=="i" or seat[0]=="j" or seat[0]=="k" or seat[0]=="l" or seat[0]=="m" or seat[0]=="n" or seat[0]=="o") and (seat[1]=="1" and seat[2]=="0"):
                pel=pel+1
                b=b+152
                people=people-1
            elif (seat[0]=="P" or seat[0]=="p") and ((seat[1]=="1" and seat[2]=="0") or (seat[1]=="1" and seat[2]=="1") or (seat[1]=="1" and seat[2]=="2")):
                pel=pel+1
                b=b+230
                people=people-1
            else:
                print("This seat not available")
                lt=lt[0:(len(lt)-len(seat))]
                continue
        else:
            print("This seat not available")
            lt=lt[0:(len(lt)-len(seat))]
            continue
        if LENGHT==2:
            if seat[0]=="P":
                if seat[1]=="1":
                    (dic["P"])=(dic["P"])[0:1]+"-"+(dic["P"])[2:]
                elif seat[1]=="2":
                    (dic["P"])=(dic["P"])[0:5]+"-"+(dic["P"])[6:]
                elif seat[1]=="3":
                    (dic["P"])=(dic["P"])[0:9]+"-"+(dic["P"])[10:]
                elif seat[1]=="4":
                    (dic["P"])=(dic["P"])[0:13]+"-"+(dic["P"])[14:]
                elif seat[1]=="5":
                    (dic["P"])=(dic["P"])[0:17]+"-"+(dic["P"])[18:]
                elif seat[1]=="6":
                    (dic["P"])=(dic["P"])[0:21]+"-"+(dic["P"])[22:]
                elif seat[1]=="7":
                    (dic["P"])=(dic["P"])[0:41]+"-"+(dic["P"])[42:]
                elif seat[1]=="8":
                    (dic["P"])=(dic["P"])[0:45]+"-"+(dic["P"])[46:]
                elif seat[1]=="9":
                    (dic["P"])=(dic["P"])[0:49]+"-"+(dic["P"])[50:]
            else:
                for ai in A1:
                    if seat[0]==ai:
                        if seat[1]=="1":
                            dic[ai]=dic[ai][0:4]+"-"+dic[ai][5:]
                        elif seat[1]=="2":
                            dic[ai]=dic[ai][0:8]+"-"+dic[ai][9:]
                        elif seat[1]=="3":
                            dic[ai]=dic[ai][0:12]+"-"+dic[ai][13:]
                        elif seat[1]=="4":
                            dic[ai]=dic[ai][0:16]+"-"+dic[ai][17:]
                        elif seat[1]=="5":
                            dic[ai]=dic[ai][0:20]+"-"+dic[ai][21:]
                        elif seat[1]=="6":
                            dic[ai]=dic[ai][0:43]+"-"+dic[ai][44:]
                        elif seat[1]=="7":
                            dic[ai]=dic[ai][0:47]+"-"+dic[ai][48:]
                        elif seat[1]=="8":
                            dic[ai]=dic[ai][0:51]+"-"+dic[ai][52:]
                        elif seat[1]=="9":
                            dic[ai]=dic[ai][0:55]+"-"+dic[ai][56:]
        if LENGHT==3:
            if seat[0]=="P":
                if seat[1]=="1" and seat[2]=="0":
                    dic["P"]=dic["P"][0:53]+"--"+dic["P"][55:]
                elif seat[1]=="1" and seat[2]=="1":
                    dic["P"]=dic["P"][0:58]+"--"+dic["P"][60:]
                elif seat[1]=="1" and seat[2]=="2":
                    dic["P"]=dic["P"][0:63]+"--"+dic["P"][65:]
            else:
                if seat[1]=="1" and seat[2]=="0":
                    for ai in A1:
                        if seat[0]==ai:
                            dic[ai]=dic[ai][0:59]+"--"+dic[ai][61:]
print("Seats you have entered are: ")
print((" "*29)+"screen")
print(" "+"_"*63)
print("/"+(" "*63)+"\ ")
print("                          SILVER(100/-)")
print(dic["A"])
print(dic["B"])
print(dic["C"])
print(dic["D"])
print("                           GOLD(118/-)")
print(dic["E"])
print(dic["F"])
print(dic["G"])
print(dic["H"])
print("                         PLATINUM(152/-)")
print(dic["I"])
print(dic["J"])
print(dic["K"])
print(dic["L"])
print(dic["M"])
print(dic["N"])
print(dic["O"])
print("                          PRIME(230/-)")
print(dic["P"])
print()
print((" "*44)+"[-] - is the seat that you have booked")
d=["k3234c","d4112y","s5644t","v1232r","q4532m","x6446j","z6216p","w7812d","a8915s","r1521p","x4644g"]
e=["dis233o","dfa423g","asd477u","cvb567i","qws314h","xgh267c","apr193g","vgy198d","vxz787v"]
f=["ADB5","CIS9","DFB2","SDF0","GBB6","SFG8","VEW5","XDP3","HJK7","CVN1"]
while 1!=0:
    discount=input("Enter the discount coupon code or 'n' if you don't have any: ")
    c=len(discount)
    if discount!="n":
        if c==6:
            for i in range(11):
                if discount==d[i]:
                    print("CONGRATULATIONS!!! You got a 12% discount")
                    BO=BO+1
                    dis=math.floor(b*(12/100))
                    b=b-dis 
                    break
            if BO==0:
                print("Your discount coupon code is invalid")
                continue
            else:
                break
        elif c==7:
            for i in range(9):
                if discount==e[i]:
                    print("CONGRATULATIONS!!! You got a 15% discount")
                    BO=BO+1
                    dis=math.floor(b*(15/100))
                    b=b-dis
                    break
            if BO==0:
                print("Your discount coupon code is invalid")
                continue
            else:
                break
        elif c==4:
            for i in range(10):
                if discount==f[i]:
                    print("CONGRATULATIONS!!! You got a 20% discount")
                    BO=BO+1
                    dis=math.floor(b*(20/100))
                    b=b-dis
                    break
            if BO==0:
                print("Your discount coupon code is invalid")
                continue
            else:
                break
        else:
            print("Your discount coupon code is invalid")
            continue
    else:
        break
print(b,"is your total amount.")
print(AM,"seats are left")
while 1!=0:
    confirm=input("Enter 'p' to proceed or 'c' for cancel your booking: ")
    if confirm=="p":
        pay=input("Enter the way you would like to do the payment(paypal or patym): ")
        py=""
        for pa in pay:
            if pa.isupper:
                pa=pa.lower()
            py=py+pa
        if py=="paytm" or py=="paypal":
            print("Send money to '123556789' ")
            print(" _____  _                    _         _     _             _ ")
            print("(_   _)( )                  ( ) _     ( )   ( )           ( )")
            print("  | |  | |___   ____  _____ | |/ )     \ \_/ /___   _   _ | |")
            print("  | |  |  _  \ / _  )/  _  \|   (       \   // _ \ ( ) ( )| |")
            print("  | |  | | | |( (_| || ( ) || |\ \       | |( (_) )| (_) || |")
            print("  (_)  (_) (_) \__,_)(_) (_)(_) (_)      (_) \___/  \___/ (_)")
            print("                  ^_~ Thanks for Using~_^                 (_)")
            break
        else:
            print("We do not support those online transactions ")
            print("We suport only paytm and paypal")
            continue
    elif confirm=="c":
        print(" _____  _                    _         _     _             _ ")
        print("(_   _)( )                  ( ) _     ( )   ( )           ( )")
        print("  | |  | |___   ____  _____ | |/ )     \ \_/ /___   _   _ | |")
        print("  | |  |  _  \ / _  )/  _  \|   (       \   // _ \ ( ) ( )| |")
        print("  | |  | | | |( (_| || ( ) || |\ \       | |( (_) )| (_) || |")
        print("  (_)  (_) (_) \__,_)(_) (_)(_) (_)      (_) \___/  \___/ (_)")
        print("                  ^_~ Thanks for Using~_^                 (_)")
        break
    else:
        print("Incorrect input")
        continue

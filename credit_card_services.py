import random
import time

print()
print()
print("\t\t\tFardeen's Credit Card Services")
print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("Hello and welcome to Fardeen's Credit Card Services. What would you like to proceed with?")
print()
print("~ Disclaimer: All references made to establishing contact with banks is only a simulation ~")

def card_generator():
    
    validity ='Invalid'
    print()
    print('''\t\tMENU

    Choose your desired card

    1. American Express
    2. Mastercard
    3. Visa''')
    print()

    ch=0
    while ch not in [1,2,3]:
        try:
            ch=int(input("Enter the number of your choice: "))
        except ValueError:
            print('Invalid Input')
            print()
            continue
        if ch not in [1,2,3]:
            print('Invalid Input')
            print()

    if ch==1:
        name='American Express'
    elif ch==2:
        name='Mastercard'
    elif ch==3:
        name='Visa'
        
    print()
    print('''\t\tMENU

    Choose country of residence

    1. Qatar
    2. USA
    3. India''')
    print()

    con=0
    while con not in [1,2,3]:
        try:
            con=int(input("Enter the number of your choice: "))
        except ValueError:
            print('Invalid Input')
            print()
            continue
        if con not in [1,2,3]:
            print('Invalid Input')
            print()

    if con==1:
        issuer='Qatar Central Bank (مصرف قطر المركزي)'
    elif con==2:
        issuer='The U.S. Federal Reserve'
    elif con==3:
        issuer='Reserve Bank of India (भारतीय रिज़र्व बैंक)'

    while validity=="Invalid":

        n=random.randint(1000000000000,9999999999999999)

        ns=str(n)[::-1]
        if len(ns)%2==0:
            l1=len(ns)+1
            l2=len(ns)
        else:
            l1=len(ns)
            l2=len(ns)+1

        s1=[]
        for i in range(1,l1,2):
            s1.append(str(int(ns[i])*2))

        s2=0
        str_s1=''.join(s1)
        for dig in str_s1:
            s2+=int(dig)

        s1_ii=[]
        for i in range(0,l2,2):
            s1_ii.append(str(int(ns[i])))

        s2_ii=0
        str_s1_ii=''.join(s1_ii)
        for dig in str_s1_ii:
            s2_ii+=int(dig)

        finalsum=s2+s2_ii
        if int(str(finalsum)[len(str(finalsum))-1])==0 and len(ns) in [13,15,16,19]:
            if ch==1:
                if str(n)[:2] in ['34','37'] and len(ns)==15:
                    validity="Valid"
            elif ch==2:
                if ((str(n)[:2] in ['51','52','53','54','55']) or (int(str(n)[:6]) in range(222100,272100))) and len(ns)==16:
                    validity="Valid"
            elif ch==3:
                if str(n)[0] == '4' and len(ns) in [13,16]:
                    validity="Valid"
        else:
            validity="Invalid"

    print()
    print("Checking if you are human....")
    time.sleep(1.7)
    print("Scanning for redundancy of credit card details....")
    time.sleep(2)
    print("Contacting ",issuer,"....")
    time.sleep(4)
    print("Approved")
    time.sleep(1.3)
    print("Generating new ",name," number....")
    time.sleep(2.5)
    print()
    print("Congratulations. Your new",name," number is ",n)
    print()
    time.sleep(1)

def validity_checker():
    n=int(input("Enter your credit card details: "))
    print("Checking if your credit card is valid....(and if it is, then say goodbye to all ur money)")
    print()
    time.sleep(3)

    ns=str(n)[::-1]
    if len(ns)%2==0:
        l1=len(ns)+1
        l2=len(ns)
    else:
        l1=len(ns)
        l2=len(ns)+1

    s1=[]
    for i in range(1,l1,2):
        s1.append(str(int(ns[i])*2))

    s2=0
    str_s1=''.join(s1)
    for dig in str_s1:
        s2+=int(dig)

    s1_ii=[]
    for i in range(0,l2,2):
        s1_ii.append(str(int(ns[i])))

    s2_ii=0
    str_s1_ii=''.join(s1_ii)
    for dig in str_s1_ii:
        s2_ii+=int(dig)

    finalsum=s2+s2_ii
    if int(str(finalsum)[len(str(finalsum))-1])==0 and len(ns) in [13,15,16,19]:
        if str(n)[:2] in ['34','37'] and len(ns)==15:
            print("Your American Express is Valid")
        elif ((str(n)[:2] in ['51','52','53','54','55']) or (int(str(n)[:6]) in range(222100,272100))) and len(ns)==16:
            print("Your Mastercard is Valid")
        elif str(n)[0] == '4' and len(ns) in [13,16]:
            print("Your Visa is Valid")
        else:
            print("Your credit card is Valid")
    else:
        print("Invalid")
    print()


def missing():
    print('''\nWelcome to the lost card services. If you forgot your credit card details or lost it but only remember a few digits, then this is the place for you.
This program will provide you a list of possible numbers your credit card could have.''')
    print()
    print('''\t\tRULES
    \t\t-----

    1. Only input '*' in the place of unknown numbers. Anything else would be invalid.
        Example: 400360000000****
                         40**600000000**4

    2. You can enter '*' upto 5 digits. But anything more than 4 unkown values could cause a very long runtime (upto 2min) or could crash the program.
    Continue with upto a max of 5 unkown digits AT YOUR OWN RISK.''')
    print()
    print()

    #Determine no. of '*'
    while True:
        ch=int(input('''Press '1' to input less than 5 unknown values
Press '2' to input 5 unkown values (BETA)
Choice: '''))
        if ch==2:
            while True:
                n=input("Enter partial card number and fill unknown numbers with '*': ")
                length=0
                for j in n:
                    if j=='*':
                        length+=1
                
                if length<=5 and length>0:
                    break
                elif length==0:
                    print()
                    print("Input atleast one unknown value")
                    print()
                else:
                    print()
                    print("Sorry. Input has more than 5 '*'")
                    print()
            break
                    
        elif ch==1:
            while True:
                n=input("Enter partial card number and fill unknown numbers with '*': ")
                length=0
                for j in n:
                    if j=='*':
                        length+=1
                if length<=4 and length>0:
                    break
                elif length==0:
                    print()
                    print("Input atleast one unknown value")
                    print()
                else:
                    print()
                    print("Sorry. Input has more than 4 '*'")
                    print()
            break
        else:
            print("Press only '1' or '2'")
             
    max_range=int('9'*length)
    final_count=0
    #Removing '*'

    l=list(n)
    cnt=[]
    for k in range(length):
        o=l.index('*')
        cnt.append(o)
        l[o]='/'

    lst=[]
    for i in range(0,(max_range+1)):
        if len(str(i)) <length:
            while len(str(i)) <length:
                i='0'+str(i)
        s=str(i)
        lsts=list(s)
        for o in lsts:
            lst.append(int(o))

        ltemp=[]                                        #Faheem starts here
        for a in l:
            if a.isdigit():
                ltemp.append(int(a))
            else:
                ltemp.append(a)
        tlist = []

        for i in range(len(ltemp)):

            if ltemp[i] != '/':
                tlist.append(str(ltemp[i]))
                
            elif ltemp[i] == '/':
                tlists = []
                for j in tlist:
                    tlists.append(str(j))
                t = ''.join(tlists)
                t = int(t)
                                                                #Thanks to Faheem! This Genius move was possible!
                new = (t*10) + lst[0]
                trash = lst[0]
                lst.remove(trash)
                tlist = list(str(new))

            else:
                print("Error")
        
        final=''.join(tlist)

        #Luhn's Algorithm

        ns=str(final)[::-1]
        if len(ns)%2==0:
            l1=len(ns)+1
            l2=len(ns)
        else:
            l1=len(ns)
            l2=len(ns)+1

        s1=[]
        for i in range(1,l1,2):
            s1.append(str(int(ns[i])*2))

        s2=0
        str_s1=''.join(s1)
        for dig in str_s1:
            s2+=int(dig)

        s1_ii=[]
        for i in range(0,l2,2):
            s1_ii.append(str(int(ns[i])))

        s2_ii=0
        str_s1_ii=''.join(s1_ii)
        for dig in str_s1_ii:
            s2_ii+=int(dig)

        finalsum=s2+s2_ii
        if int(str(finalsum)[len(str(finalsum))-1])==0 and len(ns) in [13,15,16,19]:
            card='valid'
        else:
            card="invalid"

        #Finall printing
        if card=="valid":
            print(final)
            final_count+=1
    print()
    print("Number of possible cards: ",final_count)
    
#Executing program (user interface)
while True:
    print()
    print("1. Press '1' to generate a new credit card")
    print("2. Press '2' to check the validity of your credit card number")
    print("3. Press '3' to check possible missing digits")
    print("4. Press '4' to exit")
    try:
        choice=int(input("Enter choice: "))
    except ValueError:
        print()
        print("Invalid input.")
        continue
    
    if choice==1:

        card_generator()

    elif choice==2: 

        validity_checker()

    elif choice==3:

        missing()
 
    elif choice==4:
        time.sleep(7)
        for i in '...fyi ur cvv is ':
            print(i,end='')
            time.sleep(0.3)
        time.sleep(1)
        print('*',end='')
        time.sleep(1)
        print('*',end='')
        time.sleep(1)
        print('*')
        time.sleep(1)
        break

    else:
        print()
        print("Invalid input.")

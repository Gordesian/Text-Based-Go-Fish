import random, os
gaming,pNum,playing,asked = True,0,True,""
pile,p1,p2,p3,p4,b1,b2,b3,b4,bT = [],[],[],[],[],0,0,0,0,0
def gameStart():
    global pNum,pile,p1,p2,p3,p4,b1,b2,b3,b4
    pile = [
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    p1,p2,p3,p4,b1,b2,b3,b4 = [],[],[],[],0,0,0,0
    errorS=True
    while errorS:
        try:
            print("How many opponents? (1-3)")
            pNum = int(input())
            if (pNum >= 1) and (pNum <= 3):
                errorS = False
                os.system('cls')
            else:
                os.system('cls')
                print("Input a number in range")
        except:
            os.system('cls')
            print("Input a number")
    for e in range(pNum+1):
        for i in range(8-pNum):
            card = random.randint(0,len(pile)-1)
            if e==0:
                p1.append(pile[card])
            elif e==1:
                p2.append(pile[card])
            elif e==2:
                p3.append(pile[card])
            elif e==3:
                p4.append(pile[card])
            pile.remove(pile[card])
def fish(cards):
    global pile,playing,asked,pNum
    if len(pile)!=0:
        if len(cards)==0:
            try:
                for i in range(8-pNum):
                    card = random.randint(0,len(pile)-1)
                    cards.append(pile[card])
                    pile.remove(pile[card])
            except:
                if len(cards)==0 and len(pile)==0:
                    playing = False
        else:
            card = random.randint(0,len(pile)-1)
            cards.append(pile[card])
            if pile[card]==asked:
                print("Go Again!")
            else:
                playing = False
            pile.remove(pile[card])
    else:
        playing = False
    return cards
def who(asker):
    global pNum,p1,p2,p3,p4
    p=[p1,p2,p3,p4]
    if asker==0:
        if pNum>1:
            errorW = True
            while errorW:
                try:
                    print("Who do you want to ask?")
                    asked = int(input())
                    if asked<=pNum and asked>0:
                        errorW = False
                        os.system('cls')
                    else:
                        os.system('cls')
                        print("Invalid Player")
                except:
                    os.system('cls')
                    print("Input Valid Response")
        else:
            asked=1
    else:
        asked=asker
        while asked==asker:
            asked = random.randint(0,pNum)
    return p[asked]
def ask(cards1,cards2):
    global asked,p1,p2,p3,p4
    if cards1==p1:
        errorA = True
        while errorA:
            try:
                print(cards1)
                print("What are you asking for?")
                a=input()
                asked=int(a)
                if asked>=2 and asked<=10 and asked in cards1:
                    if asked in cards2:
                        l=len(cards2)
                        for i in range(l):
                            if cards2[l-i-1]==asked:
                                cards1.append(asked)
                                cards2.remove(cards2[l-i-1])
                        os.system('cls')
                        print("Ask Again!")
                    else:
                        print("Go Fish!")
                        fish(cards1)
                    errorA = False
                else:
                    if len(cards1)==0:
                        print("Go Fish!")
                        fish(cards1)
                    else:
                        os.system('cls')
                        print("Ask for a card you have")
            except:
                asked=str(a).upper()
                if (asked=="J" or asked=="Q" or asked=="K" or asked=="A") and asked in cards1:
                    if asked in cards2:
                        l=len(cards2)
                        for i in range(l):
                            if cards2[l-i-1]==asked:
                                cards1.append(asked)
                                cards2.remove(cards2[l-i-1])
                        os.system('cls')
                        print("Ask Again!")
                    else:
                        print("Go Fish!")
                        fish(cards1)
                    errorA = False
                else:
                    if len(cards1)==0:
                        print("Go Fish!")
                        fish(cards1)
                    else:
                        os.system('cls')
                        print("Ask for a card you have")
    else:
        if len(cards1)==0:
            print("Go Fish!")
            fish(cards1)
        else:
            a = random.randint(0,len(cards1)-1)
            if cards2==p1:
                print("Player:",cards1[a],"?")
            elif cards2==p2:
                print("Bot 1:",cards1[a],"?")
            elif cards2==p3:
                print("Bot 2:",cards1[a],"?")
            elif cards2==p4:
                print("Bot 3:",cards1[a],"?")
            asked = cards1[a]
            if cards1[a] in cards2:
                l=len(cards2)
                for i in range(l):
                    if cards2[l-i-1]==cards1[a]:
                        cards1.append(cards1[a])
                        cards2.remove(cards2[l-i-1])
                print("Ask Again!")
            else:
                print("Go Fish!")
                fish(cards1)
def booker(cards,books):
    global bT,p1,p2,p3,p4
    l = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in cards:
        try:
            if i>=2 and i<=10:
                l[i-2] = l[i-2] + 1
        except:
            if i=="J":
                l[9]=l[9]+1
            elif i=="Q":
                l[10]=l[10]+1
            elif i=="K":
                l[11]=l[11]+1
            elif i=="A":
                l[12]=l[12]+1
    le=len(l)
    for i in range(le):
        if l[i]==4:
            bT=bT+1
            books=books+1
            if cards==p1:
                print("Player got a Book!")
            if cards==p2:
                print("Bot 1 got a Book!")
            if cards==p3:
                print("Bot 2 got a Book!")
            if cards==p4:
                print("Bot 3 got a Book!")
            card=0
            if i>=0 and i<=8:
                card = i+2
            elif i==9:
                card = "J"
            elif i==10:
                card = "Q"
            elif i==11:
                card = "K"
            elif i==12:
                card = "A"
            c=len(cards)
            for e in range(c):
                if cards[c-e-1]==card:
                    cards.remove(cards[c-e-1])
    return cards,books
while gaming:
    game = True
    gameStart()
    while game:
        os.system('cls')
        print("Bot 1:",len(p2),"cards",b2,"books")
        if pNum>1:
            print("Bot 2:",len(p3),"cards",b3,"books")
            if pNum>2:
                print("Bot 3:",len(p4),"cards",b4,"books")
        print("Pile:",len(pile),"cards")
        print("Cards:",p1)
        print("Books:",b1)
        input()
        playing = True
        os.system('cls')
        if len(p1)!=0 or len(pile)!=0:
            while playing:
                ask(p1,who(0))
                p1,b1=booker(p1,b1)
                if len(p1)==0 and len(pile)==0:
                    playing = False
            input()
        playing = True
        os.system('cls')
        if len(p2)!=0 or len(pile)!=0:
            print("Bot 1:")
            while playing:
                ask(p2,who(1))
                p2,b2=booker(p2,b2)
                if len(p2)==0 and len(pile)==0:
                    playing = False
            input()
        if pNum>1:
            playing = True
            os.system('cls')
            if len(p3)!=0 or len(pile)!=0:
                print("Bot 2:")
                while playing:
                    ask(p3,who(2))
                    p3,b3=booker(p3,b3)
                    if len(p3)==0 and len(pile)==0:
                        playing = False
                input()
            if pNum>2:
                playing = True
                os.system('cls')
                if len(p4)!=0 or len(pile)!=0:
                    print("Bot 3:")
                    while playing:
                        ask(p4,who(3))
                        p4,b4=booker(p4,b4)
                        if len(p4)==0 and len(pile)==0:
                            playing = False
                    input()
        if bT==13:
            game = False
    os.system('cls')
    if b1>b2 and b1>b3 and b1>b4:
        print("You Win!")
    elif b2>b1 and b2>b3 and b2>b4:
        print("Bot 1 Wins!")
    elif b3>b2 and b3>b1 and b3>b4:
        print("Bot 2 Wins!")
    elif b4>b2 and b4>b3 and b4>b1:
        print("Bot 3 Wins!")
    input()
    errorG = True
    os.system('cls')
    while errorG:
        try:
            print("Want to play again? (Y/N)")
            cont = str(input()).lower()
            if cont=="y":
                errorG = False
            elif cont=="n":
                errorG = False
                gaming = False
            else:
                os.system('cls')
                print("Input Valid Response")
        except:
            os.system('cls')
            print("Input Valid Response")

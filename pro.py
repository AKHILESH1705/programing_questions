# two child were playing a game in which they need to buy some item as per their interest .
# each child had same  amount of money in the form of notes of 500,200,100,50,10,5,2,1 amount.
# each child spent some amount "A" on purchasing their items and gave thier notes as amount.
# at last the one who has more number of notes will be consider as winner. 
# you need to help them by spending lessnumber of notes to purchase thier items. 
# you have given amount each child want to spend you need to decide winner of the game.
# 999<A<10000
# if child is asking for amount hich is out of limit which has given then appropriate message should be displayed.  
a=int(input("enter number:"))
b=int(input("enter second number:"))
n=0 
if a>999 and a<10000:
    r=a%500
    n=n+a/500
    while (r!=0):
        if r<2:
            n=n+1
        elif r<5:
            n=n+r/2
            r=r%2 
        elif r<10:
            n=n+r/5
            r=r%5       
        elif r<100:
            n=n+r/50
            r=r%50
        elif r<200:
            n=n+r/100
            r=r%100            
        else:
            n=n+r/200
            r=r%200
            print(n)
else:
    print("the amount of child is out of limit ")  
s=n
if b>999 and b<10000:
    n=0
    r1=b%500
    n=n+b/500
    while(r1!=0):
        if r1<2:
            n=n+1
        elif r1<5:
            n=n+r1/2
            r1=r1%2
        elif r1<10:
            n=n+r1/5
            r1=r1%5
        elif r1<50:
            n=n+r1/10
            r1=r1%10
        elif r1<100:
            n=n+r1/50
            r1=r1%50
        elif r1<200:
            n=n+r1/100
            r1=r1%100
        else:
            n=n+r1/200
            r1=r1%200
            print(n)
else:
    print("the amont of child b is out of limit") 
if (s<n):
    print("the first one is winer")
else:
    print("second one is winner")                           

                           

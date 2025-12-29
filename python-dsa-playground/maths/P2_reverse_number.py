""" 

reverse number =>   1234

output should be  => 4321

store it into another variable 

extract each value from the original number and store it into new variable.

you should multiply by 10 before place bacause for position placement



123

3 ->value=3

2->

"""

a=int(input("Enter your number"))
i=0
rev=0
if a==0:
    print("0")
else :
    while a>0:
        rev = rev*10 + a%10
        a//=10
print(rev)


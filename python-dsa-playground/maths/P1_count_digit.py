

# value = 221
# b = 23   output: 2

# Count the value - loop the number and find count


# 234/10 = > 23 /10 => 2/10 => 0

a=int(input("enter your number"))
count=0
a=abs(a)
if a == 0:
    print(1)
else :
    while a>0:
        count=count+1
        a=a//10
       

        
print(count)

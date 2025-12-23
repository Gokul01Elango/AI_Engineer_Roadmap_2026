"""
Topics :
    1.List
    2.Dict
    3.for loops
    4.Functions



    Mini tasks (do all 4):

        Print all even numbers from a list

        Count frequency of characters in a string

        Find max & min from a list (no max() / min())

        Write a function that reverses a string

"""
import random

def is_even():

    value=[1,2,43,45,33,24,8,42,70,42,14]
    for i in value:
        if i%2==0:
            print(i)
def count_frequency():
    sent="I am working as developer in TCS"
    print(sent.count)
    freq={}
    for i in sent:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)
def find_max_min():
    values=[10,33,34,54,65,22,3,1,9,32,4,5,6,34,23,2,2,1,1,1,1]
    max=values[0]
    min=values[0]
    # print(min)
    for i in values:
        if(max<i):
            max=i
        if(min>i):
            min=i

    print(min)
    print(max)

    # print(values)

def reversestring():
    sentence="Working"
    # print(sentence.reverse())
    # print(sentence[::-1])
    # print(sentence[-1])
    
    
    n=len(sentence)
    s=""

    i=1
    # print(n)
    for i in range(n):
        s+=sentence[n-i-1]
     
    print(s)

    # for 

def Guessing_game():
    print("Guess the number")
    number=random.randint(1,100)
    bool=True
    while bool:
        user_inp=int(input("Enter your Guess.."))
        if user_inp>number:
            print("Too high")
        elif user_inp<number:
            print("Too Low")
        elif user_inp==number:
            print("You are correct")
            bool= False

    print(number)

Guessing_game()
# reversestring()
# find_max_min()
# count_frequency()
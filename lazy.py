print("hello everyone!!!")
chorus=input()

print("how are you guys today?")
chorus=input()

if chorus == ("fine"):
    print("that is great")
else:
    print("what is the problem?")
    chorus1=input()

print("hey, whats your name?")
myName=input()

print("it is great to have you here " +myName)

print("the lenght of your name is:")
print(len(myName))

print("how old are you?")
age=input()

print("meaning you will be " + str(int(age) +1) + " in a year")

print("what is your grade?")

grade=int(input())

if grade >= 69:
    print("pass")
    print("great job")
elif grade < 69:
    print("fail")
    print("better luck next time")

print("what was your average score in science subjects last year?")
score=int(input()) 
while score != True: 
    if score == grade:
        print("alright")
        break
    if  score > grade:
        print("it decreased by: ")
        print(score - grade)
        print("meaning you did poor")
        break
    if score < grade:
        print("it increased by: ")
        print(-score + grade)
        print("you did better")  
        break
    
print("good bye " +myName)

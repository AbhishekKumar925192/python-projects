# quiz game project
print("welcome to my computer quiz!") 
playing= input("do you want to play? ")

if (playing.lower() != "yes"):
    quit()

print("okay! let's play:)")
score = 0

answer = input("what does CPU stand for? ")
if (answer.lower() == "central processing unit"):
    print("correct!")
    score += 1
else:
    print("incorrect")


answer = input("what does GPU stand for? ")
if (answer.lower() == "graphics processing unit"):
    print("correct!")
    score += 1
else:
    print("incorrect")


answer = input("Who was the first President of India? ")
if (answer.lower() == "Dr. Rajendra Prasad"):
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("In which year did India gain independence? ")
if (answer.lower() == "1947"):
    print("correct!")
    score += 1
else:
    print("incorrect")

print ("you got " + str((score / 4) * 100) + " %.")

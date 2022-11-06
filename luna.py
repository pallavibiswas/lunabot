score=0
score = int(score)

print("Over the last  2-3 weeks, how often have you been bothered by any of the following problems? \n ")

# QUESTION 1
answer1 = input("1. Little interest or pleasure in doing things  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer1 == "a" or answer1 == "Not at all":
    score+=0
elif answer1 == "b" or answer1 == "Several Days":
    score+=1
elif answer1 == "c" or  answer1 == "More than half the days":
    score+=2
elif answer1 == "d" or  answer1 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 2
answer2 = input("2. Feeling down, depressed, or hopeless  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer2 == "a" or answer2 == "Not at all":
    score+=0
elif answer2 == "b" or answer2 == "Several Days":
    score+=1
elif answer2 == "c" or  answer2 == "More than half the days":
    score+=2
elif answer2 == "d" or  answer2 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 3
answer3 = input("3. Trouble falling or staying asleep, or sleeping too much  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer3 == "a" or answer3 == "Not at all":
    score+=0
elif answer3 == "b" or answer3 == "Several Days":
    score+=1
elif answer3 == "c" or  answer3 == "More than half the days":
    score+=2
elif answer3 == "d" or  answer3 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 4
answer4 = input("4. Feeling tired or having little energy  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer4 == "a" or answer4 == "Not at all":
    score+=0
elif answer4 == "b" or answer4 == "Several Days":
    score+=1
elif answer4 == "c" or  answer4 == "More than half the days":
    score+=2
elif answer4 == "d" or  answer4 == "Nearly Everyday":
    score+=3
    
print("\n")

# QUESTION 5
answer5 = input("5. Poor appetite or overeating  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer5 == "a" or answer5 == "Not at all":
    score+=0
elif answer5 == "b" or answer5 == "Several Days":
    score+=1
elif answer5 == "c" or  answer5 == "More than half the days":
    score+=2
elif answer5 == "d" or  answer5 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 6
answer6 = input("6. Feeling bad about yourself — or that you are a failure or have let yourself or your family down   \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer6 == "a" or answer6 == "Not at all":
    score+=0
elif answer6 == "b" or answer6 == "Several Days":
    score+=1
elif answer6 == "c" or  answer6 == "More than half the days":
    score+=2
elif answer6 == "d" or  answer6 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 7
answer7 = input("7. Trouble concentrating on things, such as reading the newspaper or watching television  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer7 == "a" or answer7 == "Not at all":
    score+=0
elif answer7 == "b" or answer7 == "Several Days":
    score+=1
elif answer7 == "c" or  answer7 == "More than half the days":
    score+=2
elif answer7 == "d" or  answer7 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 8
answer8 = input("8. Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual   \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer8 == "a" or answer8 == "Not at all":
    score+=0
elif answer8 == "b" or answer8 == "Several Days":
    score+=1
elif answer8 == "c" or  answer8 == "More than half the days":
    score+=2
elif answer8 == "d" or  answer8 == "Nearly Everyday":
    score+=3

print("\n")

# QUESTION 9
answer9 = input("9. Thoughts that you would be better off dead or of hurting yourself in some way  \na. Not at all \nb. Several Days \nc. More than half the days \nd. Nearly Everyday \nAnswer: ")
if answer9 == "a" or answer9 == "Not at all":
    score+=0
elif answer9 == "b" or answer9 == "Several Days":
    score+=1
elif answer9 == "c" or  answer9 == "More than half the days":
    score+=2
elif answer9 == "d" or  answer9 == "Nearly Everyday":
    score+=3


print("\nscore: " + str(score))





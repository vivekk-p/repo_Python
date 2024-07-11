print("\n")
print("     Welcome to Computer Quiz !!\n")

play = input("Do you want to play? 'Y' for Yes or 'N' for 'No':\n ")
if play != 'Y' and play != 'y':
    print("Why don't you give it a try??")
    quit()
print("\nLet's Play with some easy questions!!\n")

score = 0
ans = input("What does CPU stand for?\n 1. Central Processing Unit    2. CentOS Ping Unix\n Answer with 1 or 2\n")

if ans == str(1):
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")

ans = input("What does RAM stand for?\n 1. RansomeWare Attack Mail    2. Random Access Memory \n Answer with 1 or 2\n")

if ans == str(2):
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")

ans = input("What is Linux?\n 1. High Level Language    2. An Operating System \n Answer with 1 or 2\n")

if ans == str(2):
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")

ans = input("What is Google Chrome?\n 1. A broswer to access website online    2. A Chrome plate made by Alphabet and Google company \n Answer with 1 or 2\n")

if ans == str(1):
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")

print("Your score is " + str(score))
percent = int((score/4)*100)
print("Your score is " + str(percent) + "%")

print('Thank you!!')
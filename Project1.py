print("\n")
print("Welcome to Computer Quiz !!\n")

play = input("Do you want to play? 'Y' for Yes or 'N' for 'No':\n  \n")
if play != 'Y':
    print("This will be your last regret not playing this quiz..Whoooshh!!")
    quit()
print("\nFine! Let's Play with some easy questions!!\n")

ans = input("What does CPU stand for?\n 1. Central Processing Unit    2. CentOS Ping Unix\n Answer with 1 or 2\n")

if ans == str(1):
    print("Correct\n")
else:
    print("Wrong\n")

ans = input("What does RAM stand for?\n 1. RansomeWare Attack Mail    2. Randome Access Memory \n Answer with 1 or 2\n")

if ans == str(2):
    print("Correct\n")
else:
    print("Wrong\n")

ans = input("What is Linux?\n 1. High Level Language    2. An Operating System \n Answer with 1 or 2\n")

if ans == str(2):
    print("Correct\n")
else:
    print("Wrong\n")

ans = input("What is Google Chrome?\n 1. A broswer to access website online    2. A Chrome plate made by Alphabet and Google company \n Answer with 1 or 2\n")

if ans == str(1):
    print("Correct\n")
else:
    print("Wrong\n")

print('Thank you for wasting your time!!\n')
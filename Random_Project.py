import random
chosen_number = random.randint(1,1000)
for _ in range(10):
    i = int(input("Enter the number that you think it is: "))
    if i == chosen_number:
        print("Hurray, You guessed the right number")
        break;
    else:
        if chosen_number > i:
            print("Greater")
        else:
            print("Smaller")
else:
     print("You have run out of chances.better luck next time")
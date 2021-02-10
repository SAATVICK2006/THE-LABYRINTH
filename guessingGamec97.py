import random
number = random.randint(1,9)

life = 4

print("YOU GOT 4 CHANCES TO GUESS A NUMBER IN BETWEEN 1 AND 10.")

guess = int(input("Guess a number in between 1 and 10: "))

while life >= 1:
    if guess == number:
        print ("CORRECT!YOU ARE THE AKINATOR!")
        break
    if life == 1:
        print("YOU LOSE!It was",number,".")
        break
    if guess < number:
        print ("No.Your guess is a bit lower than the number.You have",life-1,"chances left.")
        guess = int(input("Try again.Guess a number in between 1 and 10: "))
        life = life - 1
    elif guess > number:
        print ("No.Your guess is higher than the number.You have",life-1,"chances left.")
        guess = int(input("Try again.Guess a number in between 1 and 10: "))
        life = life - 1
from random import randint
name = input("Hello, What is your Name?") 
print("Well, " + name + ", " + "i am thinking of a number between 1 and 20, try to take a guess." )
print("You have 5 guesses")
answer = randint(1,20)
for i in range(5):
    guess=int(input("Take a guess:"))
    if guess > answer:
        print ("your guess is too high")
    if guess < answer:
        print ("your guess is too low")
    if guess == answer:
        print("Good Job!" ,name,"," "you guessed my number in", i+1, "guesses!")
        break
else:
    print("Nope,the number I was thinking of was", answer)

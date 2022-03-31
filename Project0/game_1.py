import numpy as np

number = np.random.randint(1, 101) # think of a number

count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100:"))
    
    if predict_number > number:
        print("The number must be less!")

    elif predict_number < number:
        print("The number must be greater!")

    else:
        print(f"You guessed the number! This number = {number}, for {count} attempts")
        break # end of the game, exit from the cycle
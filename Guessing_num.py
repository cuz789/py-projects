"""
GUESSING NUMBER GAME

Task: Below are the steps:

Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

Analysis:

Explanation 1: If the User inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer. 
And now the guessing game started, so the user entered 50 as his/her first guess. The compiler shows “Try Again! You guessed too high”. 
That’s mean the random number (i.e., 42) doesn’t fall in the range from 50 to 100. That’s the importance of guessing half of the range.
And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25. The user enters 25 as his/her second guess. 
This time compiler will show, “Try Again! You guessed too small”. That’s mean the integers less than 25 (from 1 to 25) are useless to be guessed.
Now the range for user guessing is shorter, i.e., from 25 to 50. Intelligently! The user guessed half of this range, so that, 
user guessed 37 as his/her third guess.  This time again the compiler shows the output, “Try Again! You guessed too small”. 
For the user, the guessing range is getting smaller by each guess. Now, the guessing range for user is from 37 to 50, 
for which the user guessed 43 as his/her fourth guess. This time the compiler will show an output “Try Again! You guessed too high”.
So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of this range,
that is, 40 as his/her fifth guess.  This time the compiler shows the output, “Try Again! You guessed too small”. 
Leaving the guess even smaller such that from 41 to 43. And now the user guessed 41 as his/her sixth guess.
Which is wrong and shows output “Try Again! You guessed too small”. And finally, the User Guessed the right number which is 42 as his/her seventh guess.

          Total Number of Guesses = 7

Hint:

Minimum number of guessing = log2(Upper bound – lower bound + 1)

"""
import random
import math

#Provding the range values
a = int(input("Provide the lowest number in range: "))
b = int(input("Provide the highest number in range: "))
print(f"Provided the range is between {a} and {b}")
#System selects a random n.o in range
number = random.randint(a,b)
print(number) #Printed to understand which number is assigned 
#User guesses and chances
total_chances = round(math.log2(b-a + 1))
print("Total Chances" , total_chances)
for i in range (1, total_chances+1) :
    guess = int(input("Guess number in range: "))
    if guess == number :
        print("Correct guess! The number is " , number)
        break
#Using elif to n unsuccessful attempts : writing as first elif because elif passes the first true statement
    elif total_chances-i == 0:
        print("GAME OVER \nBetter luck in next time!!! The number is ", number)
    elif guess > number:
        print(f"Guess is large! Try again : you have {total_chances - i} chances")
    elif guess < number:
        print(f"Guess is small! Try again: you have {total_chances - i} chances")
    else :
        print(f"Wrong guess ! Try again : you have {total_chances - i} chances")
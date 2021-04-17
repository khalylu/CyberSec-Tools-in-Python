''' original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for x in original_prices:
    discount_amount = x * .6
    final_price = x - discount_amount
    print(f"original price: {x:3} discount amount: {discount_amount:3.2f} final price: {final_price:3.2f}")
'''

'''for x in range(0, 100, 10):
    Fahrenheit = ((9/5) * x) + 32
    print(f'{x} \t {Fahrenheit}')'''


# exercise 64

'''prices = []
num = int(input("enter number of items you about to input \n"))
for i in range(num):
    prices.append(float(input('enter prices \n')))
    total_cost = sum(prices)
    print(prices)
    if prices == 0:
        break
    else:
        print(f"The total sum of the price lists = {total_cost}")
        print(f'Amount if paid in cash = {total_cost // .05}')
'''
'''from random import randint

print("Pick a number from 1 to 100, must be an integer.\nNo numbers outside those boundaries,"
      " Enjoy the Game, pick numbers wisely!!!\n")

random_number = randint(1, 100)
guessed_number = []

while True:
    guess = int(input("Enter the guessed number"))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    if guess == random_number:
        print("Congratulations You have Guessed The Right Number")
        guessed_number.append(guess)
        break

    if guess != random_number:
        if abs(random_number - guess) <= 10:
            print("WARM!!!")
        else:
            print("COLD!!!")

    else:
        if abs(random_number - guess) < abs(random_number - guess[-2]):
            print("WARMER!!!")
        else:
            print("COLDER!!!")
'''

# exercise 51 if else to solve 66

'''letter_grade = str(input("Enter the letter grade\n"))
letter_grade = letter_grade.upper()

if letter_grade == "A+":
    A_PLUS = 4.0
    print(F"Grade Points is {A_PLUS}")
elif letter_grade == "A":
    print("Grade Points is 4.0")
elif letter_grade == "A-":
    print("Grade Points is 3.7")
elif letter_grade == "B+":
    print("Grade Points is 3.3")
elif letter_grade == "B":
    print("Grade Points is 3.0")
elif letter_grade == "B-":
    print("Grade Points is 2.7")
elif letter_grade == "C+":
    print("Grade Points is 2.3")
elif letter_grade == "C":
    print("Grade Points is 2.0")
elif letter_grade == "C-":
    print("Grade Points is 1.7")
elif letter_grade == "D+":
    print("Grade Points is 1.3")
elif letter_grade == "D":
    print("Grade Points is 1.0")
elif letter_grade == "F":
    print("Grade Points is 0")
else:
    print("Invalid Entry")


lst_lg = []

while lst_lg != "":
    lst_lg.append(letter_grade)'''

# exercise 72 and 73
'''word_phrase = input("enter the word to check \n")


if word_phrase == word_phrase[::-1]:
    print(f"{word_phrase} is a palindromic word")
else:
    print(f"The word {word_phrase} not a palindromic word or phrase")'''


'''for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x}")
        print(y*x, end=" ")'''


'''m = int(input("enter the first number\n"))
n = int(input("enter the first number\n"))

d = min(m, n)

while m % d == 0 or n % d == 0:
    d = d - 1
    print(f"{d} is the GCD of m and n")'''















































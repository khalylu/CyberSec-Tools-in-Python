# Assignment 4
'''
length = float(input("Enter length in ft "))
width = float(input("Enter width in ft "))
sq_ft = length*width
print(sq_ft, "squared feet")
acre = 43560/sq_ft

print(acre, 'acres')
'''
# Assignment 5
'''more_than_litre = float(input("enter number of bottles less than or equal to a litre "))
less_than_litre = float(input('enter number of bottles more than a litre '))

refund = (.25*more_than_litre + .10*less_than_litre)
print(f"${refund:0.2f} is the amount you will receive.")'''

# Exercise 33

'''bread_price = 3.49
no_of_bread = int(input('enter the number of bread '))

reg_price = bread_price * no_of_bread
discount = reg_price * .6
total_price = reg_price - discount

print(f"Regular price for the day old bread is ${reg_price:10.2f}")
print(f'Discount for the loaves of bread ${discount:10.2f}')
print(f'Final total price of the day old loaves of bread is ${total_price:10.2f}')'''

# exercise 31

'''num = int(input("Input a four digit numbers: "))
x = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10

sum = x+x1+x2+x3

print(f'{x} + {x1} + {x2} + {x3} = {sum}')'''

# exercise 61
'''list_1 = []
num = int(input('enter the length of list \n'))
for i in range(num):
    list_1.append(float(input('enter all elements of list \n')))
    if list_1 == 0:
        print('error 0 is not valid for entry')
        break
    else:
        print(list_1)
        print((sum(list_1)) / num, 'is the average of list entered')
'''
# statement assessment
'''st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0] == 's':
        print(x)'''

st = 'Create a list of the first letters of every word in this string'
i = [x[0] for x in st.split()]
print(i)


































#python3

#This program checks to see if a number is prime.
#'i' represents the number to being checked against the input number.
i = 2
#This line allows user to input a number to find  if it is prime.
x = int(input('What number would you like checked?'))

print('')
print(x)
#This checks if the number is prime.
if x <= 0:
    print('Negative numbers can\'t be prime.')
for i in range (2, x + 1):
    if x == 1:
        print('One is not prime or non-prime.')
        break
    elif x == i:
        print('This number is prime.')
    elif x % i == 0:
        print('This number is not prime.')
        break
    else:
        i += 1
    

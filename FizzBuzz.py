#python3
#FizzBuzz game talked about by Tom Scott on YouTube
i = 1

while i <=100:
    text = ("")
    
#Add any more challenges below for the computer to check
    if i % 3 == 0:
        text += 'Fizz'
    if i % 5 == 0:
        text += 'Buzz'
    
#This prints the text needed
    if text == (""):
        print(i)
    else:
        print(text)
    i += 1
    text = ("")

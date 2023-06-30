#Magic 8-Ball Game

#import random number generator
import random

#have the user enter their name before the game loop starts 
name = input("What is your name? ")
#declare a question and answer variable as empty string for now
question = ""
answer = ""
#verification variable if user wished to end
verif = ""

#create a while loop that will not end unitl user enters 'goodbye'
while (verif != "no"):
    question = input("What is your question? ")
    
    #use the random number generator
    num = random.randint(1,9)

    #if else statements to determine the response 
    if (num == 1):
        answer = "Yes - definitely"
    elif (num == 2):
        answer = "It is decidedly so"
    elif (num == 3):
        answer = "Without a doubt"
    elif (num == 4):
        answer = "Reply hazy, try again"
    elif (num == 5):
        answer = "Ask again later"
    elif (num == 6):
        answer = "Better not tell you now"
    elif (num == 7):
        answer = "My sources say no"
    elif (num == 8):
        answer = "Outlook not so good"
    elif (num == 9):
        answer = "Very doubtful"
    else:
        answer = "Error"
    
    #print the user question and the response
    print(name + " asks: " + question)
    print("The answer is: " + answer)

    #verif if the user would like to continue
    verif = input("Would you like to conintue? Yes or No ").casefold()


    





#This code will simulate asking a Magic Eight Ball a questiion
#and getting an answer for it



import random
import time
import json
import os

global question


#List for all the answers:
    
answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes – definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
]

#Initialize history file
with open("history_file.txt", "w") as f:
    f.write("Here are my fortunes!")


with open("history_file.txt", "r") as f:
    print(f.read())

""" 
This function saves the questions and the answers done
to the 8 ball
"""
    
def save_history(question, answer):
    history_file = 'history.json' #Define file name 
    history = [] #Initialize empty list for history

    #Check if file exists
    if os.path.exists(history_file):
        #open in read mode and load existing history
        with open(history_file, 'r') as f:
            history = json.load(f)

    #Append new question and answer to history
    history.append({
        'question': question, 'answer': answer
    })
    #Open File in write mode and dump updated history
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=2)


def load_history():
    history_file = 'history.json'
    history = []

    if os.path.exists(history_file):
        #Open file in read mode and load history
        with open(history_file, 'r') as f:
            history = json.load(f)
    #Return loaded history
    return history


def eight_ball():
    
    global question
    print("THE EIGHT BALL DICTATES YOU ASK A QUESTION!")
    #Defines question as input from user
    question = input("Ask me anything!:")
    if question == 'no':
        
        print("Fine... Your loss!")
    else:
            print("Asking the voices..\n")
            #3 second wait before answer
            time.sleep(3)
        
            answer = random.choice(answers)
            print(answer)
            
            save_history(question, answer)
    
        
def main():
    global question
    replay = 'yes'
    while replay != 'no':
        eight_ball()
        if question =='no':
            break
        replay = input("Would you like to ask another question?: ")
        
        
main()

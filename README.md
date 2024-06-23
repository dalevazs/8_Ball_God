# 8_Ball_God
By David Vasquez
Welcome to my first pyhton project!

For my Basics of Coding class I was asked to develop a fully functional program, that  implemented the use of all the functionalities learned thought to us thus far. This is what I came up with.

Whenever I find myself in doubt, I usually find myself craving a simple solution to which i do not have to think much about, a toss of a coin, a tic tac toe, or going with what comes to mind first. As a a bit of fun, I decided to make this concept my main project. The idea behind the 8 ball god program comes from a wish for answers to which we do not have to put our mind to.

Why an 8 ball you might be wondering 

First we start with our imports:

```python
import random
import time
import json
import os
```

Random will be used to iterate through my list of answers in a later function.

Time makes it so the program is more interactive.

Json both allows me to save my questions and answers in a json file, as json text.

Os helps me check if the path to my file exists.

```python
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
```

Function “save_history” is used to save my questions and answers to a json file called ‘history.json’. 

It first checks if the file exists, if it does, it appends the current question and answer pair, and then saves the updated history back to “history.json’.  If the file does not exist, it creates a new file and appends the question and answer pair to it.

```python
def load_history():
    history_file = 'history.json'
    history = []

    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)

    return history
```

This function is used to return the loaded history as a list of dictionaries, each dictionary represents a pair of questions and answers.
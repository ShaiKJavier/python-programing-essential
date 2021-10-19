#!/usr/bin/env python
# coding: utf-8

# # Essentials of Python Programming

# In[ ]:


#Write a Python program to develop a Rock, Papers and Scissors game to be played against a computer.


# In[2]:


import random #importing the random module #it is built in module

while True:   #while is loop used when multiple conditions used
    human_action = input("enter the choice you want(rock,paper,scissors,lizard,spock):") #user actions are enter by the user
    
    actions = ["rock","paper","scissors","lizard","spock"] #actions is the name for list #in the list string data types used as doble qouts"" 
    
    machine_actions = random.choice(actions)  #machine actions means computer will perform the actions as random choice of actions
    
    print("\nyou choose{human_actions} vs machine choose{machine_actions}.\n") #using get the output as user actions vs machine actions
    
    if human_action == "machine_actions": #if is the condition used for if actions are equal to machine actions then it will give correct output
        print(f"both players selected same actions:it's tie") #when it is equal it shows tie 
    elif human_action == "rock":  #nested if is used if the  first condition not satisfies it takes the another action
        if machine_actions == "scissors": # action will have another condition
            print("rock hits the scissors:you win") #actions equal to computer action it will print you win
        else:
            print("paper covers the rock:you lose") #else you lose
            
    elif human_action =="paper": #another condition if above action not satisfies goes for another action
        if machine_actions == "rock": # action will have another condition
            print("paper covers the rock:you win")#actions equal to computer action it will print you win
        else:
            print("scissors cuts the paper:you lose")#else you lose
            
    elif human_action =="scissors":#nested if is used if the  first condition not satisfies it takes the another action
        if machine_actions == "papers":# action will have another condition
            print("scissors cuts the paper:you win")#actions equal to computer action it will print you win
        else:
            print("rock hits the scissors:you lose")#else you lose
    elif human_action == "lizard":
        if machine_actions == "papers":
            print("lizard eats the paper:you win")
        else:
            print("rocks hits lizard the lizard dies:you loss")
    elif human_action == "spock":
        if machine_actions == "scissors":
            print("spock smashes the scissors : you win")
        else:
            print("paper disproves spock : you loss")
    
            
    play_again = input("\nplay again?click(yes/no):\n") #you want to play again click yes means yes or no means no
    if play_again.lower() != "yes":#.lower means it should be small letter
        print("\n well played")
        
        break #hence conditions are break


# In[ ]:





# In[ ]:





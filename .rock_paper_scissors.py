print ("Welcome to the Rock-Paper-Scissors Game!\nLet's see if you can outsmart the computer! ")

rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player = input("Choose your hand wisely: O for rock, 1 for paper or 2 for scissors\n")
import random
npc_list = [ "rock" , "paper", "scissors"]
npc_choice = random.choice(npc_list)

print("Player's hand")
if player == "0":
    player = "rock"
    print(rock1)
elif player == "1":
    player = "paper"
    print(paper1)
elif player == "2":
    player ="scissors"
    print(scissors1)

print("NPC's hand")
if npc_choice == "rock":
    print(rock1)
elif npc_choice == "paper":
    print(paper1)
elif npc_choice == "scissors":
    print(scissors1)



if player == npc_choice:
    print("It's a tie! Try again.")
if player != npc_choice:
    if player == "rock" and npc_choice == "scissors":
        print("Player wins!")
    if player == "scissors" and npc_choice == "paper":
         print("Player wins!")
    if player == "paper" and npc_choice == "rock":
         print("Player wins!")
    if npc_choice == "scissors" and player == "paper":
        print("NPC wins, you lose!")
    if npc_choice == "paper" and player == "rock":
        print("NPC wins, you lose!")
    if npc_choice == "rock" and player == "scissors":
        print("NPC wins, you lose!")

print("Thanks for playing!")


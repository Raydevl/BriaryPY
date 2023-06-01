import os
import random
import time 
import colorama 
from colorama import init, Fore, Back, Style
init()
terrainadj = ["big", "small", "tiny", "huge"] ##defines alot of the 'story'
terraincoloradj = ["black", "white", "reddish-blue", "Light Orange"]
terraincoloradj2 = ["black", "white", "reddish-blue", "Light Orange"]
structure = ["house", "Gas Station", "Book store"]
terrain = ["landscape", "Island", "Forest"]
desc = ["on top of", "below", "hovering above", "currently in a superpositional state on"]
storyoption = ["open", "close"]
object = ["door", "trapdoor"]
story = f"you arrive at a {random.choice(terrainadj)} {random.choice(terraincoloradj)} {random.choice(structure)}, which is {random.choice(desc)} a {random.choice(terraincoloradj2)} {random.choice(terrain)}, you can currently {random.choice(storyoption)} a {random.choice(object)}, which is  {random.choice(desc)} it." ##defines format
print(Fore.RED + "tis' a short procedural generator I made" + Fore.RESET)
time.sleep(5)
print (story) 
##defines roomgen
radioshow = ["Endless Radiant Talkshow!", "Jimmy's Radio Show"]
radioguest = ["Jaseko", "Ian"]
radiohost2 = ["Jimmy Jahammas", "Radian"]
radiotalk = f"(Radio): :Hello, welcome to the {random.choice(radioshow)}, with {random.choice(radiohost2)}, and {random.choice(radioguest)}:"
while True:
    user_input = input("Do you open it? (y/n): ")
    if user_input.lower() == 'y':
        roomlight = random.choice(["dimly lit", "brightly lit", "pitch black", "extremely bright"])
        roomfurniture = random.choice(["bookshelf", "drawer", "desk"])
        item = random.choice(["book", "knife", "python coding manual", "bottle of green tea", "radio"])
        roomgen = f"You are now in a {roomlight} {random.choice(terraincoloradj)} room. There is a {roomfurniture} with a {item} laying on top of it. There is also a {random.choice(object)} at the end of the room."
        print(roomgen)
    if item == 'radio':
        print(Back.BLUE + radiotalk + Back.RESET)
    elif user_input.lower() == 'n':
        print("Please pick y lol")

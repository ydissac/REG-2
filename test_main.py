#########
import splash
from compo import *
import sys
import random
#########

name = input("Before we begin, what's your name?\n")
print("Hello,", name,"!")
def insult():
    adjPrint = random.choice(adj)
    nounPrint = random.choice(noun)
    verbPrint = random.choice(verb)
    specialPrint = ""

    if random.random() < 50:
        specialPrint = random.choice(special)
    
    print(name,", you're such ",specialPrint, adjPrint, nounPrint, verbPrint,"!")  # ugly, but it works.
insult()
retry = input("\nWould you like to hear another one? (y/n)\n")
# if retry == "y":
#   insult()
# else:
#   print("\nGoodbye.")
#   exit()
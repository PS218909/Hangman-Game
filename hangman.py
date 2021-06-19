import random
CHANCE = []
file = open("wordlist.txt","r")
words = file.read().split("\n")
if "" in  words:
    words.remove("")
word = random.choice(words)
empty = ["_"]*len(word)
used = []
print(word)
print(f"you have {5-len(CHANCE)} left")
def start(word):
    print(" ".join(empty))
    inp = input("enter your character : ")[0].lower()
    if inp not in used:
        used.append(inp)
    elif inp in used:
        print(f"{inp} is used before")    
        start(word)
    tf = check(inp,word)
    if tf == True:
        for i in range(len(word)):
            if word[i] == inp:
                empty[i] = inp
        if "".join(empty)==word:
            print("YOU WIN!!")
            return
        start(word)
def check(inp,word):
    if len(CHANCE)>=5:
        return False
    if inp not in word:
        CHANCE.append(1)
        if 5-len(CHANCE)!=0:
            print(f"you have {5-len(CHANCE)} Chance left")
        else:
            print(f"YOU LOSE!! THE WORD WAS '{word.upper()}'")
        if len(CHANCE)<=4:
            start(word)
    if inp in word:
        return True
start(word)

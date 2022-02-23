import json
import random

def LetterCheck(word):
    placement = [input("First: "), input("Second: "), input("Third: "),input("Forth: "),input("Fifth: ")]
    return word, placement

with open("words.json", "r") as f:
    words = json.load(f)

IsFound = False

word = random.choice(words)
print(f"Use ({word})")

while not IsFound:
    found = input("Was It Correct? ")
    if found == "y":
        IsFound = True
        break
    else:
        pass
    
    placement = LetterCheck(word.lower())

    for i in range(0, 5):
        if placement[1][i].lower() == "g":
            x=len(words)
            while x:
                if words[x-1][i] != placement[0][i]:
                    words.remove(words[x-1])
                
                x-=1

        elif placement[1][i].lower() == "y":
            y = len(words)
            while y:
                if placement[0][i] not in words[y-1] or words[y-1][i] == placement[0][i]:
                    words.remove(words[y-1])

                y-=1

        elif placement[1][i].lower() == "n":
            z = len(words)
            while z:
                if placement[0][i] in words[z-1]:
                    words.remove(words[z-1])

                z-=1

    if len(words) == 1:
        IsFound = True
        print(words[0])
        break
    else:
        word = random.choice(words)
        print(f"Use ({word})")

print("THANKS FOR USING THIS BOT")
print("BOT CREATED BY FADILOMBI")

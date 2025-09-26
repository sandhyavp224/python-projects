import random
print("Hangman game")
words=['apple','banana','jackfruit','grape','orange']
word=random.choice(words)
guessed=["-"]*len(word)
attempts = 5
used_letter=[]
while attempts > 0 and "-" in guessed:

    
    print("Word:"," ".join(guessed))
    print("Attempts left:",attempts)
    print("Used Letters:"," ".join(used_letter))
    guess=input("Guess a letter: ").lower()
    
    if len(guess)!=1  or not guess.isalpha():
        print("Invalid! Please enter a single letter.")
        continue
    used_letter.append(guess)

    
    if guess in word:
        print("Great guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i]=guess
    else:
        print("Wrong guess!.")
        attempts-=1

if"-" not in guessed:
    print("Congratulation! you guessed a correct word")
else:
    print("Game Over! the word was:",word)
    

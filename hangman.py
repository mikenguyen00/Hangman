import random
def hangman(word):
    wrong=0
    stages=["",
            "_________          ",
            "         |         ",
            "         O         ",
            "        /|\        ",
            "        / \        ",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to the Hangman Game!")
    while wrong < len(stages)-1:
        print("\n")
        msg="Guess a Letter: "
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if e == len(stages):
            print("You Lose!")
            break

        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win=True
            break

words=["pickle","apple","dog","cat"]
hangman(words[random.randint(0,len(words))])

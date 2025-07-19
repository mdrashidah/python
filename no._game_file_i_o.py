import random
def game():
    print("welcome to your score board of the game to check the highest score")
    score = random.randint(0,100)
    with open ("hiscore_of_game.txt") as f:
        hiscore_of_game = f.read()
        if hiscore_of_game == "":
            hiscore_of_game = 0
        else:
            hiscore_of_game = int(hiscore_of_game)
    print(f"you current score is : {score} ")

    #print(score)
    with open ("hiscore_of_game.txt", "a") as f:
        f.write(str(score))
    if score > int(hiscore_of_game):
        print("you have just broken the high score")
    else:
        print("you have AWAY from the high score")
    return score

game()
# Tyler Johnson
# 1/19/2023
# Black Jack
import random
from base_Cards import *
from players_code import *
from commonGameFunctions import *
from warFunctions import *

def main():
        print("Welcome to War!")
        print()
        print("You Start With 26 cards :)")
        input("Please press Enter to Start")
        running = True
        game = WarGame("War")
        game.startGame()
        game.reset()
        while game.checkInGame():
                game.reset()
                game.checkInGame()
                game.comparePlayerCards(game.player1,game.player2)
                game.checkInGame()

        print()
        print("Game Over!")
        for player in game.players:
                if len(player.cards) == 0:
                        print(player.name + " Loses!")
                else:
                        print(player.name + " Wins!")






main()



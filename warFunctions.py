from base_Cards import *
from players_code import *


class WarPlayer(Base_Hand):
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

    def resetFacing(self):
        for card in self.cards:
            card.isFaceUp = False
    def tied(self):
        for i in range(3):
            card = self.cards[i]
            card.flip()
            print(card)


    def compare(self,card1,card2):
        if card1.value > card2.value:
            return 0 #win
        elif card1.value == card2.value:
            return 2 #tie
        else:
            return 1 #lose

    def cardsLeft(self):
        cardsleft = len(self.cards)
        print(self.name+ " has " + str(cardsleft) + " cards left:")


# def Game():
#     deck = Base_Deck("Steve")
#     deck.populate()
#     deck.shuffle()
#     player1 = WarPlayer("You")
#     player2 = WarPlayer("Enemy")
#     players = [player1, player2]
#     deck.deal(players, len(deck.cards) // len(players))
#     running = True
#
#     while running:
#         print("reset")
#         cardsInPlay = []
#         for i in players:
#             cardamount = len(i.cards)
#             if cardamount < 0:
#                 players.remove(i)
#
#         if len(players) > 1:
#             running = True
#         else:
#             running = False
#
#         for player in players:
#             player.shuffleHand()
#             player.resetFacing()
#             player.flip_first_card()
#             cardsInPlay.append(player.cards[0])
#             player.cardsLeft()
#
#
#         cardCompared = 0
#         print("You flipped:")
#         print(player1.cards[cardCompared])
#         print("Joe Flipped:")
#         print(player2.cards[cardCompared])
#         compared_cards = player1.compare(player1.cards[0], player2.cards[0])
#
#
#         if compared_cards == 0: #won the comparison
#             print("You Win")
#             for i in range(1):
#                 card = player2.cards[cardCompared]
#                 player2.give_card(card,player1)
#             input("press Enter to Continue")
#
#
#         elif compared_cards == 1: #lost the comparison
#             print("You Lost")
#             for i in range(1):
#                 card = player1.cards[cardCompared]
#                 player1.give_card(card,player2)
#             input("press Enter to Continue")
#
#
#         elif compared_cards == 2: #Tied the comparison
#             print("You Tied")
#             input("press Enter to Continue")
#             print("You Flipped:")
#             player1.tied()
#             print("Joe Flipped:")
#             player2.tied()
#             cardCompared += 2


class WarGame():

    def __init__(self,deck):
        self.totalCards = Base_Hand("total")
        self.player1 = WarPlayer("You")
        self.player2 = WarPlayer("Enemy")
        self.players = [self.player1, self.player2]
        self.deck = deck

    def checkInGame(self):

        if len(self.player1.cards) >= 1 and len(self.player2.cards) >= 1:
            return True
        else:
            return False



    def startGame(self):
        self.deck = Base_Deck(self.deck)
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.players, len(self.deck.cards) // len(self.players))

        for i in self.players:
            self.cardamount = len(i.cards)
            if self.cardamount < 0:
                self.players.remove(i)
            else:
                pass


    def reset(self):
        for i in self.players:
            self.cardamount = len(i.cards)
            if self.cardamount < 0:
                self.players.remove(i)

        for player in self.players:
            player.shuffleHand()
            player.resetFacing()
            player.flip_first_card()
            print(player.cards[0])


    def comparePlayerCards(self,player1,player2):
        self.compared_cards = player1.compare(player1.cards[0], player2.cards[0])
        self.cardCompared = 0
        print(len(self.totalCards.cards))


        if self.compared_cards == 0:  # won the comparison
            print("You Win")
            if range(self.cardCompared > 1):
                for card in range(self.cardCompared):
                    card = player2.cards[self.cardCompared]
                    player2.give_card(card, player1)
                    self.totalCards.giveAll(player1)
                    self.totalCards.clear_hand()
                    for player in self.players:
                        player.cardsLeft()
            else:
                for card in range(1):
                    card = player2.cards[self.cardCompared]
                    player2.give_card(card, player1)
                    self.totalCards.giveAll(player1)
                    self.totalCards.clear_hand()
                    for player in self.players:
                        player.cardsLeft()
            input("press Enter to Continue")
            return

        elif self.compared_cards == 1:  # lost the comparison
            print("You Lost")
            if range(self.cardCompared > 1):
                for i in range(self.cardCompared):
                    card = player1.cards[self.cardCompared]
                    player1.give_card(card, player2)
                    self.totalCards.giveAll(player2)
                    self.totalCards.clear_hand()
                    for player in self.players:
                        player.cardsLeft()
            else:
                for i in range(1):
                    card = player1.cards[self.cardCompared]
                    player1.give_card(card, player2)
                    self.totalCards.giveAll(player2)
                    self.totalCards.clear_hand()
                    for player in self.players:
                        player.cardsLeft()
            input("press Enter to Continue")
            return

        elif self.compared_cards == 2:  # Tied the comparison
            print("You Tied")
            print("Everyone Puts 4 cards in the pool")
            self.tiedGame()
            for player in self.players:
                player.cardsLeft()
            input("press Enter to Continue")
            return

    def tiedGame(self):
        for player in self.players:
            if len(player.cards) >= 4:
                for i in range(4):
                    player.give_card(player.cards[0],self.totalCards)
            elif len(player.cards) == 0:
                self.checkInGame()
            else:
                for i in range(len(player.cards)-1):
                    player.give_card(player.cards[0],self.totalCards)

















from random import shuffle

#Create classes for blackjack program
#This .py file will work as a module of classes
#That will be imported in the main program
#All classes will be part of this module and game willl be a separate .py program file

class Deck:

    def __init__(self):
        pass

# A function for creating a deck
# The deck will contain cards of Suits: Heart, Spade, Diamond, Clubs  and Ranks: Ace, 2-10, Jack, Queen, King
    def deck_cards(self):
        result = []
        suit = ['H', 'S', 'D', 'C']
        num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in suit:
            for n in num:
                result.append(i+n)

# The function will return a shuffled deck with 52 cards
        shuffle(result)

        return result


class Deal:

    def __init__(self):
        pass

# A function for creating player and dealers hands
# The player and dealer will get 2 cards initially

    def deal_cards(self,cards):
        player_hand = []
        dealer_hand = []

        player_hand.append(cards.pop())
        player_hand.append(cards.pop())
        dealer_hand.append(cards.pop())
        dealer_hand.append(cards.pop())

        return [player_hand, dealer_hand]


class Calculation:

    def __init__(self):
        pass

# A function for counting the points
# This function will count the points of the player and the dealer
# The point calculation logic will also determine the value of ACE as 1 or 11 depending on the situation

    def point_calc(self, my_cards):
        point = 0
        ace = 0
        for i in my_cards:
            if i[1] in ['J','Q','K']:
                point = point + 10
            elif i[1] in ['1','2','3','4','5','6','7','8','9','10']:
                point = point + int(i[1])
            else:
                point = point + 1
                ace = 1
        if ace == 1 and point <= 10:
            point = point + 10


        return point


if __name__ == "__main__":
    mydeck = Deck()
    print(mydeck.deck_cards())


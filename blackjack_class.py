from random import shuffle


# Create classes for blackjack program
# This .py file will work as a module of classes
# That will be imported in the main program
# All classes will be part of this module and game will be a separate .py program file.

class Deck:

    def __init__(self):
        pass

    # A function for creating a deck

    # The deck will contain cards of Suits: Heart, Spade, Diamond, Clubs  and Ranks: Ace, 2-9, T, Jack, Queen, King
    def deck_cards(self):
        """
        Create a list of 52 cards and shuffle them
        :return: List of decks
        """
        result = []
        suit = ['H', 'S', 'D', 'C']
        num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        for i in suit:
            for n in num:
                result.append(i + n)

        # The function will return a shuffled deck with 52 cards
        shuffle(result)

        return result


class Deal:

    def __init__(self):
        pass

    # A function for creating player and dealers hands
    # The player and dealer will get 2 cards initially

    def deal_cards(self, cards):
        """
        takes the deck of cards and distributes 2 cards each to the player and the dealer
        :param cards: List of cards
        :return: list of cards of the player, list of cards of the dealer, balance deck of cards
        """
        player_hand = []
        dealer_hand = []

        player_hand.append(cards.pop(0))
        player_hand.append(cards.pop(0))
        dealer_hand.append(cards.pop(0))
        dealer_hand.append(cards.pop(0))

        return [player_hand, dealer_hand, cards]


class Calculation:

    def __init__(self):
        pass

    # A function for counting the points
    # This function will count the points of the player and the dealer
    # The point calculation logic will also determine the value of ACE as 1 or 11 depending on the situation

    def point_calc(self, my_cards):
        """
        Take the list of cards in hand and calculates the points. It adds 1 for Ace or 11 for ace depending on
        the total score
        if the total score is more than 21 it considers ACE as 1 but if the total score is less than 21 then it
        counts Ace as 11
        :param my_cards:list of cards in hand
        :return:points of the cards in hand
        """
        point = 0
        ace = 0
        for i in my_cards:
            if i[1] in ['T', 'J', 'Q', 'K']:
                point = point + 10
            elif i[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                point = point + int(i[1])
            else:
                point = point + 11
                ace = ace + 1

        if ace > 0:
            for i in range(0, ace):

                if point > 21:
                    point = point - 10

        return point


class Player:

    def __init__(self):
        pass

    def player_hit(self, my_cards, deck):
        """
        takes the cards on hand and the deck of cards and distributes one card to the player
        it also calculates the points of cards after adding the card to the players hand
        :param my_cards: cards on hand
        :param deck: deck of cards
        :return: list of cards on hand, balance deck of cards, total points of cards on hand
        """
        my_cards.append(deck.pop(0))
        calc_class = Calculation()
        points = calc_class.point_calc(my_cards)
        return (my_cards, deck, points)


class Dealer(Player):  # Dealer class is inherited from Player class.

    def __init__(self):
        pass

    def dealer_hit(self, my_cards, deck):
        """
        takes the cards on hand of the dealer and the deck of cards
        It adds cards to the hand of the dealer till the total score exceeds 16
        It calculates the total points of the cards on hand of the dealer
        :param my_cards: list of cards on hand of the dealer
        :param deck: the deck of cards
        :return: updated list of cards on hand, deck of cards and the points of cards on hand
        """
        calc_class = Calculation()
        points = calc_class.point_calc(my_cards)
        results = [my_cards, deck, points]
        while points <= 16:
            results = super().player_hit(my_cards, deck)
            points = results[2]

        return results


if __name__ == "__main__":
    mydeck = Deck()
    print(mydeck.deck_cards())

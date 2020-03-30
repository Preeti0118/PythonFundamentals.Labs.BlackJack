# This program will import the classes module
# And use the classes and function from the import module to run the game
import blackjack_class


# Call the function to create a shuffled deck of 52 cards
def create_deck():
    """
    creates a shuffled deck of cards
    :return: shuffled deck of 52 cards
    """
    deck_cls = blackjack_class.Deck()
    deck = deck_cls.deck_cards()
    return deck


# Deal the cards to the player and the dealer
def gameplay():
    """
    this is the main game program for black jack. It distributes 2 cards each to the player and the dealer
    and asks the dealer to decide to Hit or Stand.
    Based on players response it calculates the points and decides the winner based on blackjack game rules
    :return: None
    """

    deck = create_deck()
    deal_cls = blackjack_class.Deal()
    result = deal_cls.deal_cards(deck)
    player_hand = []
    dealer_hand = []
    player_hand = result[0]
    dealer_hand = result[1]
    deck = result[2]

    # Calculate the players points and dealers points

    calc_cls = blackjack_class.Calculation()
    player_point = calc_cls.point_calc(player_hand)
    dealer_point = calc_cls.point_calc(dealer_hand)

    # print(player_hand, player_point)
    # print(dealer_hand)

    print("Player -  this is your hand - ")
    print(player_hand)
    print('These are your points - ' + str(player_point))
    print('These are dealers cards - ' + dealer_hand[0] + ' and 1 Hidden card')

    game_continue = True

    if player_point == 21:
        print('Player Wins, Dealer Loses')
        game_continue = False

    player_cls = blackjack_class.Player()
    dealer_cls = blackjack_class.Dealer()

    while game_continue:
        # Ask the player to Hit or Stand
        player_decision = input('Do you want to H:Hit or S:Stand ? - ')
#        player_decision.upper()
        if player_decision.upper() in ['H', 'HIT']:
            player_result = player_cls.player_hit(player_hand, deck)
            player_hand = player_result[0]
            deck = player_result[1]
            player_point = player_result[2]

            if player_point == 21:
                print('Player Wins, Dealer Loses')
                game_continue = False
            elif player_point > 21:
                print('Player Loses, Dealer Wins')
                game_continue = False
            print("player -  this is your hand - ")
            print(player_hand)
            print('These are player points - ' + str(player_point))

        else:
            dealer_result = dealer_cls.dealer_hit(dealer_hand, deck)
            dealer_hand = dealer_result[0]
            deck = dealer_result[1]
            dealer_point = dealer_result[2]

            if dealer_point == 21:
                print('Dealer Wins')
            elif dealer_point > 21:
                print('Dealer Loses, Player Wins')
            elif player_point > dealer_point:
                print('Player Wins, Dealer Loses')
            elif dealer_point > player_point:
                print('Dealer Wins, Player Loses')
            else:
                print('Game Draw')
            game_continue = False

    print("player -  this is your hand - ")
    print(player_hand)
    print('These are players points - ' + str(player_point))

    print('These are dealers cards - ')
    print(dealer_hand)
    print('These are Dealers Points - ' + str(dealer_point))




if __name__ == '__main__':
    gameplay()

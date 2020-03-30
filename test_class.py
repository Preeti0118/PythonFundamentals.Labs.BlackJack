import unittest
import blackjack_class


class TestDeck(unittest.TestCase):
    def test_deckcards(self):

        """
        This test case tests function deck_cards of class Deck.
        It returns the list of 52 shuffled deck of cards..

        :return: None
        """
        expected_list = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            ]
        testing_class = blackjack_class.Deck()
        self.assertEqual(testing_class.deck_cards().sort(), expected_list.sort())

    def test_dealcards(self):

        """
        This test case tests function deal_cards of class Deal.
        It checks if the result contains three lists and it also checks the length of each list.

        :return: None
        """
        deck = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            ]

        test_class = blackjack_class.Deal()
        num_cards = test_class.deal_cards(deck)
        self.assertEqual(len(num_cards), 3)
        self.assertEqual(len(num_cards[0]),2)
        self.assertEqual(len(num_cards[1]),2)
        self.assertEqual(len(num_cards[2]),48)

    def test_pointcalc(self):

        """
        This test case tests function point_calc of class Calculation.
        It checks if the result contains the calculation of cards and give total points.

        :return: None
        """
        lst = ['SA', 'D2', 'HT', 'S9']
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 22)

        lst = ['HA', "D2", 'HJ']
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 13)

        lst = ['SA', 'HA', "DA"]
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 13)

    def test_playerhit(self):

        """
        This test case tests function player_hit of class Player.
        It checks if the result contains three lists after player say Hit.The first list contains number of cards in
        player hand, second list contains the number of cards left in the deck and third list contains total points of
        players hand.

        :return: None
        """
        deck = [
            'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
        ]

        player_deck = ['HA', 'H2', ]

        test_class = blackjack_class.Player()
        result = test_class.player_hit(player_deck,deck)
        self.assertEqual(len(result[0]),3)
        self.assertEqual(len(result[1]),47)
        self.assertEqual(result[2],18)

    def test_dealerhit(self):

        """
        This test case tests function dealer_hit of class Dealer.
        It checks if the result contains three lists after dealer say Hit.The first list contains number of cards in
        dealer hand, second list contains the number of cards left in the deck and the third list contains total points
        of dealers hand. It tests both the scenarios if the dealer has less than 16 points or more than 16 points in hand.

        :return:
        """
        deck = [
            'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
        ]

        dealer_deck = ['HA', 'H2', ]

        test_class = blackjack_class.Dealer()
        result = test_class.dealer_hit(dealer_deck,deck)
        self.assertEqual(len(result[0]),3)
        self.assertEqual(len(result[1]),47)
        self.assertEqual(result[2],18)

        deck = [
            'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
        ]
        result =[]
        dealer_deck = ['HJ', 'HK', ]

        test_class = blackjack_class.Dealer()
        result = test_class.dealer_hit(dealer_deck,deck)
        self.assertEqual(len(result[0]),2)
        self.assertEqual(len(result[1]),48)
        self.assertEqual(result[2],20)

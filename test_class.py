import unittest
import blackjack_class


class TestDeck(unittest.TestCase):
    def test_deckcards(self):
        expected_list = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            ]
        testing_class = blackjack_class.Deck()
        self.assertEqual(testing_class.deck_cards().sort(), expected_list.sort())

    def test_dealcards(self):
        deck = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            ]

        test_class = blackjack_class.Deal()
        num_cards = test_class.deal_cards(deck)
        self.assertEqual(len(num_cards), 2)

    def test_pointcalc(self):
        lst = ['S4', 'DT']
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 14)

        lst = ['HA', "DA", 'HJ']
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 12)

        lst = ['SA', 'HA', "DA"]
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 13)

    def test_playerhit(self):
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

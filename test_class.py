import unittest
import blackjack_class


class TestDeck(unittest.TestCase):
    def test_deckcards(self):
        expected_list = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            ]
        testing_class = blackjack_class.Deck()
        self.assertEqual(testing_class.deck_cards().sort(), expected_list.sort())

    def test_dealcards(self):
        deck = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            ]

        test_class = blackjack_class.Deal()
        num_cards = test_class.deal_cards(deck)
        self.assertEqual(len(num_cards), 2)

    def test_pointcalc(self):
        lst = ['S7', 'HA', "DJ"]
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 18)

        lst = ['SA', 'HA', "DJ"]
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 12)

        lst = ['S1', 'HA', "D5"]
        test_class = blackjack_class.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 17)
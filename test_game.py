import unittest
import blackjack_gameloop


class TestGame(unittest.TestCase):
    def test_deckcards(self):

        """
        This test case tests function deck_cards.
        It returns the list of 52 shuffled deck of cards..

        :return:
        """
        expected_list = [
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
        ]
        deck = blackjack_gameloop.create_deck()
        deck.sort()
        expected_list.sort()
        self.assertEqual(deck, expected_list)
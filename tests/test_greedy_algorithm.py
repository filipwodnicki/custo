from unittest import TestCase

from algorithms.greedy import greedy_algorithm
from custo.board import Board


class TestGreedyAlgorithm(TestCase):
    def test_greedy_algorithm(self):

        # Example 1
        # items = [450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261]
        # material size = 2050.

        expected_board_1_items = [450, 444, 436, 430, 261]
        expected_board_1_space = 29.0
        expected_board_2_items = [389, 389, 386, 375, 362]
        expected_board_2_space = 149.0
        expected_board_3_items = [362, 261, 261]
        expected_board_3_space = 1166.0

        # compute
        a = greedy_algorithm([450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261], 2050.)

        result_board_1_items = a[0].items
        result_board_1_space = a[0].space_remaining
        result_board_2_items = a[1].items
        result_board_2_space = a[1].space_remaining
        result_board_3_items = a[2].items
        result_board_3_space = a[2].space_remaining

        self.assertIsInstance(a, list)
        self.assertIsInstance(a[0], Board)
        self.assertTrue(len(a) == 3)

        self.assertEqual(result_board_1_items, expected_board_1_items)
        self.assertEqual(result_board_1_space, expected_board_1_space)
        self.assertEqual(result_board_2_items, expected_board_2_items)
        self.assertEqual(result_board_2_space, expected_board_2_space)
        self.assertEqual(result_board_3_items, expected_board_3_items)
        self.assertEqual(result_board_3_space, expected_board_3_space)

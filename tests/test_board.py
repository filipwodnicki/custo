import unittest
from unittest import TestCase

from custo.board import Board


class TestBoard(TestCase):

    # test "insert" Class method
    def test_insert(self):

        # Test for proper type o insert
        a = Board(2050.)

        self.assertRaises(Exception, a.insert, 'car')  # assert string fails

        self.assertRaises(Exception, a.insert, [0, 1, 2])  # assert [] fails

        try:
            a.insert(100)    # assert int OK
        except TypeError:
            self.fail("insert() raised TypeError unexpectedly!")

        try:
            a.insert(100.0)    # assert float OK
        except TypeError:
            self.fail("insert() raised TypeError unexpectedly!")

        # Test that you can't insert something big. (max board size = 2050)
        b = Board(2050.)

        with self.assertRaises(ValueError):
            b.insert(1000)
            b.insert(1000)
            b.insert(51)

        b2 = Board(2050.)

        self.assertRaises(ValueError, b2.insert, 2051)

        # Test space remaining works as planned
        c = Board(2050.)

        c.insert(100)

        self.assertEqual(c.space_remaining, 1950)

        c.insert(850)

        self.assertEqual(c.space_remaining, 1100)

    # test "remove" Class method
    def test_remove(self):

        b = Board(2050.)
        b.insert(50)

        # assert can't remove something that doesn't exist
        self.assertRaises(Exception, b.remove, 100)
        # assert space remaining works correctly
        self.assertEqual(b.space_remaining, 2000)

        b.remove(50)

        # assert can't remove something that was recently removed
        self.assertRaises(Exception, b.remove, 50)
        # assert space remaining works correctly
        self.assertEqual(b.space_remaining, 2050)

if __name__ == '__main__':
    unittest.main()

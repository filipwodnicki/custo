import unittest
from unittest import TestCase

from custo import Board, BoardCollection


class TestBoard(TestCase):

    # test "insert" Class method
    def test_insert(self):

        # Test for proper type to insert
        a = Board(2050.)

        self.assertRaises(Exception, a.insert, 'car')  # assert string fails

        self.assertRaises(Exception, a.insert, [0, 1, 2])  # assert [] fails

        self.assertTrue(a.insert, 100.0)

        self.assertRaises(TypeError, a.insert, "banana")

        # Test that you can't insert something big. (max board size = 2050)
        b = Board(2050.)

        self.assertIsNone(b.insert(1000))  # default return type for Board.insert() is None
        self.assertIsNone(b.insert(1000))
        self.assertRaises(ValueError, b.insert, 51)

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


class TestBoardCollection(TestCase):
    def test_num_boards(self):
        a = BoardCollection()

        b1 = Board(1000)
        b1.insert(500)
        b2 = Board(1000)
        b2.insert(200)
        b2.insert(200)

        a.append(b1)
        a.append(b2)

        self.assertEquals(a.num_boards, 2)

        a = BoardCollection()

        self.assertEquals(a.num_boards, 0)

    def test_append(self):
        a = BoardCollection()

        b1 = Board(1000)
        b1.insert(500)
        b2 = Board(1000)
        b2.insert(200)
        b2.insert(200)
        b3 = "Board"

        a.append(b1)
        self.assertEquals(a.contents, [b1])
        a.append(b2)
        self.assertEquals(a.contents, [b1, b2])
        self.assertRaises(TypeError, a.append, b3)

    def test_last(self):
        a = BoardCollection()
        self.assertFalse(a.last)

        b1 = Board(1000)
        b1.insert(500)
        a.append(b1)
        self.assertEqual(a.last.items, [500])

        b2 = Board(1000)
        b2.insert(200)
        a.append(b2)
        self.assertEqual(a.last.items, [200])

if __name__ == '__main__':
    unittest.main()

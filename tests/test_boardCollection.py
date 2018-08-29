from unittest import TestCase

from custo.board import Board
from custo.board import BoardCollection


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


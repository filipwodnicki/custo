class Board(object):
    """Board is single unit of calculation

    Boards have items, Boards are initialized with a length,
    and Boards keep a running total of the space_remaining."""

    def __init__(self, material_size):
        self.board_length = material_size
        self.items = list()
        self.space_remaining = self.board_length

    def insert(self, piece_length):
        """Add a item to the Board"""
        if self.space_remaining >= piece_length:
            self.items.append(piece_length)
            self.space_remaining -= piece_length
        else:
            raise ValueError('piece of length too long to be inserted')

    def remove(self, piece_length):
        """Remove an item from the Board"""
        if piece_length in self.items:
            self.items.remove(piece_length)
            self.space_remaining += piece_length
        else:
            raise ValueError('piece not on the Board!')

    def __repr__(self):
        return str('Board with items {}, unused space: {}'.format(self.items, self.space_remaining))

    def __str__(self):
        return str(self.items)


class BoardCollection(object):
    """Represents a collection of Boards, representing the result of calculation

    BoardCollection inializes its contents to []
    num_boards is supported
    append adds a Board to the collection"""

    def __init__(self):
        self.contents = []

    @property
    def num_boards(self):
        """Returns the number of boards in a BoardCollection"""
        return len(self.contents)

    @property
    def last(self):
        """Returns the last Board on a BoardCollection"""
        try:
            if self.contents[-1]:
                return self.contents[-1]
        except IndexError:
            return False

    def append(self, board):
        """Adds a Board at the end of a BoardCollection"""
        if isinstance(board, Board):
            self.contents.append(board)
        else:
            raise TypeError("Only Board can be appended to BoardCollection")


if __name__ == '__main__':
    pass

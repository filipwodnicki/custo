class Board(object):

    def __init__(self, material_size):
        self.board_length = material_size
        self.contents = []
        self.space_remaining = self.board_length

    def insert(self, piece_length):

        if self.space_remaining >= piece_length:
            self.contents.append(piece_length)
            self.space_remaining -= piece_length
        else:
            raise ValueError('piece of length too long to be inserted')

    def remove(self, piece_length):

        if piece_length in self.contents:
            self.contents.remove(piece_length)
            self.space_remaining += piece_length
        else:
            raise ValueError('piece not on the Board!')

    def __repr__(self):
        return str('Board with items {}, unused space: {}'.format(self.contents, self.space_remaining))

    def __str__(self):
        return str ( self.contents )

if __name__ == '__main__':
    a = Board(100)
    print(a)
    a.insert(50)
    print(a)
    a.insert(50)
    print(a)
    a.remove(50)
    print(a)

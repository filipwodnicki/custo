from board import Board, BoardCollection


def greedy_algorithm(pieces, material_size):
    """Implementation of the First-Fit Greedy Algorithm

    Inputs:
    pieces - list[] of items to place optimally
    material_size - length of Boards to cut from, assumes unlimited supply

    Output:
    Optimally laid out BoardCollection.contents, which is a list[] of Boards"""

    bc = BoardCollection()
    bc.append(Board(material_size))

    pieces.sort(reverse=True)  # sort in ascending order

    # we must copy pieces, else our actual list will get modified
    for piece in pieces.copy():

        piece_added = False  # for recording state: did we add this piece to BoardCollection yet?

        # if piece fits, add it on that Board, remove it from the list, mark it as such and break out of for loop
        for board in bc.contents:
            if board.space_remaining >= piece:
                board.insert(piece)
                pieces.remove(piece)
                piece_added = True
                break

        # if it hasn't been added yet, make a new Board and put it there
        if piece_added is False:
            bc.append(Board(material_size))
            bc.last.insert(piece)
            pieces.remove(piece)

    return bc.contents

if __name__ == '__main__':
    print(greedy_algorithm([450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261], 2050.))

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame as p
from Chess import ChessEngine

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  # 400 is another option
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

"""
Initialize a global dictionary of images. This will be called exactly once in the main
"""
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("images/" + piece + ".png"),
            (SQ_SIZE, SQ_SIZE)
        )
    # Note: we can access an image by saying 'IMAGES["wp"]'


"""
The main driver for our code. This will handle user input and updating the graphics
"""
# The main driver for our code. This will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # only do this once, before the while loop
    running = True

    sqSelected = ()  # no square is selected, keep track of last click (row, col)
    playerClicks = []  # keep track of player clicks [(6,4), (4,4)]

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y)
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if sqSelected == (row, col):  # clicked same square twice
                    sqSelected = ()  # deselect
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)

                # after 2nd click
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())  # debug output

                    gs.makeMove(move)

                    sqSelected = ()  # reset
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


# Responsible for all drawing within a current game state
def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


"""
Draw the squares on the board. The top left square is always light.
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board using the current GameState.board
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

















if __name__ == "__main__":
    main()
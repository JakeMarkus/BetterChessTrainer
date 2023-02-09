import chess
from chessboard import display


class Board:

    def __init__(self):
        self.board = chess.Board()
        self.visualizer = display.start(caption="Opening Trainer")

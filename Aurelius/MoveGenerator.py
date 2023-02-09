
from stockfish import Stockfish

class AI:
    def __init__(self):
        self.stockfish = Stockfish(path="C:/Users/jakem/Documents/stockfish/stockfish_windows", depth=15, parameters={"Skill Level": 20, "Hash": 2048})
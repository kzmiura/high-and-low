from Deck import Deck
from PlayingCard import PlayingCard


import pyxel


class CardTable:
    WIDTH = 256 / 2
    HEIGHT = 192 / 2

    def __init__(self) -> None:
        self.stock = Deck()
        self.stock.shuffle()
        self.layout: list[PlayingCard] = []

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.rect((pyxel.width - self.WIDTH) / 2, (pyxel.height - self.HEIGHT) / 4, self.WIDTH, self.HEIGHT, pyxel.COLOR_GREEN)
        for i, card in enumerate(self.layout):
            card.draw(
                (pyxel.width - PlayingCard.WIDTH) / 2 + 32 * (1 - 2 * i),
                (pyxel.height - PlayingCard.HEIGHT) / 3,
            )

    def draw_stock(self) -> None:
        self.layout.append(self.stock.draw_card())
        if len(self.layout) > 2:
            self.layout.pop(0)

    def check_rank(self, guessing_high: bool) -> bool:
        if self.layout[1].rank == self.layout[0].rank:
            return False
        return (self.layout[1].rank > self.layout[0].rank) == guessing_high
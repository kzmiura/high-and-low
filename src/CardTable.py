import pyxel

from Deck import Deck
from PlayingCard import PlayingCard


class CardTable:
    WIDTH = 256 / 2
    HEIGHT = 192 / 2

    def __init__(self) -> None:
        self.stock = Deck()
        self.stock.shuffle()
        self.layout: list[PlayingCard] = []

    def draw(self) -> None:
        pyxel.rect(
            (pyxel.width - self.WIDTH) / 2,
            (pyxel.height - self.HEIGHT) / 4,
            self.WIDTH,
            self.HEIGHT,
            pyxel.COLOR_GREEN
        )
        for i, card in enumerate(self.layout):
            card.draw(
                (pyxel.width - PlayingCard.WIDTH) / 2 + 32 * (1 - 2 * i),
                (pyxel.height - PlayingCard.HEIGHT) / 3,
            )

    def draw_stock(self) -> None:
        drawed_card = self.stock.draw_card()
        self.layout.append(drawed_card)
        if len(self.layout) > 2:
            self.layout.pop(0)

    def is_result_high(self) -> bool:
        return None if self.layout[1] == self.layout[0] else self.layout[1] > self.layout[0]

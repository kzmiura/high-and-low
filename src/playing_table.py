from collections import deque

import pyxel
from deck import Deck
from playing_card import PlayingCard


class PlayingTable:
    def __init__(self) -> None:
        self.width = pyxel.width / 2
        self.height = pyxel.height / 2
        self.deck = Deck()
        self.deck.shuffle()
        self.layouts: deque[PlayingCard] = deque(maxlen=2)
        self.prepare_layout()

    def draw(self) -> None:
        tx = (pyxel.width - self.width) / 2
        ty = (pyxel.height - self.height) / 2
        pyxel.rect(
            tx,
            ty,
            self.width,
            self.height,
            pyxel.COLOR_CYAN,
        )
        for i, card in enumerate(self.layouts):
            card.draw(
                tx + (self.width * (3 / 2 - i) - PlayingCard.WIDTH) / 2,
                ty + (self.height - PlayingCard.HEIGHT) / 2,
            )

    def prepare_layout(self) -> None:
        for _ in range(self.layouts.maxlen):
            self.draw_card()
        self.layouts[0].face_up()

    def draw_card(self) -> None:
        drawn_card = self.deck.draw()
        self.layouts.append(drawn_card)

    def open_layouts(self) -> None:
        for card in self.layouts:
            card.face_up()

    def is_card_higher(self) -> bool:
        """Return whether the guessed card rank is higher than the base card rank.

        Returns:
            bool: True if the guessed card rank is higher than the base card rank, False if not.
            None: If the guessed card rank is the same as the base card rank.

        Raises:
            ValueError: If the number of layouts is not 2.
        """
        if len(self.layouts) != 2:
            raise ValueError("The number of layouts must be 2.")
        base_rank, guessed_rank = (card.rank for card in self.layouts)
        return None if guessed_rank == base_rank else guessed_rank > base_rank

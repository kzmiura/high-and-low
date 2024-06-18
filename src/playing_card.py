import enum
from typing import Optional

import pyxel


class Suit(enum.Enum):
    HEART = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()
    SPADE = enum.auto()


class PlayingCard:
    WIDTH = 48
    HEIGHT = 72

    def __init__(self, rank: int, suit: Suit, reversed: bool = False) -> None:
        if not (isinstance(rank, int) and isinstance(suit, Suit) and isinstance(reversed, bool)):
            raise TypeError
        if not (1 <= rank <= 13):
            raise ValueError(f"Rank must be between 1 and 13 but got {rank}.")

        self.rank = rank
        self.suit = suit
        self.reversed = reversed

    def __str__(self) -> str:
        return "Reversed" if self.reversed else f"{self.rank_to_str()} of {self.suit.name.lower()}"

    def __repr__(self) -> str:
        return f"PlayingCard({self.rank}, {self.suit}, {self.reversed})"

    def draw(self, x, y) -> None:
        if self.reversed:
            pyxel.blt(x, y, pyxel.images[0], 48, 32, 48, 72, pyxel.COLOR_BLACK)
            return

        pyxel.blt(x, y, pyxel.images[0], 0, 32, 48, 72, pyxel.COLOR_BLACK)
        # draw rank
        pyxel.text(
            x + (self.WIDTH - pyxel.FONT_WIDTH) / 2,
            y + (self.HEIGHT - pyxel.FONT_HEIGHT) / 2,
            self.rank_to_str(),
            self.get_color(),
        )
        # draw suit mark
        self.draw_suit_mark(x + 4, y + 4)

    def get_color(self) -> int:
        return pyxel.COLOR_RED if self.suit in (Suit.HEART, Suit.DIAMOND) else pyxel.COLOR_BLACK

    def draw_suit_mark(self, x: int, y: int) -> None:
        u, v = {
            Suit.HEART: (16, 0),
            Suit.DIAMOND: (24, 0),
            Suit.CLUB: (16, 16),
            Suit.SPADE: (24, 16),
        }[self.suit]
        pyxel.blt(x, y, pyxel.images[0], u, v, 8, 16, pyxel.COLOR_WHITE)
        pyxel.blt(x + 8, y, pyxel.images[0], u, v, -8, 16, pyxel.COLOR_WHITE)

    def rank_to_str(self) -> str:
        match self.rank:
            case 1:
                return "A"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case _:
                return str(self.rank)

    def face_up(self) -> None:
        self.reversed = False

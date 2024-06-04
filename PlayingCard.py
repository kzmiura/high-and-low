import enum

import pyxel


class Suit(enum.Enum):
    HEART = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()
    SPADE = enum.auto()


class PlayingCard:
    WIDTH = 48
    HEIGHT = 80

    def __init__(self, suit: Suit, rank: int, reversed: bool = True) -> None:
        if isinstance(suit, Suit) and isinstance(rank, int) and 1 <= rank <= 13 and isinstance(reversed, bool):
            self.suit = suit
            self.rank = rank
            self.color = pyxel.COLOR_RED if suit in (
                Suit.HEART, Suit.DIAMOND) else pyxel.COLOR_BLACK
            self.reversed = reversed
        else:
            raise ValueError("Invalid arguments")

    def __str__(self) -> str:
        return f"{self.rank_to_str():2>} of {self.suit.name}"

    def __repr__(self) -> str:
        return f"PlayingCard({self.suit}, {self.rank})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, PlayingCard):
            raise ValueError("Invalid comparison")
        return self.suit == other.suit and self.rank == other.rank

    def draw(self, x, y) -> None:
        if self.reversed:
            pyxel.blt(x, y, pyxel.images[0], 48, 32, 48, 80, pyxel.COLOR_BLACK)
            return
        pyxel.blt(x, y, pyxel.images[0], 0, 32, 48, 80, pyxel.COLOR_BLACK)
        pyxel.text(x + self.WIDTH / 2, y + self.HEIGHT /
                   2, self.rank_to_str(), self.color)
        self._draw_suit(x + 4, y + 4)

    def _draw_suit(self, x, y) -> None:
        match self.suit:
            case Suit.HEART:
                u, v = 16, 0
            case Suit.DIAMOND:
                u, v = 24, 0
            case Suit.CLUB:
                u, v = 16, 16
            case Suit.SPADE:
                u, v = 24, 16

        pyxel.blt(x, y, pyxel.images[0], u, v, 8, 16, pyxel.COLOR_WHITE)
        pyxel.blt(x + 8, y, pyxel.images[0], u, v, -8, 16, pyxel.COLOR_WHITE)

    def turn_up(self) -> None:
        self.reversed = False

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

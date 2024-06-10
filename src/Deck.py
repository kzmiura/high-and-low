import random

from PlayingCard import PlayingCard, Suit


class Deck:
    def __init__(self) -> None:
        self.cards = [
            PlayingCard(suit, rank) for suit in Suit for rank in range(1, 14)
        ]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> PlayingCard:
        return self.cards.pop()

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self) -> str:
        return "\n".join(map(str, self.cards))

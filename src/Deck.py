import random
from playing_card import PlayingCard, Suit


class Deck:
    def __init__(self) -> None:
        self.cards = [
            PlayingCard(rank, suit, reversed=True) for rank in range(1, 14) for suit in Suit
        ]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> PlayingCard:
        return self.cards.pop()

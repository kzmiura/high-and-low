import pyxel
import enum

from playing_table import PlayingTable


class State(enum.Enum):
    GUESS = enum.auto()
    REVEAL = enum.auto()


class Game:
    def __init__(self) -> None:
        self.is_game_over = False
        self.state = State.GUESS
        self.table = None
        self.score = 0
        self.base_score = 100
        self.score_rate = 1
        self.level = 1
        self.game_start()

    def update(self) -> None:
        match self.state:
            case State.GUESS:
                self.update_guess()
            case State.REVEAL:
                self.update_reveal()

    def draw(self) -> None:
        if self.table is not None:
            self.table.draw()
            self.draw_ui()
        match self.state:
            case State.GUESS:
                self.show_message("Higher or Lower? (H/L)")
            case State.REVEAL:
                self.show_message(
                    "Press Enter to continue",
                    "You " + ("win!" if self.is_win else "lose"),
                )

    def update_guess(self) -> None:
        if pyxel.btnp(pyxel.KEY_H):
            self.check_guess(True)
        elif pyxel.btnp(pyxel.KEY_L):
            self.check_guess(False)
        else:
            return
        self.state = State.REVEAL

    def update_reveal(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.table.draw_card()
            self.state = State.GUESS

    def draw_ui(self) -> None:
        # draw health
        for i in range(self.health):
            pyxel.blt(4 + 20 * i, 4, pyxel.images[0], 16, 0, 8, 16, pyxel.COLOR_WHITE)
            pyxel.blt(4 + 8 + 20 * i, 4, pyxel.images[0], 16, 0, -8, 16, pyxel.COLOR_WHITE)
        
        # draw level, target score, and score
        texts = (
            f"Level : {self.level:>4}",
            f"Target: {self.get_target_score():>4}",
            f"Score : {self.score:>4}",
        )
        for i, text in enumerate(texts):
            pyxel.text(4, 24 + i * pyxel.FONT_HEIGHT, text, pyxel.COLOR_WHITE)

    def game_start(self) -> None:
        self.table = PlayingTable()
        self.health = 3
        self.state = State.GUESS

    def game_over(self) -> None:
        self.is_game_over = True

    def check_guess(self, is_guess_high: bool) -> None:
        self.table.open_layouts()
        is_higher = self.table.is_card_higher()
        self.is_win = False if is_higher is None else is_higher is is_guess_high
        if self.is_win:
            self.score += self.base_score * self.score_rate
            self.check_score()
        else:
            self.health -= 1
            self.check_health()

    def check_score(self) -> None:
        if self.score >= self.get_target_score():
            self.clear_level()

    def get_target_score(self) -> int:
        return sum(((i + 1) * 400 for i in range(self.level)))
    
    def clear_level(self) -> None:

        self.level += 1

    def check_health(self) -> None:
        if self.health <= 0:
            self.game_over()

    def show_message(self, *messages: str) -> None:
        for i, message in enumerate(messages):
            pyxel.text(
                (pyxel.width - len(message) * pyxel.FONT_WIDTH) / 2,
                8 + i * pyxel.FONT_HEIGHT,
                message,
                pyxel.COLOR_WHITE,
            )

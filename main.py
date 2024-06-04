import enum
import pyxel

from CardTable import CardTable


class Scene(enum.Enum):
    TITLE = enum.auto()
    GAME = enum.auto()
    GAME_OVER = enum.auto()


class State(enum.Enum):
    STARTING = enum.auto()
    GUESSING = enum.auto()
    REVEALING = enum.auto()


class App:
    def __init__(self) -> None:
        pyxel.init(256, 192)
        pyxel.load("./my_resource.pyxres")
        self.scene = Scene.TITLE
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        match self.scene:
            case Scene.TITLE:
                self.update_title()
            case Scene.GAME:
                self.update_game()
            case Scene.GAME_OVER:
                self.update_game_over()

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)
        match self.scene:
            case Scene.TITLE:
                self.draw_title()
            case Scene.GAME:
                self.draw_game()
            case Scene.GAME_OVER:
                self.draw_game_over()

    def start(self) -> None:
        self.state = State.STARTING
        self.table = CardTable()

    def update_title(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = Scene.GAME
            self.start()

    def update_game(self) -> None:
        if not self.table.stock:
            self.scene = Scene.GAME_OVER
            return
        match self.state:
            case State.STARTING:
                self.update_starting()
            case State.GUESSING:
                self.update_guessing()
            case State.REVEALING:
                self.update_revealing()

    def update_starting(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.table.draw_stock()
            self.table.draw_stock()
            self.table.layout[0].turn_up()
            self.state = State.GUESSING

    def update_guessing(self) -> None:
        if pyxel.btnp(pyxel.KEY_H):
            self.check_guessing(True)
            self.table.layout[1].turn_up()
            self.state = State.REVEALING
        elif pyxel.btnp(pyxel.KEY_L):
            self.check_guessing(False)
            self.table.layout[1].turn_up()
            self.state = State.REVEALING

    def update_revealing(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.table.draw_stock()
            self.state = State.GUESSING

    def update_game_over(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = Scene.TITLE

    def draw_title(self) -> None:
        self.draw_center("Press Enter to start")

    def draw_game(self) -> None:
        self.table.draw()
        match self.state:
            case State.STARTING:
                self.draw_message("Press Enter to draw a card")
            case State.GUESSING:
                self.draw_message("Higher or Lower?")
            case State.REVEALING:
                self.draw_message("Won!" if self.is_won else "Lose", "Press Enter to continue")

    def draw_game_over(self) -> None:
        self.draw_center("Game Over")
        self.draw_message("Press Enter to return to the title")

    def draw_center(self, title: str) -> None:
        pyxel.text((pyxel.width - 4 * len(title)) / 2, pyxel.height / 2, title, pyxel.COLOR_WHITE)

    def draw_message(self, *message: str) -> None:
        for i, message in enumerate(message):
            pyxel.text((pyxel.width - 4 * len(message)) / 2, 8 * (i + 1), message, pyxel.COLOR_BLACK)

    def check_guessing(self, guessing_high: bool) -> None:
        self.is_won = self.table.check_rank(guessing_high)


if __name__ == "__main__":
    App()

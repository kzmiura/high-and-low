import enum
import pyxel

from game import Game


class Scene(enum.Enum):
    TITLE = enum.auto()
    GAME = enum.auto()
    GAME_OVER = enum.auto()


class App:
    def __init__(self) -> None:
        pyxel.init(256, 192, "High and Low")
        pyxel.load("../res/my_resource.pyxres")
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
        match self.scene:
            case Scene.TITLE:
                self.draw_title()
            case Scene.GAME:
                self.draw_game()
            case Scene.GAME_OVER:
                self.draw_game_over()

    def update_title(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.start_game()

    def draw_title(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)
        for i, text in enumerate(("High and Low", "Press Enter to start")):
            pyxel.text(
                (pyxel.width - len(text) * pyxel.FONT_WIDTH) / 2,
                (pyxel.height - 2 * pyxel.FONT_HEIGHT) /
                2 + i * pyxel.FONT_HEIGHT,
                text,
                pyxel.COLOR_WHITE,
            )

    def update_game(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)
        if self.game.is_game_over:
            self.scene = Scene.GAME_OVER
        self.game.update()

    def draw_game(self) -> None:
        self.game.draw()

    def update_game_over(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.return_title()

    def draw_game_over(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)
        for i, text in enumerate(("Game Over", "Press Enter to return")):
            pyxel.text(
                (pyxel.width - len(text) * pyxel.FONT_WIDTH) / 2,
                (pyxel.height - 2 * pyxel.FONT_HEIGHT) /
                2 + i * pyxel.FONT_HEIGHT,
                text,
                pyxel.COLOR_WHITE,
            )

    def start_game(self) -> None:
        self.game = Game()
        self.scene = Scene.GAME

    def return_title(self) -> None:
        self.scene = Scene.TITLE


if __name__ == "__main__":
    App()

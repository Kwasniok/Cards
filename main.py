from gui.application import Application
from gui.window import Window


def main():
    application = Application()
    win = Window(application, title="Game", x=100, y=100, width=500, height=500)
    application.run()
    application.quit()


if __name__ == "__main__":
    main()

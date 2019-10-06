from game.game_application import Game_Application


def main():
    application = Game_Application()
    application.run()
    application.destroy()


if __name__ == "__main__":
    main()

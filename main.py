import window


def main():
    screen = window.Window()
    screen.render([
        "#   1",
        "##   2",
        "###   3",
        "#1",
        "##2",
        "###3",
        "",
        "Hello world",
        "",
        "> What color is purple?",
        "-Xander 2023",
        "",
        "=> https://xkcd.com/ xkcd webcomic",
        "",
        "* List element 1",
        "* Item 2",
        "* I'm a third item",
        "```",
        "print(\"Hello, world!\")",
        "return 0",
        "```",
    ])
    screen.mainloop()


if __name__ == "__main__":
    main()

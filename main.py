import window


def main():
    screen = window.Window()
    with open("test.gmi", "r") as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line][:-1]
        print(lines)
        f.close()

    screen.render(lines)
    screen.mainloop()


if __name__ == "__main__":
    main()

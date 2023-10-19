import tkinter
# from tkinter.constants import N, NE, E, SE, S, SW, W, NW, TOP
from tkinter.constants import *

import settings


class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.configure(background="orange")
        self.root.title(settings.title)
        self.root.geometry(settings.size)
        self.preformatted = False
        self.scrollbar = tkinter.Scrollbar(self.root, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side=RIGHT, anchor=E, fill=BOTH)
        self.view = tkinter.Frame(self.root, bg="red")
        self.view.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)
        self.textlines = []
        # self.root.mainloop()

    def mainloop(self):
        self.root.mainloop()

    def render(self, content: list[str]):
        for line in content:
            if line:
                if not self.preformatted:
                    if line[:2] == "=>":
                        self.textlines.append(tkinter.Label(self.view, text=f"=⇒ {line.split(maxsplit=2)[2]} ({line.split(maxsplit=2)[1]})"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(f"=⇒ {line.split(maxsplit=2)[2]} ({line.split(maxsplit=2)[1]})")
                    elif line[:3] == "```":
                        self.preformatted = True
                    elif line[0] == "#" and not line[1] == "#":
                        self.textlines.append(tkinter.Label(self.view, text=f"Heading 1: {line[1:].lstrip()}"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(f"Heading 1: {line[1:].lstrip()}")
                    elif line[0:2] == "##" and not line[2] == "#":
                        self.textlines.append(tkinter.Label(self.view, text=f"Heading 2: {line[2:].lstrip()}"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(f"Heading 2: {line[2:].lstrip()}")
                    elif line[0:3] == "###" and not line[3] == "#":
                        self.textlines.append(tkinter.Label(self.view, text=f"Heading 3: {line[3:].lstrip()}"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(f"Heading 3: {line[3:].lstrip()}")
                    elif line[0] == "*" and line[1].isspace():
                        self.textlines.append(tkinter.Label(self.view, text=f"• {line.split(maxsplit=1)[1]}"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(f"• {line.split(maxsplit=1)[1]}")
                    else:
                        self.textlines.append(tkinter.Label(self.view, text=f"{line}"))
                        self.textlines[-1].pack(side=TOP, anchor='w')
                        print(line)
                elif line[:3] == "```":
                    self.preformatted = False
                else:
                    self.textlines.append(tkinter.Label(self.view, text=f"Code: {line}"))
                    self.textlines[-1].pack(side=TOP, anchor='w')
                    print(f"Code: {line}")
            else:
                self.textlines.append(tkinter.Label(self.view, text=f"{line}"))
                self.textlines[-1].pack(side=TOP, anchor='w')
                print(line)

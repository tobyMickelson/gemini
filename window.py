import tkinter
# from tkinter.constants import N, NE, E, SE, S, SW, W, NW, TOP
from tkinter.constants import *

import settings


class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(settings.title)
        self.root.geometry(settings.size)

        self.scrollable = tkinter.Canvas(self.root, highlightthickness=0)
        self.scrollbar = tkinter.Scrollbar(self.root, orient=VERTICAL, command=self.scrollable.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollable.pack(side=LEFT, fill=BOTH, expand=True)
        self.view = tkinter.Text(self.scrollable)
        self.view.configure(state="disabled")
        self.scrollable.bind("<Configure>", lambda event: (
            self.scrollable.configure(scrollregion=self.scrollable.bbox("all"))
        ))
        self.scrollable.create_window((0, 0), window=self.view, anchor="nw")
        self.scrollable.configure(yscrollcommand=self.scrollbar.set)

        self.preformatted = False
        self.textlines = []
        # self.root.mainloop()

    def mainloop(self):
        self.root.mainloop()

    def render(self, content: list[str]):
        self.view.configure(state="normal")
        line_num = '0'
        for line in content:
            if line:
                if not self.preformatted:
                    if line[:2] == "=>":
                        self.view.insert(END, f"=⇒ {line.split(maxsplit=2)[2]} ({line.split(maxsplit=2)[1]})\n")
                        # TODO: Link formatting
                    elif line[:3] == "```":
                        self.preformatted = True
                    elif line[0] == "#" and not line[1] == "#":
                        self.view.insert(END, f"{line[1:].lstrip()}\n")
                        self.view.tag_add("h1", f"{line_num}.0", f"{line_num}.end")
                    elif line[0:2] == "##" and not line[2] == "#":
                        self.view.insert(END, f"{line[2:].lstrip()}\n")
                        self.view.tag_add("h2", f"{line_num}.0", f"{line_num}.end")
                    elif line[0:3] == "###" and not line[3] == "#":
                        self.view.insert(END, f"{line[3:].lstrip()}\n")
                        self.view.tag_add("h3", f"{line_num}.0", f"{line_num}.end")
                    elif line[0] == "*" and line[1].isspace():
                        self.view.insert(END, f"• {line[1:].lstrip()}\n")
                        self.view.tag_add("list", f"{line_num}.0", f"{line_num}.end")
                    else:
                        self.view.insert(END, f"{line}\n")
                        self.view.tag_add("plain", f"{line_num}.0", f"{line_num}.end")
                elif line[:3] == "```":
                    self.preformatted = False
                else:
                    self.view.insert(END, f"{line}\n")
                    self.view.tag_add("preformatted", f"{line_num}.0", f"{line_num}.end")
            else:
                self.view.insert(END, f"{line}\n")
                self.view.tag_add("plain", f"{line_num}.0", f"{line_num}.end")

            line_num = str(int(line_num) + 1)

        self.view.tag_configure("plain", font=settings.font_plain)
        self.view.tag_configure("h1", font=settings.font_h1)
        self.view.tag_configure("h2", font=settings.font_h2)
        self.view.tag_configure("h3", font=settings.font_h3)
        self.view.tag_configure("list", font=settings.font_list)
        self.view.tag_configure("preformatted", font=settings.font_preformatted)
        self.view.configure(state="disabled")

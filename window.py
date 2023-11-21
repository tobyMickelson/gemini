import tkinter
# from tkinter.constants import N, NE, E, SE, S, SW, W, NW, TOP
from tkinter.constants import *
from time import sleep

import settings


class PreformattedBlock:
    def __init__(self, view):
        self.outer = view
        self.frame = tkinter.Frame(background="#CCC")
        self.window = self.outer.view.window_create(END, window=self.frame)
        self.view = tkinter.Text(self.frame, font=settings.font_preformatted, background="#CCC")
        self.scrollbar = tkinter.Scrollbar(self.frame, orient=HORIZONTAL, command=self.view.xview)
        self.view.configure(xscrollcommand=self.scrollbar.set)
        self.view.pack(fill=BOTH, expand=TRUE, side=TOP, anchor=N)
        self.scrollbar.pack(fill=BOTH, expand=TRUE, side=BOTTOM, anchor=S)
        self.lines = "0"

    def set_size(self):
        self.view.configure(height=int(self.view.index('end').split('.')[0]) - 2)


class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(settings.title)
        self.root.geometry(settings.size)

        self.view = tkinter.Text(self.root)
        self.scrollbar = tkinter.Scrollbar(self.root, orient=VERTICAL, command=self.view.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.view.configure(yscrollcommand=self.scrollbar.set, state="disabled")
        self.view.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.preformatted = False
        self.preformatted_blocks = []
        self.textlines = []
        # self.root.mainloop()

    def mainloop(self):
        while True:
            for preformatted in self.preformatted_blocks:
                preformatted.frame.configure(width=self.root.winfo_width() - self.scrollbar.winfo_width() - 10)
            self.root.update_idletasks()
            self.root.update()
            sleep(1/30)

    def render(self, content: list[str]):
        self.view.configure(state="normal")
        self.line_num = "1"
        for line in content:
            added = False
            printed = False
            print(self.line_num)
            if line:
                if not self.preformatted:
                    if line[0] == "#" and not line[1] == "#":
                        self.view.insert(END, f"{line[1:].lstrip()}\n")
                        self.view.tag_add("h1", f"{self.line_num}.0", f"{self.line_num}.end")
                        added = True
                        printed = True
                    if line[0:2] == "##" and not line[2] == "#":
                        self.view.insert(END, f"{line[2:].lstrip()}\n")
                        self.view.tag_add("h2", f"{self.line_num}.0", f"{self.line_num}.end")
                        added = True
                        printed = True
                    if line[0:3] == "###" and not line[3] == "#":
                        self.view.insert(END, f"{line[3:].lstrip()}\n")
                        self.view.tag_add("h3", f"{self.line_num}.0", f"{self.line_num}.end")
                        added = True
                        printed = True
                    if line[:2] == "=>":
                        self.view.insert(END, f"=⇒ {line.split(maxsplit=2)[2]} ({line.split(maxsplit=2)[1]})\n")
                        self.view.tag_add("link", f"{self.line_num}.0", f"{self.line_num}.end")
                        added = True
                        printed = True
                    if line[:3] == "```":
                        self.preformatted = True
                        self.preformatted_blocks.append(PreformattedBlock(self))
                        code_start = str(int(self.line_num))
                        added = True
                    if line[0] == "*" and line[1].isspace():
                        self.view.insert(END, f"• {line[1:].lstrip()}\n")
                        self.view.tag_add("list", f"{self.line_num}.0", f"{self.line_num}.end")
                        added = True
                        printed = True
                    if not added:
                        self.view.insert(END, f"{line}\n")
                        self.view.tag_add("plain", f"{self.line_num}.0", f"{self.line_num}.end")
                        printed = True
                elif line[:3] == "```" and self.preformatted and not added:
                    self.preformatted = False
                    self.preformatted_blocks[-1].set_size()
                elif not line[:3] == "```" and self.preformatted and not added:
                    self.preformatted_blocks[-1].view.insert(END, f"{line}\n")
                else:
                    self.view.insert(END, f"{line}\n")
                    printed = True
            else:
                self.view.insert(END, f"{line}\n")
                self.view.tag_add("plain", f"{self.line_num}.0", f"{self.line_num}.end")
                printed = True

            if printed:
                self.line_num = str(int(self.line_num) + 1)

        self.view.tag_configure("plain", font=settings.font_plain)
        self.view.tag_configure("h1", font=settings.font_h1, spacing3=settings.spacing3_h1)
        self.view.tag_configure("h2", font=settings.font_h2, spacing3=settings.spacing3_h2)
        self.view.tag_configure("h3", font=settings.font_h3, spacing3=settings.spacing3_h3)
        self.view.tag_configure("list", font=settings.font_list)
        self.view.tag_configure("preformatted", font=settings.font_preformatted, background="#CCC")
        self.view.configure(state="disabled")

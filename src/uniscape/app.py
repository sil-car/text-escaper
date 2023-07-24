# $ python3 -c 'import uniscape.cli; uniscape.cli.main()' [ARGS]

import sys
from pathlib import Path

from tkinter import font
from tkinter import Tk
from tkinter import Text

from tkinter.ttk import Button
from tkinter.ttk import Frame
from tkinter.ttk import Label
from tkinter.ttk import Scrollbar
from tkinter.ttk import Style

from . import cli
from .esc import wordlist_to_unicode

class UniScapeWindow(Frame):
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)

        # Set general mainframe properties.
        self.config(padding=(1, 1, 1, 1))
        self.grid(row=0, column=0, sticky='nwes')

        # Make each mainframe widget expand proportionally to initial size.
        gw1 = 8 # proportional width of 1st grid block
        gw2 = 1 
        gw3 = 1
        gh1 = 1 # proportional height of 1st grid block
        gh2 = 5
        for i in range(gw1+1):
            self.columnconfigure(i, weight=gw1)
        for i in range(gw1+1, gw1+gw2+gw3+1):
            self.columnconfigure(i, weight=gw2)
        for i in range(gh1+1):
            self.rowconfigure(i, weight=gh1)
        for i in range(gh1+1, gh1+gh2+1):
            self.rowconfigure(i, weight=gh2)

        # Define top row.
        self.t_input = Text(self,
            width=40,
            height=gh1,
            wrap="word",
            highlightthickness=0,
            font=root.font,
        )
        sv_input = Scrollbar(self,
            orient='vertical',
            command=self.t_input.yview
        )
        self.t_input.config(yscrollcommand=sv_input.set)
        btn = Button(self,
            text="Enter",
            command=self.update_output
        )

        # Define bottom row.
        self.t_output = Text(self,
            width=40,
            height=gh2,
            wrap="word",
            state='disabled',
        )
        sv_output = Scrollbar(self,
            orient='vertical',
            command=self.t_output.yview
        )
        self.t_output.config(yscrollcommand=sv_output.set)

        # Place widgets.
        self.t_input.grid(
            column=0,
            row=0,
            columnspan=gw1,
            rowspan=gh1,
            sticky='nwes'
        )
        sv_input.grid(
            column=gw1,
            row=0,
            rowspan=gh1,
            columnspan=gw2,
            sticky='nws'
        )
        btn.grid(
            column=gw1+gw2,
            row=0,
            rowspan=gh1,
            columnspan=gw3,
            sticky='nwes'
        )
        self.t_output.grid(
            column=0,
            row=gh1,
            columnspan=gw1,
            rowspan=gh2,
            sticky='nwes'
        )
        sv_output.grid(
            column=gw1,
            row=gh1,
            columnspan=gw2,
            rowspan=gh2,
            sticky='nws'
        )

        # Set focus.
        self.t_input.focus()

        # Define callbacks.
        root.bind("<Return>", self.update_output)
        root.bind("<Control-Key-a>", self.handle_ctrl_a)
        root.bind("<Control-Key-A>", self.handle_ctrl_a) # in case of caps lock

    def update_output(self, *args):
        self.t_output.config(state='normal')
        self.t_input.delete('end-1c') # remove final newline
        self.t_output.delete('1.0', 'end') # empty previous output
        self.t_output.insert('1.0', wordlist_to_unicode(self.t_input.get('1.0', 'end').split()))
        self.t_output.config(state='disabled')

    def handle_ctrl_a(self, event):
        self.t_input.tag_add('sel', '1.0', 'end')   # make selection
        self.t_input.mark_set('insert', 'end')      # create marker at end
        self.t_input.see('insert')                  # move cursor to marker
        return 'break'

class UniScapeApp(Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        parent_dir = Path(__file__).parent
        # Set the theme.
        self.th = 'alt' # ok: alt default # no: clam classic
        # self.font = 'DejaVuSansMono' # diacritics don't combine
        # self.font = 'TkFixedFont' # diacritics don't combine
        # self.font = 'DejaVuSans' # works, but not monospaced
        # self.font = font.Font(family="FreeMono") # extra spaces after comined diacritics
        # self.font = 'NotoSansMono-Regular' # works
        # self.font = 'UbuntuSansMono-Regular' # works
        self.font = str(parent_dir / 'UbuntuMono-R.ttf')
        s = Style()
        s.theme_use(self.th)

        # Set root parameters.
        self.w = 500
        self.h = 125
        self.geometry(f"{self.w}x{self.h}")
        self.title("UniScape")
        self.minsize(self.w, self.h)
        # self.resizable(False, False)

        # Make root widget's outer border expand with window.
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


def main():
    if len(sys.argv) > 1:
        cli.main()
        return
    classname = "Uniscape"
    root = UniScapeApp(className=classname)
    UniScapeWindow(root, class_=classname)
    root.mainloop()

if __name__ == '__main__':
    main()

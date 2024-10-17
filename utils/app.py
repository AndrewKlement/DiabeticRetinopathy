from .settings import *
import tkinter
import pywinstyles, sys
import sv_ttk

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title(title)        
        self.geometry(f"{width}x{height}")
        self.iconbitmap(icon_path)
        sv_ttk.set_theme(theme=theme)
        self.apply_theme_to_titlebar()

    def apply_theme_to_titlebar(self):
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            # Set the title bar color to the background color on Windows 11 for better appearance
            pywinstyles.change_header_color(self, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(self, "dark" if sv_ttk.get_theme() == "dark" else "normal")

            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)

    
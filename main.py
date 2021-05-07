#!/usr/bin/env python3

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo

from pencere import *



if __name__ == "__main__":
    win = ClipboardWindow()
    win.connect("destroy", win.destroy_func)
    win.show_all()
    Gtk.main()
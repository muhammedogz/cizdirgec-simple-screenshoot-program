from __future__ import division
import gi
import os
import math

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo

import cizim_alani



if __name__ == "__main__":
    win = ClipboardWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
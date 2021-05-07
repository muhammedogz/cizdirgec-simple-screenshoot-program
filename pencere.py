from __future__ import division
import gi
import os
import math

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo

import cizim_alani

class ClipboardWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cizdirgec")

        self.box = Gtk.Box()
        grid = Gtk.Grid()
        

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.entry = Gtk.Entry()
        self.image = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)

        button_kirp = Gtk.Button(label="Cizdirgec")
        button_temizle = Gtk.Button(label="Temizle")
        button_kaydet = Gtk.Button(label="Kaydet")

        grid.attach(self.image, 0, 1, 1, 1)
        grid.attach(button_kirp, 2, 1, 1, 1)
        grid.attach(button_temizle, 2, 2, 1, 1)
        grid.attach(button_kaydet, 2, 3, 1, 1)

        button_kirp.connect("clicked", self.yapistir_fonk)
        button_temizle.connect("clicked", self.temizle_fonk)
        button_kaydet.connect("clicked", self.kaydet_fonk)
        
        self.flag = True
        self.box.add(grid)
        
        self.add(self.box)

    def yapistir_fonk(self, widget):
        os.system("xfce4-screenshooter -c --region")
        image = self.clipboard.wait_for_image()
        if image is not None:
            # self.image.set_from_pixbuf(image)
            image.savev("temp.png", "png", (), ())
            if self.flag == True:
                self.frame = PaintArea()
                self.frame.set_shadow_type(Gtk.ShadowType.IN)
                self.box.add(self.frame)
                self.flag = False
            else:
                self.box.remove(self.frame)
                self.frame = PaintArea()
                self.frame.set_shadow_type(Gtk.ShadowType.IN)
                self.box.add(self.frame)
            self.show_all()
            # self.image2.write_to_png("sa.png")
       
    def temizle_fonk(self, widget):
        self.frame.temizle(widget)

    def kaydet_fonk(self, widget):
        self.frame.surface.write_to_png("kaydedildi.png")

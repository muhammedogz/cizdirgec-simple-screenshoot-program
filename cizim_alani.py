import gi
import os
from pencere import *

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo



class PaintArea(Gtk.Frame):
    def __init__(self, css=None, border_width=0):
        super().__init__()
        self.set_border_width(border_width)
        self.set_size_request(500, 500)
        self.vexpand = True
        self.hexpand = True
        self.surface = None

        
        self.da = Gtk.DrawingArea()
        self.da.set_size_request(100,100)
        self.add(self.da)

        self.da.connect('draw',self.draw_cb)
        self.da.connect('configure-event',self.configure_event_cb)

        self.da.connect('motion-notify-event',self.motion_notify_event_cb)
        self.da.connect('button-press-event',self.button_press_event_cb)
        self.da.set_events(self.da.get_events() | Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.POINTER_MOTION_MASK)


        # cr = cairo.Context(surface)


    def clear_surface(self):
        filename = "temp.png"
        self.surface = cairo.ImageSurface.create_from_png(filename)
        if self.surface is None:
            w, h = self.surface.get_width(), self.surface.get_height()

            res = cairo.ImageSurface(cairo.FORMAT_ARGB32, 
            w, h)
        # self.set_size_request(w, h)
            cr = cairo.Context(res)
            cr.mask_surface(self.surface,0,0)
        #cr.set_source_rgb(1,1,1)
            cr.fill()
            cr.paint()

            del cr
    
    def configure_event_cb(self, widget, event):
        if self.surface is not None:
            del self.surface
            self.surface = None
        win = widget.get_window()
        width = widget.get_allocated_width()
        height = widget.get_allocated_height()
        
        self.surface = win.create_similar_surface(
            cairo.CONTENT_COLOR,
            width,
            height)

        self.clear_surface()
        return True
        



    def draw_cb(self, widget ,cr):

        if self.surface is None:
            return False

        cr.set_source_surface(self.surface,0,0)
        cr.paint()
        return False


    def draw_brush(self, widget, x, y):

        cr = cairo.Context(self.surface)
        cr.set_source_rgb(5,0,0)
        cr.rectangle(x-3,y-3,6,6)
        cr.fill()
        del cr

        widget.queue_draw_area(x-3,y-3,10,10)
        


    def button_press_event_cb(self, widget, event):


        if self.surface is None:
            return False

    
        if event.button == Gdk.BUTTON_PRIMARY:
            self.draw_brush(widget, event.x, event.y)
        elif event.button == Gdk.BUTTON_SECONDARY:
            self.clear_surface()
            widget.queue_draw()

        return True
        
    def temizle(self, widget):
        self.clear_surface()
        widget.queue_draw()

    def motion_notify_event_cb(self, widget, event):

        if self.surface is None:
            return False

        if event.state & Gdk.EventMask.BUTTON_PRESS_MASK:
            self.draw_brush(widget , event.x, event.y)

        return True
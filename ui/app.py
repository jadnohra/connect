import sys
import os
import threading
import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock
from .movable_widget import MovableWidget


class _MainWindow(MovableWidget):
    def __init__(self):
        super().__init__()

    def update(self, dt):
        super().update()
        with self.canvas:
            self.canvas.clear()
            Color([1,1,1])
            Line(points=[0, 0, 1000, 1000], width=2, cap='none')
            Line(ellipse=[0, 0, 400,200], width=2, cap='none')


class ConnectViewerApp(App):
    def __init__(self):
        def input_threading():
            while True:
                cmd = sys.stdin.readline().strip()
        super().__init__()
        self.window = None
        thread = threading.Thread(target=input_threading)
        thread.daemon = True
        thread.start()

    def build(self):
        self.window = _MainWindow()
        # self.window.add_widget(Slider(min=-100, max=100, value=25))
        Clock.schedule_interval(self.window.update, 1.0/10.0)
        return self.window


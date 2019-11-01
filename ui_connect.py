import sys
import os
import threading
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.uix.slider import Slider
from kivy.graphics import Scale, Translate, LoadIdentity, Color, Line, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock

kivy.require('1.11.1')


class _ConnectViewerMainWindow(Widget):
    class CanvasMover():

        TRANSLATE, SCALE = range(2)

        def __init__(self, widget):
            self.widget = widget
            self.mode = self.TRANSLATE
            self.active_mode = self.mode
            self.total_scale = 1.0
            self.scale = 1.0
            self.switch(False)
            self._keyboard = Window.request_keyboard(
                None, self.widget, 'text')
            self._keyboard.bind(on_key_down=self._on_key_down,
                                on_key_up=self._on_key_up)

        def switch(self, on):
            if not on:
                self.total_scale = self.total_scale * self.scale
                self.active_mode = self.mode
                self.translation = [0, 0]
                self.translation_diff = [0, 0]
                self.scale = 1.0
                self.scale_ratio = 1.0

        def move(self, touch):
            print(touch)
            if self.mode == self.TRANSLATE:
                target_transl = [(touch.pos[x] - touch.opos[x])
                                 / self.total_scale for x in [0, 1]]
                self.translation_diff = [target_transl[x]
                                         - self.translation[x] for x in [0, 1]]
            else:
                target_scale = (touch.pos[1] - touch.opos[1]) * 0.01
                self.scale_ratio = max(0.5, 1.0 + target_scale / self.scale)

        def update(self):
            with self.widget.canvas.before:
                LoadIdentity()
                if self.mode == self.TRANSLATE:
                    self.widget.g_translate = Translate(*self.translation_diff)
                    self.translation = [self.translation[x]
                                        + self.translation_diff[x]
                                        for x in [0, 1]
                                        ]
                    self.translation_diff = [0, 0]
                else:
                    self.widget.g_scale = Scale(self.scale_ratio)
                    self.scale = self.scale * self.scale_ratio
                    self.scale_ratio = 1.0

        def _on_key_down(self, keyboard, keycode, text, modifiers):
            if keycode[1] in ['lctrl', 'rctrl']:
                self.mode = self.SCALE

        def _on_key_up(self, keyboard, keycode):
            if keycode[1] in ['lctrl', 'rctrl']:
                self.mode = self.TRANSLATE

    def __init__(self):
        super(_ConnectViewerMainWindow, self).__init__()
        self._canvas_mover = self.CanvasMover(self)

    def update(self, dt):
        self._canvas_mover.update()
        with self.canvas:
            self.canvas.clear()
            Color([1,1,1])
            Line(points=[0, 0, 1000, 1000], width=2, cap='none')
            Line(ellipse=[0, 0, 400,200], width=2, cap='none')

    def on_touch_up(self, touch):
        self._canvas_mover.switch(False)

    def on_touch_move(self, touch):
        self._canvas_mover.switch(True)
        self._canvas_mover.move(touch)


class _ConnectViewerApp(App):

    def __init__(self):
        def input_threading():
            while True:
                cmd = sys.stdin.readline().strip()
        super(_ConnectViewerApp, self).__init__()
        self.window = None
        thread = threading.Thread(target=input_threading)
        thread.daemon = True
        thread.start()

    def build(self):
        self.window = _ConnectViewerMainWindow()
        # self.window.add_widget(Slider(min=-100, max=100, value=25))
        Clock.schedule_interval(self.window.update, 1.0/10.0)
        return self.window


if __name__ == '__main__':
    # Example: python road_viewer_app -- --dbg
    g_dbg = '--dbg' in sys.argv
    _ConnectViewerApp().run()

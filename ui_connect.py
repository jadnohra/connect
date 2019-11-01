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

kivy.require('1.0.8')


class _RoadViewerMainWindow(Widget):
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
                None, self, 'text')
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
            if keycode[1] == 'alt':
                self.mode = self.SCALE

        def _on_key_up(self, keyboard, keycode):
            if keycode[1] == 'alt':
                self.mode = self.TRANSLATE

    def __init__(self):
        super(_RoadViewerMainWindow, self).__init__()
        self.road_file = None
        self._canvas_mover = self.CanvasMover(self)

    def set_file(self, road_file=None):
        self.road_file = road_file
        self.road = None
        self.file_stamp = None

    def update(self, dt):
        '''
        if self.road_file is None:
            return
        file_stamp = os.stat(self.road_file).st_mtime
        if file_stamp != self.file_stamp:
            self.file_stamp = file_stamp
            self.road = road.Road()
            self.road.load_file(self.road_file)
        '''
        self._canvas_mover.update()
        with self.canvas:
            self.canvas.clear()
            # road_render.draw_road_kivy(self.road, self.canvas)
            Color([1,1,1])
            Line(points=[0, 0, 1000, 1000], width=2, cap='none')
            Line(ellipse=[0, 0, 400,200],
                 width=2, cap='none')

    def on_touch_up(self, touch):
        self._canvas_mover.switch(False)

    def on_touch_move(self, touch):
        if self.road is not None:
            self._canvas_mover.switch(True)
            self._canvas_mover.move(touch)


class _RoadViewerApp(App):

    def __init__(self, road_file=None):
        def input_threading():
            while True:
                cmd = sys.stdin.readline().strip()
                self.window.set_file(cmd)
        super(_RoadViewerApp, self).__init__()
        self.road_file = road_file
        self.window = None
        thread = threading.Thread(target=input_threading)
        thread.daemon = True
        thread.start()

    def build(self):
        self.window = _RoadViewerMainWindow()
        self.window.set_file(self.road_file)
        # self.window.add_widget(Slider(min=-100, max=100, value=25))
        Clock.schedule_interval(self.window.update, 1.0/10.0)
        return self.window


if __name__ == '__main__':
    # Note, Kivy has the annoyance that to pass user command line params,
    # one should first add the empty argument '--'.
    # Example: python road_viewer_app -- --file test_road.txt
    g_dbg = '--dbg' in sys.argv
    road_file = (sys.argv[sys.argv.index('--file')+1]
                 if '--file' in sys.argv else None)
    _RoadViewerApp(road_file).run()

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Scale, Translate, LoadIdentity

class MovableWidget(Widget):
    def __init__(self):
        super().__init__()
        self._total_scale = 1.0
        self._scale_ratio = 1.0
        self._switch(False)
        self._keyboard = Window.request_keyboard(
            None, self, 'text')
        self._keyboard.bind(on_key_down=self._on_key_down,
                            on_key_up=self._on_key_up)

    def update(self):
        with self.canvas.before:
            LoadIdentity()
            self.g_translate = Translate(*self._translation_diff)
            self._translation = [self._translation[x]
                                + self._translation_diff[x]
                                for x in [0, 1]
                                ]
            self._translation_diff = [0, 0]
            self.g_scale = Scale(self._scale_ratio)
            self._total_scale = self._total_scale * self._scale_ratio
            self._scale_ratio = 1.0

    def _switch(self, on):
        if not on:
            self._translation = [0, 0]
            self._translation_diff = [0, 0]

    def _move(self, touch):
        target_transl = [(touch.pos[x] - touch.opos[x])
                         / self._total_scale for x in [0, 1]]
        self._translation_diff = [target_transl[x]
                                 - self._translation[x] for x in [0, 1]]
                
    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        self._switch(False)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        self._switch(True)
        self._move(touch)

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self._scale_ratio = 0.75
            elif touch.button == 'scrollup':
                self._scale_ratio = 1.25
                
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'alt':
            self.mode = self.SCALE

    def _on_key_up(self, keyboard, keycode):
        if keycode[1] == 'r':
            self._translation_diff = [-x for x in self._translation]
            self._scale_ratio = 1.0 / self._total_scale
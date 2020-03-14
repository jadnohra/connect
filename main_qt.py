import argparse
from PyQt5.QtWidgets import  QApplication, QTreeWidget, QTreeWidgetItem
from core.core import load_db

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




class MathTextLabel(QTreeWidgetItem):

    def __init__(self, mathText, parent=None, **kwargs):
        super(QTreeWidgetItem, self).__init__(parent, **kwargs)

        l=QVBoxLayout(self)
        l.setContentsMargins(0,0,0,0)

        r,g,b,a=self.palette().base().color().getRgbF()

        self._figure=Figure(edgecolor=(r,g,b), facecolor=(r,g,b))
        self._canvas=FigureCanvas(self._figure)
        l.addWidget(self._canvas)
        self._figure.clear()
        text=self._figure.suptitle(
            mathText,
            x=0.0,
            y=1.0,
            horizontalalignment='left',
            verticalalignment='top',
            size=QtGui.QFont().pointSize()*2
        )
        self._canvas.draw()

        (x0,y0),(x1,y1)=text.get_window_extent().get_points()
        w=x1-x0; h=y1-y0

        self._figure.set_size_inches(w/80, h/80)
        self.setFixedSize(w,h)

class ViewTree(QTreeWidget):
    def __init__(self, value):
        super().__init__()
        def fill_item(item, value):
            def new_item(parent, text, val=None):
                if val is not None or True:
                    child = QTreeWidgetItem([text])
                else:
                    child = MathTextLabel(text)
                    # https://www.codecogs.com/latex/integration/htmlequations.php
                    # http://www.holoborodko.com/pavel/quicklatex/
                fill_item(child, val)
                parent.addChild(child)
                child.setExpanded(True)
            if value is None: return
            elif isinstance(value, dict):
                for key, val in sorted(value.items()):
                    new_item(item, str(key), val)
            elif isinstance(value, (list, tuple)):
                for val in value:
                    text = (str(val) if not isinstance(val, (dict, list, tuple))
                            else '[%s]' % type(val).__name__)
                    new_item(item, text, val) 
            else:
                new_item(item, str(value))

        fill_item(self.invisibleRootItem(), value)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='The connect .yaml file')
    parser.add_argument('--no_nltk', help='Disable nltk', action='store_true')

    args = parser.parse_args()

    data_source = args.file if args.file else './data/math/.'
    db = load_db(data_source)

    app = QApplication([])
    # Now use a palette to switch to dark colors:
    app.setStyle("Fusion")
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtCore import Qt
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    window = ViewTree(db)
    window.setWindowTitle('connect')
    window.show()
    app.exec_()
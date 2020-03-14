import sys
from ui.app import ConnectViewerApp

if __name__ == '__main__':
    # Example: python road_viewer_app -- --dbg
    g_dbg = '--dbg' in sys.argv
    ConnectViewerApp().run()

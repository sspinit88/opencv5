from capture_manager import CaptureManager
from window_manager import WindowManager
import cv2

class Cameo:
    def __init__(self):
        self._windowManger = WindowManager('Cameo', self.onKeyPress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0),
            self._windowManger,
            True
        )

    def run(self):
        """Run the main loop."""
        self._windowManger.createdWindow()
        while self._windowManger.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                # TODO: Filter the frame
                pass
            self._captureManager.exitFrame()
            self._windowManger.processEvent()

    def onKeyPress(self, keycode):
        """Handle a keypress.
            space -> Take a screenshot.
            tab -> Start / stop recording a screencast.
            escape -> Quit.
        """
        if keycode == 32: # Space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManger.destroyWindow()

if __name__ == "__main__":
    Cameo().run();

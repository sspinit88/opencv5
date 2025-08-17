import cv2


class WindowManager():
    def __init__(self, windowName, keyPressCallback = None):
        self.keyPressCallback = keyPressCallback
        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createdWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = bool(self._windowName)

    def show(self, frame):
        cv2.imshow(self._windowName, frame)
    
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvent(self):
        keycode = cv2.waitKey(1)
        if self.keyPressCallback is not None and keycode != -1:
            self.keyPressCallback(keycode)

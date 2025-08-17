import cv2

class MauseEvent:
    """
    Class to handle mouse events for OpenCV windows.

    Attributes:
        clicked (bool): Indicates whether the left mouse button was released.
    """

    def __init__(self):
        """
        Initializes the MauseEvent instance.
        Sets the clicked attribute to False.
        """
        self.clicked = False

    def onMouse(self, event, x, y, flags, param) -> None:
        """
        Mouse callback function to be used with OpenCV windows.

        Args:
            event: The type of mouse event (e.g., cv2.EVENT_LBUTTONUP).
            x: The x-coordinate of the mouse event.
            y: The y-coordinate of the mouse event.
            flags: Any relevant flags passed by OpenCV.
            param: Additional parameters supplied by OpenCV.

        Sets the clicked attribute to True when the left mouse button is released.
        """
        if event == cv2.EVENT_LBUTTONUP:
            self.clicked = True

    def isClicked(self):
        """
        Returns whether the left mouse button has been released.

        Returns:
            bool: True if the left mouse button was released, False otherwise.
        """
        return self.clicked
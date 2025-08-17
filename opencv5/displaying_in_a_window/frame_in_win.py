import cv2
from mouse_event import MauseEvent

# Name of the window to display the camera feed
nameOfWindow = 'Frame in Window HA-HA!'

# Message to display in the console
msg = 'Showing camera feed. Click window or press any key to stop.'

# Create an instance of the mouse event handler
mouse = MauseEvent()

# Open the default camera (usually the first webcam)
cameraCapture = cv2.VideoCapture(0)

# Create a named window for display
cv2.namedWindow(nameOfWindow)

# Set the mouse callback for the window to handle mouse events
cv2.setMouseCallback(nameOfWindow, mouse.onMouse)

print(msg)

# Read the first frame from the camera
success, frame = cameraCapture.read()

# Main loop: display frames until a key is pressed or the window is clicked
while success and cv2.waitKey(1) == -1 and not mouse.isClicked():
    cv2.imshow(nameOfWindow, frame)
    success, frame = cameraCapture.read()

# Destroy the window and release the camera resource
cv2.destroyWindow(nameOfWindow)
cameraCapture.release()
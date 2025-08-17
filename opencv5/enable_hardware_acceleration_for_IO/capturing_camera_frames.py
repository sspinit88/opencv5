import cv2

outputFile = 'output-from-camera.avi'
cameraCapture = cv2.VideoCapture(0) # With gstreamer gst-plugins-base gst-plugins-base-libs gst-plugins-good
# cameraCapture = cv2.VideoCapture(0, cv2.CAP_ANY)
# cameraCapture = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not cameraCapture.isOpened():
    print("Camera not opened!")
    exit()

fps = 30  # An assumption
frameWidth = int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (frameWidth, frameHeight)

videoWriter = cv2.VideoWriter(
    outputFile,
    cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps,
    size
)

success, frame = cameraCapture.read()
print("Capture success:", success, "Shape:", frame.shape if success else None)

numFramesRemaining = 10 * fps - 1  # 10 seconds of frames
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1

import cv2 as cv

srcVideoFile = 'sample_1280x720_surfing_with_audio.avi'
outputVideoFile = 'output.avi'

### CPU only
videoCapture = cv.VideoCapture(srcVideoFile)

### OpenCV will try to use GPU acceleration on supported systems
# videoCapture = cv.VideoCapture(
#     srcVideoFile,
#     cv.CAP_ANY,
#     [
#         cv.CAP_PROP_HW_ACCELERATION,
#         cv.VIDEO_ACCELERATION_ANY
#     ]
# )

fps = videoCapture.get(cv.CAP_PROP_FPS)
frameWidth = int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH))
frameHeight = int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT))
size = (frameWidth, frameHeight)

videoWriter = cv.VideoWriter(
    outputVideoFile,
    cv.VideoWriter_fourcc('I', '4', '2', '0'),
    fps,
    size
)

success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()



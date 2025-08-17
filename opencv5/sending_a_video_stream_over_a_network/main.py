import cv2
import flask
from mjpeg_generaror import mjpeg_generator

app = flask.Flask(__name__)

@app.route('/')
def stream_from_camera():
    return flask.Response(
        mjpeg_generator(),
        mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        threaded=True)
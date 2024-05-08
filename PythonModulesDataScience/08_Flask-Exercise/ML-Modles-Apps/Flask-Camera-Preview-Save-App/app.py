from flask import Flask, render_template, Response
import cv2
import os


app = Flask(__name__)

camera = cv2.VideoCapture(0)  # Accessing the default camera (usually the built-in webcam)

previewing = True  # Flag to indicate if preview is ongoing
saved_image = None  # Variable to store the saved image path
saved_resized_image = None

def generate_frames():
    while True:
        if previewing:
            success, frame = camera.read()  # Read a frame from the camera
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame as JPEG
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield the frame as a byte stream
        else:
            break

@app.route('/')
def index():
    global previewing
    previewing = True
    return render_template('index.html')

@app.route('/Preview')
def preview():
    global previewing
    previewing = True
    return render_template('index.html')

@app.route('/Save')
def predict():
    global previewing, saved_image,saved_resized_image
    previewing = False
    success, frame = camera.read()  # Capture a frame from the camera
    if success:
        cv2.imwrite('static/saved_image.jpg', frame)  # Save the captured frame as 'saved_image.jpg'
        saved_image = 'static/saved_image.jpg'
        frame_resized = cv2.resize(frame, (224, 224))
        cv2.imwrite('static/saved_resized_image.jpg', frame_resized)
        saved_resized_image = 'static/saved_resized_image.jpg'
        
        
    return render_template('result.html', saved_image=saved_image)
    

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)


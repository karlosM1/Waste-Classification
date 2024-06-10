import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import base64
import cv2
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

model = tf.keras.models.load_model('wasteCLS.h5')
class_names = ['Organic', 'Recyclable']
confidence_threshold = 0.5

class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    predicted_class = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ImageData {self.id}>"

def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array_with_batch = np.expand_dims(img_array, axis=0)
    return img_array_with_batch

def draw_bounding_box(image, trash_class, confidence):
    image = np.array(image)
    x1, y1, x2, y2 = 10, 10, image.shape[1]-10, image.shape[0]-10  # Dummy bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = f'{trash_class}: {confidence*100:.2f}%'
    cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return Image.fromarray(image)

@app.route('/', methods=['GET'])
def home():
    return render_template('homes.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            image = Image.open(file)
            input_image = preprocess_image(image)
            detections = model.predict(input_image)
            max_confidence = np.max(detections[0])
            if max_confidence < confidence_threshold:
                predicted_class = "Unknown class"
            else:
                predicted_class_index = np.argmax(detections[0])
                predicted_class = class_names[predicted_class_index]
            detected_image = draw_bounding_box(image.copy(), predicted_class, max_confidence)

            # Convert the image to base64 string
            buffered = io.BytesIO()
            detected_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            # Save to database
            new_image = ImageData(image=img_str, predicted_class=predicted_class)
            db.session.add(new_image)
            db.session.commit()

            return redirect(url_for('result'))
    return render_template('index.html')


@app.route('/result')
def result():
    images = ImageData.query.order_by(ImageData.timestamp.desc()).all()
    return render_template('result.html', images=images)

@app.route('/camera', methods=['GET'])
def camera():
    return render_template('camera.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('camera'))
    if file:
        image = Image.open(file)
        input_image = preprocess_image(image)
        detections = model.predict(input_image)
        max_confidence = np.max(detections[0])
        if max_confidence < confidence_threshold:
            predicted_class = "Unknown class"
        else:
            predicted_class_index = np.argmax(detections[0])
            predicted_class = class_names[predicted_class_index]
        detected_image = draw_bounding_box(image.copy(), predicted_class, max_confidence)

        # Convert the image to base64 string
        buffered = io.BytesIO()
        detected_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Save to database
        new_image = ImageData(image=img_str, predicted_class=predicted_class)
        db.session.add(new_image)
        db.session.commit()

        return redirect(url_for('result'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

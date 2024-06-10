# Waste-Classification and Detection Web Application
This web application classifies waste images into either "Organic" or "Recyclable" categories using a pre-trained TensorFlow model. It also draws a bounding box around the detected waste and displays the confidence level of the classification. The application stores the images along with their predicted classes in a SQLite database.

# Features
Upload an image to classify as either "Organic" or "Recyclable".
Draw bounding boxes around the detected waste in the image.
Display the confidence level of the classification.
Save classified images and their predicted classes in a database.
View a history of all classified images with their predicted classes and timestamps.

# Requirements
Python 3.x
Flask
Flask-SQLAlchemy
Pillow
NumPy
TensorFlow
OpenCV-Python

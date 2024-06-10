# Waste-Classification and Detection Web Application
This web application classifies waste images into either "Organic" or "Recyclable" categories using a pre-trained TensorFlow model. It also draws a bounding box around the detected waste and displays the confidence level of the classification. The application stores the images along with their predicted classes in a SQLite database.

# Features
Upload an image to classify as either "Organic" or "Recyclable".
Draw bounding boxes around the detected waste in the image.
Display the confidence level of the classification.
Save classified images and their predicted classes in a database.
View a history of all classified images with their predicted classes and timestamps.

# Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Pillow
- NumPy
- TensorFlow
- OpenCV-Python

# Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd <repository-directory>
2. Install the Required Packages
Install the necessary Python packages using pip.
pip install -r requirements.txt
Ensure that requirements.txt includes the following packages:
- Flask
- Flask-SQLAlchemy
- Pillow
- numpy
- tensorflow
- opencv-python
3. Load the TensorFlow Model
Ensure the TensorFlow model (wasteCLS.h5) is in the same directory as the script.
4. Run the Application
Initialize the database and start the Flask development server.
python app.py
5. Access the Application
Open a web browser and navigate to http://127.0.0.1:5000/ to access the application.
6. Application Structure
app.py: The main application script containing routes and logic for image classification and storage.
templates/: Directory containing HTML templates for the web pages.
- homes.html: Home page.
- index.html: Page for uploading images to classify.
- result.html: Page displaying the results of classified images.
- camera.html: Page for uploading images from a camera (placeholder).
- static/: Directory for static files like CSS and JavaScript.

# Database Schema
ImageData Table:
1. id (Integer, Primary Key): Unique identifier for each record.
2. image (Text): Base64 encoded string of the classified image.
3. predicted_class (String): Predicted class of the image ("Organic" or "Recyclable").
4. timestamp (DateTime): Timestamp of when the image was classified.
# Image Processing
- Preprocess Image: Convert the image to RGB, resize to 224x224 pixels, and normalize pixel values.
- Prediction: Use the TensorFlow model to predict the class of the image.
- Draw Bounding Box: Draw a bounding box around the detected waste and label it with the class and confidence level.
- Save to Database: Convert the image with the bounding box to a base64 string and save it along with the predicted class in the database.

# Contact
For any issues or contributions, please create an issue or pull request on the repository.

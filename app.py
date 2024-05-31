import streamlit as st_lit
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image

# Load the trained model
model = load_model('ASL_Model.h5')
letter_predicted = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']


# Function to preprocess and predict image
def predict_image(image):
    # Preprocess the image (adjust this part based on your preprocessing steps)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (28, 28))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)

    # Predict
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    confidence = predictions[0][predicted_class]

    return letter_predicted[predicted_class], confidence


# Stream_lit app
def main():
    st_lit.set_page_config(page_title="ASL Sign Language Recognition", page_icon=":v:")
    st_lit.title("ASL Sign Language Recognition")

    st_lit.write("Upload an image or use your webcam to capture a picture.")

    # Choose between webcam and file upload
    option = st_lit.radio("", ("Upload Image", "Use Webcam"))

    if option == "Upload Image":
        # File uploader
        uploaded_file = st_lit.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="fileUploader")

        if uploaded_file is not None:
            # Read and display the image
            image = np.array(Image.open(uploaded_file))
            st_lit.image(image, caption="Uploaded Image", use_column_width=True)

            # Predict
            if st_lit.button("Predict", key="predictButton"):
                prediction, confidence = predict_image(image)
                st_lit.success(f"Predicted character: {prediction}")
                st_lit.success(f"Confidence: {confidence * 100:.2f}%")

    elif option == "Use Webcam":
        # Webcam capture
        st_lit.warning("Camera access required. Click 'Allow' in your browser.")
        run_camera = st_lit.checkbox("Run Webcam", key="runWebcam")

        if run_camera:

            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                st_lit.error("Unable to access the camera. Please check your camera settings.")
                return

            _, frame = cap.read()
            st_lit.image(frame, caption="Webcam", channels="BGR", use_column_width=True)

            # Predict on captured image
            if st_lit.button("Predict", key="predictWebcam"):
                prediction, confidence = predict_image(frame)
                st_lit.success(f"Predicted character: {prediction}")
                st_lit.success(f"Confidence: {confidence * 100:.2f}%")


if __name__ == "__main__":
    main()

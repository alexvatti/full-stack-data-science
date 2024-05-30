import streamlit as st
from PIL import Image
import numpy as np
from tensorflow import keras
from keras.models import Sequential

def predict_image(file_Image):
    class_names = ['top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    image_path = file_Image
    gray_image = Image.open(image_path).convert('L')
    gray_array = np.array(gray_image)

    print("Original image shape:", gray_array.shape) # (height,width)

    image_resized = gray_image.resize((28, 28))
    image_scaled = np.array(image_resized)


    print("Resized image shape:", image_scaled.shape) # (height,width)

    # Convert image to float32 and normalize
    image_scaled = image_scaled.astype('float32') / 255.0

    # Reshape the image to match the model input shape
    image_scaled_final = np.expand_dims(image_scaled, axis=0)

    # Make prediction using the model
    loaded_ann_model = keras.models.load_model('fashion-ann.h5')
    predict_value = loaded_ann_model.predict(image_scaled_final)

    # Get the index of the class with the highest probability
    value = np.argmax(predict_value)

    print("Predicted class:", class_names[value])
    return value, class_names[value]

st.title("Fashion - ANN - MODEL")

uploaded_file = st.file_uploader("Choose a image file",type=["png","jpg","jpeg"])
if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.write(img)
    button=st.button("Predict")
    if button:
        index,class_label=predict_image(uploaded_file)
        st.markdown (f"# Class Index:  {index}")
        st.markdown(f"# Class Label: {class_label}")


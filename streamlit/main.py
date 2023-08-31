import requests
import streamlit as st
from PIL import Image
import torch
from torchvision import transforms as T
import numpy as np
import os
from config import DEFAULT_CONFIDENCE_THRESHOLD, DEFAULT_IoU_THRESHOLD


# suppress warnings
st.set_option("deprecation.showfileUploaderEncoding", False)

# define a device and load the model
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


@st.cache(allow_output_mutation=True)
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='streamlit/weights/best.pt', force_reload=True) 
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()


# @st.cache
# def load_image(img):
#     im = Image.open(img)
#     return im

model.eval()
model.conf = DEFAULT_CONFIDENCE_THRESHOLD  # NMS confidence threshold
model.iou = DEFAULT_IoU_THRESHOLD  # NMS IoU threshold

st.title("Grass object detection app")

# displays a file uploader widget

# with st.form("my-form"):
#     uploaded_files = st.file_uploader(label="Choose an image (jpg, jpeg, png)", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
#     submitted = st.form_submit_button("Delete uploaded files")
uploaded_files = st.file_uploader(label="Choose an image (jpg, jpeg, png)", accept_multiple_files=True, type=["jpg", "png", "jpeg"])

# make a batch out of the uploaded images
imgs = [Image.open(image) for image in uploaded_files]

def show_image(image, caption, labels):
    st.subheader(caption)
    st.image(image, width=640)
    st.write("Labels:")
    st.write(labels)
    st.write('\n')


def save_image(image, name, path):
    file_path = os.path.join(path, name)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(file_path, 'wb') as f:
        image.save(f)


# displays a button
if st.button("Detect objects"):
    if imgs is None: 
        st.write("Please upload an image first")
    else:
        file_names = [uploaded_file.name for uploaded_file in uploaded_files]
        output = model(imgs, size=640)
        images = output.render()
        for i, detected_image in enumerate(images):
            transform = T.ToPILImage()
            img = transform(detected_image)
            image_labels = output.pandas().xyxy[i].groupby('name').agg({'name':'count'}).rename(columns={'name':'number'})
            show_image(img, file_names[i], image_labels)
            save_image(img, file_names[i], 'detected-images')


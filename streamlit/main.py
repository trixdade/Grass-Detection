import requests
import streamlit as st
from PIL import Image
import torch
from torchvision import transforms as T
import numpy as np

from config import DEFAULT_CONFIDENCE_THRESHOLD, DEFAULT_IoU_THRESHOLD


# suppress warnings
st.set_option("deprecation.showfileUploaderEncoding", False)

# define a device and load the model
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


@st.cache(allow_output_mutation=True)
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt') 
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

model.conf = DEFAULT_CONFIDENCE_THRESHOLD  # NMS confidence threshold
model.iou = DEFAULT_IoU_THRESHOLD  # NMS IoU threshold

st.title("Grass object detection app")

# displays a file uploader widget

# with st.form("my-form", clear_on_submit=True):
uploaded_files = st.file_uploader(label="Choose an image (jpg, jpeg, png)", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
# submitted = st.form_submit_button("Delete uploaded files")


# make a batch out of the uploaded images
imgs = [Image.open(image) for image in uploaded_files]


def process_images_batch(images, model):
    model.eval()
    output = model(images, size=640)
    return output

def show_image(image, caption):
    st.subheader(caption)
    st.image(image, width=640)
    st.write('\n\n')

def show_output_images(output, captions):
    images = output.render()
    for i, detected_image in enumerate(images):
        transform = T.ToPILImage()
        img = transform(detected_image)
        show_image(img, captions[i])


# displays a button
if st.button("Detect objects"):
    if imgs is None: 
        st.write("Please upload an image first")
    else:
        file_names = [uploaded_file.name for uploaded_file in uploaded_files]
        output = process_images_batch(imgs, model)
        show_output_images(output, file_names)
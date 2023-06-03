# Grass-Detection

This is a streamlit-based object detection service that was designed to detect different types of plants on the images of grass. The model has been trained to detect 12 different classes, such as:
- Taraxacum Officinale
- Poa Pratensis
- Propleshina (Empty Gap)
- Achillea Millefolium
- Plantago Major
- Potentilla Anserina
- Trifolium Pratense
- Poa Trivialis
- Glechoma Hederacea
- Musor (Garbage)
- Ranunculus Repens
- Dry Grass

Labeled dataset could be found [here](https://drive.google.com/file/d/1eh7bzooIiVdBBoM57p-CmO5AUNKM0nG1/view?usp=sharing).

## Demo 
![Demo](https://github.com/trixdade/Grass-Detection/blob/main/imgs/demo.gif)


## Run the model
### Python venv
To run the example, run in terminal:
    
    python -m venv .venv
    .venv/Scripts/activate
    pip install -r streamlit/requirements.txt
    streamlit run streamlit/main.py
    
UI will be here http://localhost:8501
    
### Docker
To run the example in a machine running Docker and docker-compose, run in terminal:

    docker-compose build
    docker-compose up
    
To visit the streamlit UI, visit http://localhost:8501



## TO DO
- [x] streamlit service
- [x] show table of labels for each image
- [x] save processed images
- [x] move model to ONNX to speed up on CPU and GPU (2x-3x speed up)
- [ ] add progress bar
- [ ] fastAPI backend
- [ ] Unit testing
- [ ] relabel negative samples in data

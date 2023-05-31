# Grass-Detection

To run the example in a machine running Docker and docker-compose, run:

    docker-compose build
    docker-compose up
    
To visit the streamlit UI, visit http://localhost:8501


### TO DO

- [x] streamlit service
- [x] labels in the second column
- [x] fix ValueError with some images
- [ ] save processed images
- [ ] add progress bar
- [ ] move model to ONNX/OpenVINO to speed up on CPU (2x-3x speed up)
- [ ] move model to TensorRT to speed up on GPU
- [ ] fastAPI backend
- [ ] Unit testing
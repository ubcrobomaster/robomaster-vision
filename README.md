# vision

## Armour Panel Detection

This approach uses a pipeline of computer vision and machine learning algorithms to detect the center of the panels. At a high level, the pipeline goes as follows:
```
1. Preprocess Image
2. Bitmask LEDs
4. Match target LEDs
5. Compute center of panel
```

## Training the model with Keras + Tensorflow 2.0 and performing inference of the model

### Set-up the virtual environment
```
cd vision
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/requirements.txt
```

### Training
```
cd vision/source/panel_finder/
python panel_classifier/ --mode train
```

### Inference
```
cd vision/source
python panel_finder --mode {video/webcam} --video {video_path}
```

## Converting the Keras model to a frozen Tensorflow graph
*Tensorflow 2.0 has no longer supports the freezing of
tensorflow graphs to .pb files. We need to downgrade in order
to do this if we want to use OpenCV DNN*

### Set up Tensorflow 1.14 virtual environment
```
cd vision/requirements
virtualenv -p python3 tf114
source tf114/bin/activate
pip install requirements_convert.txt
```

### Convert 
```
cd source/panel_finder/
python panel_classifier/ --mode convert
```

## Inference (Laptop or Raspberry Pi)

### Virtual Environments

- For Raspberry Pi follow the guide in the raspberrypi_setup directory
- For laptops you can the *venv* virtual environment

### Inference
```
cd vision/source
python panel_finder/ --mode {video/webcam} --vide {video_path} --framework opencv
```

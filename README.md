# Crowd Counting using YOLO

This project implements a crowd counting system using YOLO (You Only Look Once) object detection. It can detect and count people in images or video streams in real-time.

## Features

- Real-time people detection and counting
- Support for both images and video streams
- Bounding box visualization
- Live count display
- Webcam support
- Video file processing with optional output saving

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage with Webcam

Run the following command to start counting people using your webcam:
```bash
python crowd_counter.py
```

### Processing Video Files

To process a video file and save the output:
```python
from crowd_counter import CrowdCounter

counter = CrowdCounter()
counter.process_video('input_video.mp4', 'output_video.mp4')
```

### Processing Single Images

To process a single image:
```python
from crowd_counter import CrowdCounter
import cv2

counter = CrowdCounter()
image = cv2.imread('input_image.jpg')
count, processed_image = counter.count_people(image)
cv2.imshow('Result', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Model

The project uses YOLOv8 by default, which will be automatically downloaded on first run. You can specify a different model by passing the model path to the CrowdCounter constructor:

```python
counter = CrowdCounter(model_path='path/to/your/model.pt')
```

## Performance

- Real-time processing on most modern computers
- Accuracy depends on the YOLO model used
- Performance can be improved by using a GPU

## License

This project is open-source and available under the MIT License. 
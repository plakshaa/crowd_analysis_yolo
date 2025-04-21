# Crowd Counting using YOLO

This project implements a crowd counting system using YOLO (You Only Look Once) object detection. It can detect and count people in images or video streams in real-time.

## Features

- Real-time people detection and counting
- Support for both images and video streams
- Bounding box visualization
- Live count display
- Webcam support
- Video file processing with optional output saving

## Installation Guide for Collaborators

### Prerequisites
- Python 3.8 or higher
- Git
- Webcam (for real-time testing)

### Step 1: Clone the Repository
Open your terminal/command prompt and run:
```bash
git clone https://github.com/plakshaa/crowd_analysis_yolo.git
cd crowd_analysis_yolo
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download YOLO Model
The first time you run the script, it will automatically download the YOLOv8 model. However, if you want to download it manually:
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
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

## Troubleshooting

### Common Issues and Solutions

1. **Webcam not detected**
   - Ensure your webcam is properly connected
   - Check if other applications are using the webcam
   - Try changing the camera index in the code (default is 0)

2. **Dependencies installation fails**
   - Make sure you have the latest pip version: `pip install --upgrade pip`
   - Try installing dependencies one by one
   - Check Python version compatibility

3. **YOLO model download fails**
   - Check your internet connection
   - Try downloading the model manually from the YOLO website
   - Place the model file in the project directory

4. **Performance issues**
   - Reduce the input resolution in the code
   - Use a lighter YOLO model variant
   - Ensure you have sufficient RAM and CPU power

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Open a pull request

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
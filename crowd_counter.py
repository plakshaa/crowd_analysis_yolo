import cv2
import numpy as np
from ultralytics import YOLO

class CrowdCounter:
    def __init__(self, model_path='yolov8n.pt'):
        """
        Initialize the crowd counter with YOLO model
        Args:
            model_path: Path to the YOLO model weights
        """
        self.model = YOLO(model_path)
        self.class_id = 0  # Person class ID in COCO dataset

    def count_people(self, image):
        """
        Count people in the given image
        Args:
            image: Input image (numpy array)
        Returns:
            count: Number of people detected
            annotated_image: Image with bounding boxes and count
        """
        # Run YOLO inference
        results = self.model(image)
        
        # Count people
        count = 0
        for result in results:
            boxes = result.boxes
            for box in boxes:
                if int(box.cls) == self.class_id:  # Check if detected object is a person
                    count += 1
                    # Draw bounding box
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Add count text to image
        cv2.putText(image, f'People Count: {count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return count, image

    def process_video(self, video_path, output_path=None):
        """
        Process a video file and count people in each frame
        Args:
            video_path: Path to input video
            output_path: Path to save output video (optional)
        """
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video file")
            return
        
        # Get video properties
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        # Initialize video writer if output path is provided
        writer = None
        if output_path:
            writer = cv2.VideoWriter(output_path, 
                                   cv2.VideoWriter_fourcc(*'mp4v'),
                                   fps, (width, height))
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame
            count, processed_frame = self.count_people(frame)
            print(f"Frame count: {count}")
            
            # Write frame if output path is provided
            if writer:
                writer.write(processed_frame)
            
            # Display frame
            cv2.imshow('Crowd Counter', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Clean up
        cap.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()

def main():
    # Initialize crowd counter
    counter = CrowdCounter()
    
    # Example usage with webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process frame
        count, processed_frame = counter.count_people(frame)
        print(f"People count: {count}")
        
        # Display frame
        cv2.imshow('Crowd Counter', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 
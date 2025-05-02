
# Image Recognition Chatbot

This project captures images from a webcam, saves them, and uses a pre-trained Mask R-CNN model to detect and label objects in the image. The labels follow the COCO dataset classes.

## Features

- Capture images via webcam using OpenCV.
- Auto-increment file naming for organized image storage.
- Run object detection using a pre-trained `maskrcnn_resnet50_fpn` from PyTorch's torchvision.
- Display detected objects with bounding boxes and class labels.
- Save images with clear folder structure and naming convention.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-recognition-chatbot.git
   cd image-recognition-chatbot
   ```

2. Install required Python packages:
   ```bash
   pip install torch torchvision opencv-python pillow matplotlib
   ```

## Usage

1. Run the main script:
   ```bash
   python your_script_name.py
   ```

2. **Controls:**
   - Press `c` to capture an image.
   - Press `q` to quit.

3. Once an image is captured, the object detection model runs and displays the image with labeled bounding boxes.

## File Structure

```
image-recognition-chatbot/
│
├── captured_images/        # Folder to store captured images
├── your_script_name.py     # Main Python script
└── README.md               # This file
```

## Notes

- Make sure your webcam is connected and accessible.
- Captured images are stored in:  
  `C:/Users/Dhruv Chaudhary/Desktop/image_recognition_chatbot/captured_images/`

- You can change the path in the script if needed.

## Acknowledgements

- [PyTorch](https://pytorch.org/)
- [Torchvision](https://pytorch.org/vision/stable/index.html)
- [COCO Dataset](https://cocodataset.org/#home)

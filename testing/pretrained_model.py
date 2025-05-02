import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load a pretrained Mask R-CNN model
model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set the model to evaluation mode used for output


# Load and preprocess the input image
image_path = "C:/Users/Dhruv Chaudhary/Desktop/image_recognition_chatbot/captured_images/capture_9.jpg"  # Replace with your image path
image = Image.open(image_path).convert("RGB")
image_tensor = F.to_tensor(image).unsqueeze(0)  # Convert image to tensor and add batch dimension

# Perform object detection
with torch.no_grad():
    predictions = model(image_tensor)  # prediction is a list data type whicgh contain boxes ,labels scores masks 

# print(predictions)

# Extract detection results
boxes = predictions[0]["boxes"].cpu().numpy()
labels = predictions[0]["labels"].cpu().numpy()  # Labels correspond to COCO classes
scores = predictions[0]["scores"].cpu().numpy()
masks = predictions[0]["masks"].cpu().numpy()

# Define COCO class labels
COCO_CLASSES = [
    "__background__", "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "N/A", "stop sign", "parking meter", "bench", "bird", "cat", "dog",
    "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "N/A", "backpack", "umbrella",
    "N/A", "N/A", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
    "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "N/A", "wine glass",
    "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "N/A",
    "dining table", "N/A", "N/A", "toilet", "N/A", "TV", "laptop", "mouse", "remote", "keyboard",
    "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "N/A", "book", "clock",
    "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

# Visualize the results
draw = ImageDraw.Draw(image)
for i in range(len(scores)): 
    if scores[i] > 0.6:  # Only consider detections with confidence > 0.1 it will help to detect multiple frames  

        # print(scores[i])    used to print the probalities of the class     
        box = boxes[i]   # Bounding boxes for detected objects
        
        label = COCO_CLASSES[labels[i]] # tell the label
        draw.rectangle(box, outline="red", width=3)
        draw.text((box[0], box[1]), label, fill="red")

  


# Show the image with detected objects
plt.figure(figsize=(12, 8))
plt.imshow(image)
plt.axis("off")
plt.show()




import cv2
import os
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt



def save_image(image, folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
    file_path = os.path.join(folder_path, file_name)  # Create the full path
    cv2.imwrite(file_path, image)  # Save the image using OpenCV
    print(file_path)
    

def address(folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
    file_path = os.path.join(folder_path, file_name)  # Create the full path
    return file_path


def get_next_filename(folder_path, basename):
    # Get the list of files in the folder
    existing_files = os.listdir(folder_path)
    
    # Filter files with the given basename pattern
    existing_files = [f for f in existing_files if f.startswith(basename)]
    
    # If no files exist, start from 1
    if not existing_files:
        return f"{basename}_1.jpg"
    
    # Extract the numbers from the existing filenames and find the max number
    numbers = []
    for file in existing_files:
        # Assume the filename pattern is "basename_number.jpg"
        try:
            number = int(file.split('_')[-1].split('.')[0])  # Extract the number
            numbers.append(number)
        except ValueError:
            continue  # Ignore files that don't match the pattern
    
    # If no valid numbers found, return the first filename
    if not numbers:
        return f"{basename}_1.jpg"
    
    # Find the next number
    next_number = max(numbers) + 1
    file_name= f"{basename}_{next_number}.jpg"
    return file_name

def capture_and_save_images():
    
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'c' to capture an image, or 'q' to quit.")
    basename = "capture"
    folder_path = "C:/Users/Dhruv Chaudhary/Desktop/image_recognition_chatbot/captured_images"

    while True:  # Infinite loop to keep capturing images
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("Error: Could not read frame.")
            break

        # Show the camera feed
        cv2.imshow("Camera Feed", frame)

        # Wait for a key press (1ms for smoother frame updates)
        key = cv2.waitKey(1) & 0xFF  # Wait for 1 ms for a key press

        if key == ord('c'):  # Press 'c' to capture the image
            # Get the next available filename based on the directory content
            new_file = get_next_filename(folder_path, basename)

            # save_image(frame, folder_path, new_file)
            k=address(folder_path, new_file)
            # print(k) 
            save_image(frame, folder_path, new_file)           
            # print(f"{new_file} captured and saved!")
            output(new_file)
           

        elif key == ord('q'):  # Press 'q' to quit
            print("Exiting...")
            cap.release()  # Release the camera
            cv2.destroyAllWindows()  # Close the OpenCV window
            break
            
         


    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the OpenCV window
    
    return new_file


def output(image_name):
        # Load a pretrained Mask R-CNN model
        model = maskrcnn_resnet50_fpn(pretrained=True)
        model.eval()  # Set the model to evaluation mode used for output
        

        # Load and preprocess the input image
        image_path = f"C:/Users/Dhruv Chaudhary/Desktop/image_recognition_chatbot/captured_images/{image_name}"   # Replace with your image path
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


# Run the function to test
# capture_and_save_images() and then process the image

addr=capture_and_save_images()
# print(addr)
# # if addr:
# #     output(addr)
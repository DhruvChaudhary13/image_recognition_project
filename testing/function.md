# def save_image(image, folder_path, file_name):
#     os.makedirs(folder_path, exist_ok=True)  # Ensure the folder exists
#     file_path = os.path.join(folder_path, file_name)  # Create the full path
#     cv2.imwrite(file_path, image)  # Save the image using OpenCV
#     print(f"Image saved at: {file_path}")


# def get_next_filename(folder_path, basename):
#     # Get the list of files in the folder
#     existing_files = os.listdir(folder_path)
    
#     # Filter files with the given basename pattern
#     existing_files = [f for f in existing_files if f.startswith(basename)]
    
#     # If no files exist, start from 1
#     if not existing_files:
#         return f"{basename}_1.jpg"
    
#     # Extract the numbers from the existing filenames and find the max number
#     numbers = []
#     for file in existing_files:
#         # Assume the filename pattern is "basename_number.jpg"
#         try:
#             number = int(file.split('_')[-1].split('.')[0])  # Extract the number
#             numbers.append(number)
#         except ValueError:
#             continue  # Ignore files that don't match the pattern
    
#     # If no valid numbers found, return the first filename
#     if not numbers:
#         return f"{basename}_1.jpg"
    
#     # Find the next number
#     next_number = max(numbers) + 1
#     return f"{basename}_{next_number}.jpg"


# def capture_and_save_images():
#     cap = cv2.VideoCapture(0)  # Open the default camera
#     if not cap.isOpened():
#         print("Error: Could not open camera.")
#         return

#     print("Press 'c' to capture an image, or 'q' to quit.")
#     basename = "capture"
#     folder_path = "captured_images"

#     while True:  # Infinite loop to keep capturing images
#         ret, frame = cap.read()  # Read a frame from the camera
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         # Show the camera feed
#         cv2.imshow("Camera Feed", frame)

#         # Wait for a key press (1ms for smoother frame updates)
#         key = cv2.waitKey(1) & 0xFF  # Wait for 1 ms for a key press

#         if key == ord('c'):  # Press 'c' to capture the image
#             # Get the next available filename based on the directory content
#             new_file = get_next_filename(folder_path, basename)
#             save_image(frame, folder_path, new_file)
#             print(f"{new_file} captured and saved!")
#         elif key == ord('q'):  # Press 'q' to quit
#             print("Exiting...")
#             cap.release()  # Release the camera
#             cv2.destroyAllWindows()  # Close the OpenCV window
#             break

#     cap.release()  # Release the camera
#     cv2.destroyAllWindows()  # Close the OpenCV window

import time
import cv2

# Initialize the webcam video capture
video = cv2.VideoCapture(0)

# Allow the camera sensor time to warm up/initialize
time.sleep(1)

while True:
    # Capture frame-by-frame
    check, frame = video.read()

    # Display the resulting frame in a window
    cv2.imshow("My video", frame)

    # Listen for a key press for 1 millisecond
    key = cv2.waitKey(1)

    # Break the loop if the 'q' key is pressed
    if key == ord("q"):
        break

# Safely close the webcam stream and clean up windows
video.release()
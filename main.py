import cv2
from camera.usb_cam import USBCamera
from plate_detection.detector import PlateDetector
from plate_detection.recognizer import PlateRecognizer
from validation.validator import PlateValidator
from api.client import APIClient
from config.settings import API_URL

def main():
    # Initialize components
    stream_url = "http://192.168.1.11:8080/video"
    camera = USBCamera(stream_url)
    detector = PlateDetector()
    recognizer = PlateRecognizer()
    validator = PlateValidator()
    api_client = APIClient(API_URL)

    print("Starting plate recognition system...")

    # Main loop to continuously monitor for plates
    while True:
        frame = camera.get_frame()
        if frame is None:
            print("Failed to capture frame. Retrying...")
            continue

        # Detect plates in the frame
        plates = detector.detect(frame)
        for plate in plates:
            # Recognize text from the detected plate
            text = recognizer.recognize(plate)
            if text:
                print(f"Detected plate: {text}")
                # Validate the plate format
                if validator.is_valid(text):
                    print(f"Valid plate detected: {text}")
                    # Call the API with the valid plate
                    api_client.register_plate(text)
                else:
                    print(f"Invalid plate format: {text}")

        # Display the frame (optional, for debugging)
        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    # Cleanup
    camera.__del__()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
from camera.usb_cam import USBCamera
from plate_detection.detector import PlateDetector
from plate_detection.recognizer import PlateRecognizer
from api.client import APIClient
from config.settings import API_URL
import argparse


def main(mode):
    # Initialize components
    stream_url = "http://192.168.1.11:8080/video"
    camera = USBCamera(stream_url)
    detector = PlateDetector()
    recognizer = PlateRecognizer()
    api_client = APIClient(API_URL)

    print("Starting plate recognition system...")

    # Main loop to continuously monitor for plates
    while True:
        frame = camera.get_frame()
        if frame is None:
            print("Failed to capture frame. Retrying...")
            continue

        # Display the frame
        cv2.imshow("Camera Feed", frame)
        key = cv2.waitKey(1) & 0xFF

        # Quit if 'q' is pressed
        if key == ord("q"):
            break

        # Production mode: process plates in real-time
        if mode == "prod":
            plates = detector.detect(frame)
            for plate in plates:
                text = recognizer.recognize(plate)
                if text:
                    print(f"Detected plate: {text}")
        # Development mode: process plates only when 'c' is pressed
        elif mode == "dev":
            if key == ord("c"):
                plates = detector.detect(frame)
                for plate in plates:
                    text = recognizer.recognize(plate)
                    if text:
                        print(f"Detected plate: {text}")

    # Cleanup
    camera.__del__()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plate recognition system")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-dev", action="store_true", help="Run in development mode (capture on 'c' key)"
    )
    group.add_argument(
        "-prod", action="store_true", help="Run in production mode (real-time capture)"
    )
    args = parser.parse_args()

    mode = "dev" if args.dev else "prod"
    main(mode)

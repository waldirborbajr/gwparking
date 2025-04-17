import cv2

class USBCamera:
    def __init__(self, device=0):
        self.cap = cv2.VideoCapture(device)
        if not self.cap.isOpened():
            raise ValueError("Unable to open USB camera")
        
        # Set the frame width and height to 640x480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Print the set resolution for verification
        print(f"Set resolution to: {self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Check if the frame size is as expected
            if frame.shape[:2] != (480, 640):
                print(f"Warning: Frame size is {frame.shape[1]}x{frame.shape[0]}, expected 640x480")
            return frame
        return None

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
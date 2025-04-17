import cv2

class PlateDetector:
    def detect(self, frame):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Simple edge detection (replace with a robust model in production)
        edges = cv2.Canny(gray, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        plates = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            # Filter by aspect ratio and size (tune these values)
            if 2 < w / h < 5 and w > 100 and h > 20:
                plate = frame[y:y+h, x:x+w]
                plates.append(plate)
        return plates
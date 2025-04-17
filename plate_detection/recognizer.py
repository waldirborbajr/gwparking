import pytesseract
import cv2

class PlateRecognizer:
    def recognize(self, plate):
        # Preprocess the plate image
        gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Perform OCR
        text = pytesseract.image_to_string(thresh, config='--psm 8').strip()
        # Clean up the text (remove non-alphanumeric characters)
        text = ''.join(c for c in text if c.isalnum()).upper()
        return text if len(text) == 7 else None
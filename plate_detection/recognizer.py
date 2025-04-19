import pytesseract
import cv2


class PlateRecognizer:
    def recognize(self, plate):
        # Preprocess the plate image
        gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Set Tesseract config with whitelist for A-Z and 0-9
        config = (
            "--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        )
        # Perform OCR
        text = pytesseract.image_to_string(thresh, config=config).strip()
        # Filter to only include A-Z and 0-9
        text = "".join(c for c in text if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        # Return text if length is 7, else None
        return text if len(text) == 7 else None

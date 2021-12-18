import cv2


def qrDecode(path):
    de = cv2.QRCodeDetector()
    val, _, _ = de.detectAndDecode(cv2.imread(path))
    return val

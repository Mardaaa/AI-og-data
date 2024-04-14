import cv2
import os

def take_picture():
    cap = cv2.VideoCapture(0) # 0 is webcam index
    
    while(True):
        ret, frame = cap.read() # Capture frame-by-frame
        cv2.imshow('img1', frame)
        key = cv2.waitKey(1)
        if key == ord('y'): # Press 'y' to take a picture
            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_dir, 'image1.png')
            cv2.imwrite(image_path, frame)
            print("Image captured!")
            break
        elif key == 27: # ESC to exit without capturing
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    take_picture()
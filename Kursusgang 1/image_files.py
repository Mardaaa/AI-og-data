import cv2
import os

def take_picture():
    cap = cv2.VideoCapture(0) # 0 is webcam index
    
    while(True):
        _, frame = cap.read() # Capture frame-by-frame
        cv2.imshow('img1', frame)
        key = cv2.waitKey(1)
        if key == ord('y'): # Press 'y' to take a picture
            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_dir, 'image2.png')
            cv2.imwrite(image_path, frame)
            print("Image captured!")
            break
        elif key == 27: # ESC to exit without capturing
            break
    
    cap.release()
    cv2.destroyAllWindows()

def load_picture(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)
    if not os.path.exists(path):
        print("Image doesn't exist")
        print("Make sure you've typed in the correct filename")
    else:
        img = cv2.imread(path)
        cv2.imshow(file_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    take_picture()
    # load_picture('image1.png')
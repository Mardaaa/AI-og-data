import cv2
import os
import random


def load_image(file_name):
    """A function that loads an image based on file name"""
    # Check path for image
    try:
        path = os.path.join(os.path.dirname(__file__), f'{file_name}')
    except FileNotFoundError:
        print("Image was not found")
    
    # If path exists, load the image in cv2
    try:
        image = cv2.imread(path)
        img_resized = cv2.resize(image, (800, 600))
    except cv2.error as e:
        print(f"The error {e} has occured")


    return img_resized


def convert2grayscale(image):
    """A function that converts an image to grayscale"""
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img_gray

def add_noise(image, percentage):
    """A function that adds x-percentage noise to an image"""
    row, col = image.shape
    total_pixels = row * col

    # Calculate number of pixels that needs to be noisy based on percentage
    num_noisy_pixels = int(total_pixels * (percentage / 100))
   
    # Make noise-pixels either black or white
    for i in range(int(num_noisy_pixels)):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        # Alternate between 0 (black) and 255 (white) based on even/odd iteration
        image[y_coord][x_coord] = 0 if i % 2 == 0 else 255

    return image


def apply_mean_filter(image, size):
    """A function that applies an x-sized mean filter to an image """
    img_filtered = cv2.blur(image, (size, size))
    return img_filtered

def apply_median_filter(image, size):
    """A function that applies an x-sized median filter to an image"""
    img_filtered = cv2.medianBlur(image, size)
    return img_filtered

def display_image(image):
    """A simple function that displays an image"""
    cv2.imshow("Image display", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image = load_image('ai_picture.jpg')
    img_gray = convert2grayscale(image)
    img_noise = add_noise(img_gray, 10) # Change percentage

    # img_filtered = apply_mean_filter(img_noise, 3) # Mean filter
    # img_filtered = apply_median_filter(img_noise, 3) # Median filter
    display_image(img_noise)

if __name__ == '__main__':
    main()


import cv2
import os
import random


def load_image(file_name):
    try:
        path = os.path.join(os.path.dirname(__file__), f'{file_name}')
    except FileNotFoundError:
        print("Image was not found")
    
    try:
        image = cv2.imread(path)
        img_resized = cv2.resize(image, (800, 600))
    except cv2.error as e:
        print(f"The error {e} has occured")
    # else:
    #     cv2.imshow("Default image", img_resized)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    return img_resized


def convert2grayscale(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Grayscale image", img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_gray


# Row: 600
# Col: 800

def add_noise(image, percentage):
    row, col = image.shape
    total_pixels = row * col
    num_noisy_pixels = int(total_pixels * (percentage / 100))
    # decimal = percentage / 100 
    # number_of_pixels = random.randint(row*int(decimal), col*int(decimal))
    for _ in range(int(num_noisy_pixels)):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = random.choice([0, 255])

    return image


def apply_mean_filter(image, size):
    img_filtered = cv2.blur(image, (size, size))
    return img_filtered

def apply_median_filter(image, size):
    img_filtered = cv2.medianBlur(image, size)
    return img_filtered

def display_image(image):
    cv2.imshow("Image display", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image = load_image('ai_picture.jpg')
    img_gray = convert2grayscale(image)
    img_noise = add_noise(img_gray, 10)

    img_filtered = apply_mean_filter(img_noise, 3)
    # img_filtered = apply_median_filter(img_noise, 3)
    display_image(img_filtered)

if __name__ == '__main__':
    main()


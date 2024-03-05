import cv2
import os
import numpy as np
from sklearn.decomposition import PCA, KernelPCA
import matplotlib.pyplot as plt

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

def apply_gaussian_noise(image, sigma):
    """A function that applies gaussian noise to an image"""
    row, col = image.shape
    
    # Create noise
    mean = 0
    noise = np.random.normal(loc=mean, scale=sigma, size=(row, col))
    
    # Add noise to image
    img = image + noise

    # Clip pixel values to the valid range [0, 255]
    img = np.clip(img, 0, 255)

    # Convert to uint8 data type
    img = np.uint8(img)
    return img

def apply_mean_filter(image, size):
    """A function that applies an x-sized mean filter to an image """
    img_filtered = cv2.blur(image, (size, size))
    return img_filtered

def apply_median_filter(image, size):
    """A function that applies an x-sized median filter to an image"""
    img_filtered = cv2.medianBlur(image, size)
    return img_filtered

def display_image(image):
    """A function that displayes an image"""
    cv2.imshow("Image Display", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_linear_PCA(image):
    pca = PCA(n_components=32, random_state=42)

    kernel_pca = KernelPCA(
    n_components=400,
    kernel="rbf",
    gamma=1e-3,
    fit_inverse_transform=True,
    alpha=5e-3,
    random_state=42,
    )

    pca.fit(image)
    transformed_image = pca.transform(image)

    # You can also reconstruct the image using the inverse_transform method,
    # if you want to see the reconstructed image after applying PCA.
    reconstructed_image = pca.inverse_transform(transformed_image)

    plt.imshow(reconstructed_image)  # Display the transformed image
    plt.axis('off')
    plt.show()

def main():
    img = load_image('ai_picture.jpg')
    img_gray = convert2grayscale(img)
    gaussian_noise = apply_gaussian_noise(img_gray, 25)

    # img_filtered = apply_mean_filter(gaussian_noise, 3)
    # img_filtered = apply_median_filter(gaussian_noise, 3)
    apply_linear_PCA(gaussian_noise)
    # display_image(gaussian_noise)

if __name__ == '__main__':
    main()

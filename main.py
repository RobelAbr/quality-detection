import os
import cv2
import numpy as np
import shutil


def calculate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
    return sharpness


def calculate_brightness(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab[:, :, 0]
    brightness = np.mean(l_channel)
    return brightness


def analyze_image_quality(image_path):
    image = cv2.imread(image_path)
    sharpness = calculate_sharpness(image)
    brightness = calculate_brightness(image)
    return sharpness, brightness


def delete_low_quality_images(folder_path, threshold_sharpness=100, threshold_brightness=100):
    file_list = os.listdir(folder_path)

    image_files = [f for f in file_list if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)

        sharpness, brightness = analyze_image_quality(image_path)

        if sharpness < threshold_sharpness or brightness < threshold_brightness:
            print(f"Deleting {image_file} (Sharpness: {sharpness}, Brightness: {brightness})")
            # os.remove(image_path)

            shutil.move(image_path, "D:\\rabraha\\Temp")


if __name__ == "__main__":
    folder_path = "D:\\rabraha\\testPic"

    sharpness_threshold = 5
    brightness_threshold = 5

    delete_low_quality_images(folder_path, sharpness_threshold, brightness_threshold)
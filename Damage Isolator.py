import cv2
import numpy as np
import pandas as pd

def analyze_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to the HSV color space to better isolate brown colors
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for brown color
    # These ranges might need adjustment based on your specific images
    lower_brown = np.array([10, 100, 20])
    upper_brown = np.array([20, 255, 200])
    
    # Threshold the HSV image to get only brown colors
    mask = cv2.inRange(hsv, lower_brown, upper_brown)
    
    # Calculate percentage of damaged cells
    brown_pixels = np.count_nonzero(mask)
    total_pixels = image.shape[0] * image.shape[1]
    percentage_damaged = (brown_pixels / total_pixels) * 100
    
    # Optionally, save the mask as an image to visualize the detected areas
    cv2.imwrite('detected_brown_areas.png', mask)
    
    return percentage_damaged


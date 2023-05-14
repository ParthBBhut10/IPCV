# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cHRay8bTZllIfr4kuIvNGUewr09_rlZd
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.fft import fftshift, fft2, ifftshift, ifft2



 
image = cv2.imread('img.jpg', 0) 
plt.imshow(image, cmap='gray')





def butterworth_lowpass_filter(image, cutoff_frequency, order):
    # Convert image to frequency domain
    image_fft = fftshift(fft2(image))
    
    # Create butterworth filter mask
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    x = np.linspace(-center_col, center_col - 1, cols)
    y = np.linspace(-center_row, center_row - 1, rows)
    X, Y = np.meshgrid(x, y)
    distance = np.sqrt(X**2 + Y**2)
    filter_mask = 1 / (1 + (distance / cutoff_frequency)**(2 * order))
    
    # Apply filter in the frequency domain
    filtered_image_fft = image_fft * filter_mask
    
    # Convert back to spatial domain
    filtered_image = np.real(ifft2(ifftshift(filtered_image_fft)))

    return filtered_image









def butterworth_highpass_filter(image, cutoff_frequency, order):
    # Convert image to frequency domain
    image_fft = fftshift(fft2(image))
    
    # Create butterworth filter mask
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    x = np.linspace(-center_col, center_col - 1, cols)
    y = np.linspace(-center_row, center_row - 1, rows)
    X, Y = np.meshgrid(x, y)
    distance = np.sqrt(X**2 + Y**2)
    filter_mask = 1 / (1 + (cutoff_frequency / distance)**(2 * order))
    
    # Apply filter in the frequency domain
    filtered_image_fft = image_fft * filter_mask
    
    # Convert back to spatial domain
    filtered_image = np.real(ifft2(ifftshift(filtered_image_fft)))
    
    return filtered_image











cutoff_frequency = 10  # Adjust this value according to your requirements
order = 2  # Adjust this value according to your requirements







# Apply Butterworth low-pass filter
filtered_image_lowpass = butterworth_lowpass_filter(image, cutoff_frequency, order)




# Apply Butterworth high-pass filter
filtered_image_highpass = butterworth_highpass_filter(image, cutoff_frequency, order)








# Display the original and filtered images
fig=plt.figure(dpi=300)

fig.add_subplot(1,3,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

fig.add_subplot(1,3,2)
plt.imshow(filtered_image_lowpass, cmap='gray')
plt.title('Butterworth LPF')
plt.axis('off')

fig.add_subplot(1,3, 3)
plt.imshow(filtered_image_highpass, cmap='gray')
plt.title('Butterworth HPF')
plt.axis('off')
plt.show()
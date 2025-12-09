import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\gowth\Downloads\Official_portrait_of_Barack_Obama.jpg" #add your path here

img = cv.imread(path)
    
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

blurred_img = cv.medianBlur(img_rgb, ksize=5)

plt.figure(figsize=(8, 4))
plt.title("Median Blurred img")
plt.imshow(blurred_img)
plt.axis()
plt.show()

num_levels = 4
i = np.arange(0, 256)
bin_size = 64
num_output_levels = 10
bin_size = 256 // num_output_levels

output_step = 255 // (num_output_levels - 1)

look_up_table = np.clip((i // bin_size) * output_step, 0, 255).astype(np.uint8)


print(f"Calculated Look-Up Table (Start): {look_up_table[:10]}")
print(f"Calculated Look-Up Table (End): {look_up_table[-10:]}")


posterized_img = cv.LUT(blurred_img, look_up_table)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original (Median Blurred)")
plt.imshow(blurred_img)
plt.axis()

plt.subplot(1, 2, 2)
plt.title("Posterized Image (10 Levels)")
plt.imshow(posterized_img)
plt.axis()
plt.tight_layout()
plt.show()


import sys

import cv2
import numpy as np

if len(sys.argv) == 1:
    print(f"Usage: python {sys.argv[0]} file_name")
    exit()

file_path = sys.argv[1]

image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
height, width = image.shape

for kernel_height in range(1, height + 1):
    for kernel_width in range(1, width + 1):
        # Create a kernel from the top-left corner (0, 0)
        kernel = image[0:kernel_height, 0:kernel_width]

        # Create an image using the kernel
        tiled_image = np.tile(
            kernel, (height // kernel_height + 1, width // kernel_width + 1)
        )

        # Crop image to the original dimensions
        tiled_image = tiled_image[:height, :width]

        # Compare the created image with the original
        if np.array_equal(tiled_image, image):
            original_image = cv2.imread(file_path)
            original_kernel = original_image[:kernel_height, :kernel_width]

            cv2.imwrite("generator_tile.png", original_kernel)
            print(
                f"Generator kernel found and saved as 'generator_tile.png'. Size: {kernel_height}x{kernel_width}"
            )
            exit()
    print(kernel_height)

print("No repeating pattern found within the image dimensions.")

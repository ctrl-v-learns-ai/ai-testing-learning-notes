# -*- coding: utf-8 -*-
"""
NumPy Project 03: Image Processor
Note: This project demonstrates matrix operations.
      Actual image loading requires PIL/Pillow.
"""

import numpy as np

print("=" * 50)
print("  Image Processor (Matrix Operations)")
print("=" * 50)

# Create a sample 8x8 grayscale image (0-255)
np.random.seed(42)
image = np.random.randint(0, 256, (8, 8), dtype=np.uint8)

print("\nOriginal Image (8x8):")
print(image)

# Transform 1: Brightness adjustment
print("\n=== Brightness +50 ===")
bright = np.clip(image.astype(np.int16) + 50, 0, 255).astype(np.uint8)
print(bright)

# Transform 2: Flip horizontal
print("\n=== Flip Horizontal ===")
flipped_h = np.flip(image, axis=1)
print(flipped_h)

# Transform 3: Flip vertical
print("\n=== Flip Vertical ===")
flipped_v = np.flip(image, axis=0)
print(flipped_v)

# Transform 4: Rotate 90 degrees
print("\n=== Rotate 90 degrees ===")
rotated = np.rot90(image)
print(rotated)

# Transform 5: Simple blur (3x3 average)
print("\n=== Simple Blur (center 4x4) ===")
blurred = image.copy().astype(np.float64)
for i in range(1, 7):
    for j in range(1, 7):
        region = image[i-1:i+2, j-1:j+2]
        blurred[i, j] = np.mean(region)
print(blurred.astype(np.uint8))

# Transform 6: Contrast adjustment
print("\n=== Contrast x1.5 ===")
mean_val = np.mean(image)
contrasted = np.clip((image - mean_val) * 1.5 + mean_val, 0, 255).astype(np.uint8)
print(contrasted)

# Statistics
print("\n=== Image Statistics ===")
print(f"Shape: {image.shape}")
print(f"Mean: {np.mean(image):.1f}")
print(f"Std: {np.std(image):.1f}")
print(f"Min: {np.min(image)}")
print(f"Max: {np.max(image)}")

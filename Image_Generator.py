import numpy as np
import matplotlib.pyplot as plt

# Create a 2D grid of coordinates
x, y = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))

# Create a checkerboard pattern using modulo operation
checkerboard_pattern = np.sin(np.pi * x) * np.sin(np.pi * y)

# Normalize the pattern to values between 0 and 1
pattern_normalized = (checkerboard_pattern - checkerboard_pattern.min()) / (checkerboard_pattern.max() - checkerboard_pattern.min())

# Add color to the pattern
color_pattern = np.stack([pattern_normalized, 1 - pattern_normalized, np.zeros_like(checkerboard_pattern)], axis=-1)

# Display the image using matplotlib
plt.imshow(color_pattern)
plt.axis('off')  # Turn off axis labels
plt.show()

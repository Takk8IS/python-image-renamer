# Copyright (c)
# License: Attribution 4.0 International (CC BY 4.0)
# Author: David C Cavalcante
# LinkedIn: https://www.linkedin.com/in/hellodav/
# Medium: https://medium.com/@davcavalcante/
# Takk™ Innovate Studio
# Positive results, rapid innovation
# Leading the Digital Revolution as the Pioneering 100% Artificial Intelligence Team
# URL: https://takk.ag/
# Medium: https://takk8is.medium.com/

# Designed to help you. From AIs to human-beans.
# Every donation propels us forward.
# $USDT (TRC-20): TP6zpvjt2ZNGfWKPevfp65ZrcbKMWSQXDi

import os

# Get the current directory where the .py file is located
folder = os.getcwd()

# List all files in the folder
files = os.listdir(folder)

# Initialize a counter for the number of photos
counter = 1

# Loop through the files in the folder
for file in files:
    # Check if the file is an image (by extension)
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        # Create the new file name
        new_name = f'photo-{counter:03d}.png'
        # Full path to the current file
        current_path = os.path.join(folder, file)
        # Full path to the new file
        new_path = os.path.join(folder, new_name)
        # Rename the file
        os.rename(current_path, new_path)
        # Increment the counter
        counter += 1

print("Renaming completed...")

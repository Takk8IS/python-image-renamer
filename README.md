# Image Renamer

This Python script is designed to rename image files in a specific directory. It searches for files with common image extensions (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`) and renames them sequentially as "photo-001.png", "photo-002.png", and so on.

## Functionality

The code performs the following steps:

1. Imports the `os` module to interact with the operating system.
2. Retrieves the current directory where the Python file is located.
3. Lists all the files in the directory.
4. Initialises a counter for the file names.
5. Iterates over each file in the directory.
6. Checks if the file is an image based on the extension.
7. Creates a new file name in the format "photo-XXX.png", where XXX is a three-digit number incremented for each renamed file.
8. Constructs the full path of the current file and the new file.
9. Renames the file using the `os.rename()` function.
10. Increments the counter.
11. Displays a message indicating that the renaming is complete.

## How to Use

1. Ensure you have Python installed on your system.
2. Save the Python script in a directory that contains the image files you want to rename.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script by typing `python image-renamer.py` in the terminal.
5. The script will rename all the image files in the directory and display a completion message.

## Donations

If this script has been helpful for you, consider making a donation to support our work:

-   $USDT (TRC-20): TP6zpvjt2ZNGfWKPevfp65ZrcbKMWSQXDi

Your donations help us continue developing useful and innovative tools.

Thank you for using our script!

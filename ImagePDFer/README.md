# ImagePDFer

ImagePDFer is a user-friendly tool that converts a folder of images into a single PDF file. The images are enhanced using techniques similar to those found in CamScanner and are sorted by their modification times.

## Features

- Converts images from a specified folder into a single PDF file.
- Enhances images using grayscale conversion, Gaussian blur, edge detection, and thresholding.
- Sorts images by their last modification time before adding them to the PDF.
- Provides clear user feedback throughout the process.

## Prerequisites

Ensure you have the following Python libraries installed:

- `opencv-python`
- `fpdf`
- `Pillow`

You can install these libraries using pip:

```bash
pip install opencv-python fpdf pillow
```

## Usage

1. Clone the repository or download the script.

2. Navigate to the directory containing the script.

3. Run the script:

    ```bash
    python ImagePDFer.py
    ```

4. Follow the on-screen prompts to enter the path to the image folder and the desired output PDF file name (including the `.pdf` extension).

### Example

```bash
Welcome to ImagePDFer - Your Image to PDF Conversion Tool
Enter the path to the image folder: /path/to/your/images
Enter the desired output PDF file name (including .pdf extension): output.pdf
Starting the PDF creation process...
Processing /path/to/your/images/image1.jpg...
Processing /path/to/your/images/image2.jpg...
PDF created successfully: output.pdf
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and include appropriate tests.

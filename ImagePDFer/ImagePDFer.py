import os
import glob
import cv2
from fpdf import FPDF
from PIL import Image

def get_sorted_images(image_folder):
    images = glob.glob(os.path.join(image_folder, '*'))
    images.sort(key=lambda x: os.path.getmtime(x))
    return images

def enhance_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    _, thresholded = cv2.threshold(edged, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded

def create_pdf(image_folder, output_pdf):
    images = get_sorted_images(image_folder)
    
    if not images:
        print("No images found in the provided folder.")
        return

    pdf = FPDF()

    for image_path in images:
        print(f"Processing {image_path}...")
        enhanced_image = enhance_image(image_path)
        temp_image_path = image_path + '_enhanced.jpg'
        cv2.imwrite(temp_image_path, enhanced_image)
        cover = Image.open(temp_image_path)
        width, height = cover.size
        pdf.add_page()
        pdf.image(temp_image_path, 0, 0, width / 4, height / 4)
        os.remove(temp_image_path)

    pdf.output(output_pdf, "F")
    print(f"PDF created successfully: {output_pdf}")

def main():
    try:
        image_folder = input("Enter the path to the image folder: ").strip()
        if not os.path.isdir(image_folder):
            print("The provided path is not a valid directory.")
            return
        
        output_pdf = input("Enter the desired output PDF file name (including .pdf extension): ").strip()
        if not output_pdf.endswith('.pdf'):
            print("Output file name must end with .pdf extension.")
            return

        print("Starting the PDF creation process...")
        create_pdf(image_folder, output_pdf)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

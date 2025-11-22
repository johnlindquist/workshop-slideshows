#!/usr/bin/env python3
import fitz  # PyMuPDF
import os
import sys

def extract_images_from_pdf(pdf_path, output_dir="images"):
    """Extract all images from a PDF file."""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Open PDF
    pdf_document = fitz.open(pdf_path)
    image_list = []
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list_page = page.get_images()
        
        # Extract images from this page
        for img_index, img in enumerate(image_list_page):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Generate filename
            image_filename = f"image_page{page_num+1}_img{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            # Save image
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            
            image_list.append(image_filename)
            print(f"Extracted: {image_filename}")
    
    pdf_document.close()
    return image_list

if __name__ == "__main__":
    pdf_path = "Claude_Code_Power_User_Mastery.pdf"
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found!")
        sys.exit(1)
    
    images = extract_images_from_pdf(pdf_path)
    print(f"\nTotal images extracted: {len(images)}")
    print(f"Images saved to: images/")


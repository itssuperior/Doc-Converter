import os
import io
import google.generativeai as genai
from PIL import Image
from docx import Document
from bs4 import BeautifulSoup
from docx.shared import Inches
# Open the PDF file
pdf_document = fitz.open(pdf_path)
    # Create a new Word document
doc = Document()
    
total_pages = len(pdf_document)
print(f"📄 Found {total_pages} page(s) in the PDF.")
# STEP 1: Iterate through each page of the PDF
for page_num in range(total_pages):
        print(f"\n--- Processing Page {page_num + 1} of {total_pages} ---")
        page = pdf_document.load_page(page_num)

        # Convert the page to an image (pixmap)
        # Increase DPI for better image quality and OCR accuracy
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save image to a byte stream in memory
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()
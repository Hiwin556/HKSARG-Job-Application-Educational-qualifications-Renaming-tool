import os
import shutil
from datetime import datetime

# Define the paths here
SOURCE_FOLDER = r""  # folder containing the PDF files (Path Of OrigionalPDFs)
DESTINATION_FOLDER = r""  # folder where converted files will be stored (Path Of RenamedPDFs)

def convert_pdfs():
    # Validate source folder exists
    if not os.path.exists(SOURCE_FOLDER):
        print(f"Error: Source folder '{SOURCE_FOLDER}' does not exist!")
        return
    
    # Get user input for name and application number
    user_name = input("\nPlease enter your name: ")
    application_number = input("Please enter your application number: ")
    
    # Create application number subfolder inside destination folder
    application_folder = os.path.join(DESTINATION_FOLDER, application_number)
    if not os.path.exists(application_folder):
        os.makedirs(application_folder)
        print(f"Created application folder: {application_folder}")
    
    # Get all PDF files from source folder
    pdf_files = [f for f in os.listdir(SOURCE_FOLDER) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the source folder!")
        return
    
    print(f"\nFound {len(pdf_files)} PDF files to process...")
    
    # Process each PDF file
    for pdf_file in pdf_files:
        # Get original file name without extension
        original_name = os.path.splitext(pdf_file)[0]
        
        # Create new file name
        new_filename = f"{original_name}_{user_name}_{application_number}.pdf"
        
        # Source and destination paths
        source_path = os.path.join(SOURCE_FOLDER, pdf_file)
        destination_path = os.path.join(application_folder, new_filename)
        
        try:
            # Copy and rename the file
            shutil.copy2(source_path, destination_path)
            print(f"Successfully converted: {pdf_file} -> {new_filename}")
        except Exception as e:
            print(f"Error converting {pdf_file}: {str(e)}")
    
    print("\nConversion completed!")

if __name__ == "__main__":
    print("PDF Converter")
    print("=============")
    convert_pdfs() 
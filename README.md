# PDF Converter

A simple Python utility to rename and organize PDF files according to a specific naming convention.

## Setup

1. Make sure you have Python installed on your system
2. The program uses two main folders:

   Example:
   - `C:\Users\user\PDF Converter\OriginalPDFs` - Place your original PDF files here
   - `C:\Users\user\PDF Converter\RenamedPDFs` - Converted files will be stored here

## How to Use

1. Place all your PDF files that need to be renamed in the `OriginalPDFs` folder
2. Run the program by executing `pdf_converter.py`
3. When prompted:
   - Enter your name
   - Enter your application number
4. The program will:
   - Create a new subfolder with your application number in the `RenamedPDFs` directory
   - Copy all PDF files from the source folder
   - Rename them according to the format: `file_[original-name]_[your-name]_[application-number].pdf`
   - Place them in the new subfolder

## File Naming Convention

The converted files will follow this naming pattern:
```
file_[original-name]_[your-name]_[application-number].pdf
```

For example, if you have:
- Original file name: `document.pdf`
- Your name: `John`
- Application number: `12345`

The converted file will be named:
```
file_document_John_12345.pdf
```

## Error Handling

The program will:
- Check if the source folder exists
- Verify that PDF files are present in the source folder
- Create the destination folder if it doesn't exist
- Display success/error messages for each file processed 

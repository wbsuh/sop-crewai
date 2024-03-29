import fitz  # PyMuPDF

def pdf_to_markdown(pdf_path, md_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Initialize a variable to hold the markdown content
    markdown_content = ""
    
    # Iterate through each page in the PDF
    for page_num in range(len(doc)):
        # Extract text from the current page
        text = doc.load_page(page_num).get_text()
        
        # Add the extracted text to the markdown content variable
        # Here you might want to add additional formatting based on your needs
        # For example, you could prepend each page's text with a Markdown header
        markdown_content += f"\n\n# Page {page_num + 1}\n\n{text}"
    
    # Save the markdown content to a file
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
    
    print(f"Markdown file saved to {md_path}")

# Example usage
pdf_path = "ICH guidelines.pdf"  # Specify your PDF file path
md_path = "ICH guidelines.md"  # Specify your desired markdown file path
pdf_to_markdown(pdf_path, md_path)
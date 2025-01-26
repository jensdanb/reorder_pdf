from pypdf import PdfReader, PdfWriter
from glob import iglob
from time import sleep


# Find pdf documents and open them all in Python as PdfReader objects. 

input_file_names = iglob('*input/*.pdf')
input_pdfs = [PdfReader(name) for name in input_file_names]

if len(input_pdfs) == 0:
    print("No pdf files found in input folder. Exiting in 3 seconds")
    sleep(3)
    exit()


# Ensure all documents have same number of pages and find that number. 

pages_per_pdf = [len(pdf.pages) for pdf in input_pdfs]

if not len(set(pages_per_pdf)) == 1:
    print("Number of pages per document are not all the same number. Exiting in 3 seconds")
    sleep(3)
    exit()

number_of_pages = pages_per_pdf[0]


# Make output files as PdfWriter objects, add the right pages to them, save and close. 

for page_nr in range(number_of_pages):
    writer = PdfWriter()
    
    for input_pdf in input_pdfs:
        writer.append(input_pdf, [page_nr])
    
    output_file = open("output/doc_" + str(page_nr+1) + ".pdf", "wb")
    writer.write(output_file)
    writer.close()
    output_file.close()

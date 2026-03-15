#!/usr/bin/env python3

# importing required modules
from pypdf import PdfWriter


def PDFmerge(pdfs, output):
    # creating pdf file writer object
    pdfWriter = PdfWriter()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfWriter.append(pdf)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfWriter.write(f)


def main():
    # pdf files to merge
    pdfs = ['resume_akshat.pdf', 'Akshat_Resume.pdf']

    # output pdf file name
    output = 'combined_example.pdf'

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
    # calling the main function
    main()
# from PIL import Image
import os, PyPDF2

def encryptpdf(pdf_path = "imvickykumar999.pdf", passw = 'pass'):
    pdfFile = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    # passw = input('Enter password to set : ')
    pdfWriter.encrypt(passw)

    resultPdf = open(f'{pdf_path.split(".")[0]}.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

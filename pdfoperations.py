from PyPDF2 import PdfWriter,PdfReader
n=int(input("enter number of pages you want to combine"))
pdfs=['Design And Analysis Of Algorithms - - Unit 4 - Week 1 Quiz.pdf','Design And Analysis Of Algorithms - - Unit 6 - Week 2 Quiz.pdf']
pw=PdfWriter()

for pdf in pdfs:
    pr=PdfReader(open(pdf,'rb'))
    page=pr.pages[n-1]
    pw.add_page(page)

with open('outt.pdf','wb') as i:
    pw.write(i)
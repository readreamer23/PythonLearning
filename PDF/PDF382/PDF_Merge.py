from PyPDF2 import PdfReader,PdfWriter
import os

curpath = os.path.dirname('D:\\Dev_Tools\\python\\TEST_PDF\\merge\\')
file1 = os.path.join(curpath,'0.pdf')
file2 = os.path.join(curpath,'1.pdf')
file3 = os.path.join(curpath,'合并后的文档.pdf')

def merge_pdf(file1,file2,file3):
    read_pdf1 = PdfReader(file1)
    read_pdf2 = PdfReader(file2)
    n1 = len(read_pdf1.pages)
    n2 = len(read_pdf2.pages)
    writer_pdf=PdfWriter()

    for i in range(n1):
        writer_pdf.add_page(read_pdf1.pages[i])
    for j in range(n2):
        writer_pdf.add_page(read_pdf2.pages[j])

    with open(file3, "wb") as f:
        writer_pdf.write(f)

    print("合并后文件：",file3)
    print("合并完毕")
if __name__=='__main__':
    merge_pdf(file1,file2,file3)

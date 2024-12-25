from PyPDF2 import PdfFileReader,PdfFileWriter

import os

curpath = os.path.dirname('D:\\Dev_Tools\\python\\TEST_PDF\\')
filename = os.path.join(curpath,'PDF1.pdf')
def split_pdf(file1):
    read_pdf=PdfFileReader(file1)
    n=read_pdf.getNumPages()
    print("文档共有%d页"%(n))

    for i in range(n):
        writer_pdf=PdfFileWriter()
        writer_pdf.addPage(read_pdf.getPage(i))
        file2=os.path.join(curpath,'split',str(i)+'.pdf')
        with open(file2,"wb") as f:
            writer_pdf.write(f)

    print("拆分完毕")
if __name__=='__main__':
    split_pdf(filename)

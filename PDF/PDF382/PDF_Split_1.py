from PyPDF2 import PdfReader,PdfWriter

import os

curpath = os.path.dirname('D:\\Dev_Tools\\python\\TEST_PDF\\')
filename = os.path.join(curpath,'PDF1.pdf')


"""
    拆分PDF文件:把PDF每页都拆分为一个PDF文件
    :param input_file: 输入的PDF文件路径。
"""
def split_pdf(file1):
    read_pdf=PdfReader(file1)
    n=len(read_pdf.pages)
    print("文档共有%d页"%(n))

    for i in range(n):
        writer_pdf=PdfWriter()
        writer_pdf.add_page(read_pdf.pages[i])
        file2=os.path.join(curpath,'split',str(i)+'.pdf')
        with open(file2,"wb") as f:
            writer_pdf.write(f)

    print("拆分完毕")
if __name__=='__main__':
    split_pdf(filename)

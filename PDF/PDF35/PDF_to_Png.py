import fitz
import glob
import os

curpath = os.path.dirname('C:\\Users\\lihui\\Desktop\\back\\20241211\\')
pdfpath = os.path.join(curpath,'体检报告.pdf')
savepath = os.path.join(curpath,'png')
print("源文件：",pdfpath)

"""
    拆分PDF文件为指定数量的小文件。
    :param input_file: 输入的PDF文件路径。
    :param output_prefix: 输出文件的前缀。
    :param split_count: 拆分的数量。
    """
def pdf2png():
    pdfs=glob.glob(pdfpath)

    for i in pdfs:
        pdffile = fitz()
        start = i * split_size
        end = min((i + 1) * split_size, page_count)
        for index in range(start, end):
            output.add_page(pdf_reader.pages[index])

        with open('{}-{}.pdf'.format(output_prefix, i), 'wb') as output_pdf:
            output.write(output_pdf)

print("拆分PDF完毕")

# 使用示例
if __name__=='__main__':
    #print("拆分PDF为3份")
    pdf2png()

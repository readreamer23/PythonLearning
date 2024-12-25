import PyPDF2
import os

curpath = os.path.dirname('D:\\Dev_Tools\\python\\TEST_PDF\\')
file1 = os.path.join(curpath,'PDF1.pdf')
file2 = os.path.join(curpath,'output\\','output')
print("源文件：",file1)
print("拆分后文件前缀:",file2)

"""
    拆分PDF文件为指定数量的小文件。
    :param input_file: 输入的PDF文件路径。
    :param output_prefix: 输出文件的前缀。
    :param split_count: 拆分的数量。
    """
def split_pdf(input_file, output_prefix, split_count):
    pdf_reader = PyPDF2.PdfReader(input_file)
    page_count = len(pdf_reader.pages)
    split_size = (page_count // split_count) + 1  # 计算每个分割文件的页数

    for i in range(split_count):
        output = PyPDF2.PdfWriter()
        start = i * split_size
        end = min((i + 1) * split_size, page_count)
        for index in range(start, end):
            output.add_page(pdf_reader.pages[index])

        with open('{}-{}.pdf'.format(output_prefix, i), 'wb') as output_pdf:
            output.write(output_pdf)

print("拆分PDF完毕")

# 使用示例
if __name__=='__main__':
    print("拆分PDF为3份")
    split_pdf(file1, file2, 3)

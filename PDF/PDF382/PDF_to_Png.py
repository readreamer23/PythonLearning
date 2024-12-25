import fitz
import glob
import os

curpath = os.path.dirname('D:\\Dev_Tools\\python\\TEST_PDF\\')
pdfpath = os.path.join(curpath,'PDF1.pdf')
savepath = os.path.join(curpath,'png')
print("源文件：",pdfpath)
print("图片目标文件夹：",savepath)

"""
    PDF文件转图片
    :param input_file: 输入的PDF文件路径。
    """
def pdf2png():
    pdfs=glob.glob(pdfpath) #获取所有PDF文档文件名

    for f in pdfs:
        pdffile = fitz.open(f)
        filename=os.path.split(f)[1]
        filename=filename.split('.')[0]
        filepath=os.path.join(savepath,filename)
        for x in range(pdffile.page_count):
            page=pdffile[x]
            x_1=1
            y_1=1
            mat=fitz.Matrix(x_1,y_1)
            pix=page.get_pixmap(matrix=mat,alpha=False)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            #pix.writeImage(filepath+'\\'+f"{x}.png")    
            pix.save(f"{filepath}\\{x}.png")




# 使用示例
if __name__=='__main__':
    pdf2png()
    print("PDF转图片成功！")

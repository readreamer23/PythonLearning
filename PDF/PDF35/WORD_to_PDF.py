import win32com.client
from win32com.client import gencache
from win32com.client import constants
import os
import sys

curpath = os.path.dirname('C:\\Users\\lihui\\Desktop\\back\\20241211\\')
wordfilename = os.path.join(curpath,'word1.docx')
pdffilename = os.path.join(curpath,'word1.pdf')
print("源文件：",wordfilename)

def word2pdf(wordpath,pdfpath):
    word = gencache.EnsureDispatch('Word.Application')
    print(sys.modules[word.__module__].__file__)

    #word=win32com.client.Dispatch('Word.Application')

    doc = word.Documents.Open(wordpath)
    doc.ExportAsFixedFormat(pdfpath,constants.wdExportFormatPDF)
    word.Quit()




# 使用示例
if __name__=='__main__':
    word2pdf(wordfilename,pdffilename)
    print("WORD转PDF完毕")

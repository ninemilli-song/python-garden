"""
**********有没有觉得 Kindle 中的笔记很难查找？**********
*********Kindle 把所有的笔记都放在一个文件中了**********
********这个小工具按照图名将笔记归类到各自的文件中********
*******************方便爱读书的你*********************
"""
import os
import shutil


def gen_node(target_path):
    """
    生成笔记
    """
    # kindle 中笔记的目录
    note_path = '/Volumes/Kindle/documents/My Clippings.txt'
    f = open(note_path, 'r+')
    
    try:
        # 如果文件已存在会抛出异常，捕获异常避免程序错误
        os.mkdir(target_path)
    except OSError as error:
        print("OSError" + str(error) + "\n")
        # 如果文件目录存在，则清空然后新建
        if error.errno == 17:
            print("🚗 I will delete it and create a new one! :)" + "\n")
            shutil.rmtree(target_path, ignore_errors=True)
            os.mkdir(target_path)
        pass

    while True:
        onenote = []
        for i in range(0,5):
            line = f.readline()
            if not line:
                exit()
            onenote.append(line)
        book_note = open('%s%s.txt'%(target_path, onenote[0]), 'a+')
        book_note.write(onenote[1] + '\n')
        book_note.write(onenote[3] + '\n')
        book_note.write(onenote[4] + '\n')
        book_note.close()


if __name__ == '__main__':
    print("/"*60)
    print("有没有觉得 Kindle 中的笔记很难查找？".center(60, '*'))
    print("Kindle 把所有的笔记都放在一个文件中了".center(60, '*'))
    print("这个小工具按照图名将笔记归类到各自的文件中".center(60, '*'))
    print("方便爱读书的你".center(60, '*'))
    print("/"*60)
    path = input("请输入你导出文件的目录（默认目录为桌面 - /Users/ninemilli/Desktop/digest/）: ")

    if path == '':
        path = '/Users/ninemilli/Desktop/digest/'
    
    gen_node(path)

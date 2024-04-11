#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    #str1 = input("please input:\n")
    #print(str1)

    # file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
    # access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    # t    # 文本模式(默认)。
    # x    # 写模式，新建一个文件，如果该文件已存在则会报错。
    # b    # 二进制模式。
    # +    打开一个文件进行更新(可读可写)。
    # U    # 通用换行模式（不推荐）。
    # r    # 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    # rb    # 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    # r + 打开一个文件用于读写。文件指针将会放在文件的开头。
    # rb + 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    # w    # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    # wb    # 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    # w + 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    # wb + 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    # a    # 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # ab    # 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    # a + 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    # ab + 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
    # buffering: 如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
    fr = open("D:/ws-py/snow-python-overview/01_hello_world/files/a.txt", "r")
    fw = open("D:/ws-py/snow-python-overview/01_hello_world/files/a.txt", "a+")
    print(fr.tell())
    print(fw.tell())

    print(fr.readlines())
    print(fr.tell())

    fw.write("asdfsdfsaf\n23424234234\n")
    print(fw.tell())
    fw.flush()

    print(fr.tell())
    fr.seek(0) #不论读写都有个指针的问题，读的时候，指针从0开始，读完了，会停在末尾，如果再次调用，也是从末尾开始，如果想让它重新从文件头开始读，就得重置为0
    print(fr.readlines())

    fr.close()
    fw.close()

    f1 = open("D:/ws-py/snow-python-overview/01_hello_world/files/a.txt", "a+")
    f1End = f1.tell()
    f1.seek(0)
    print(f1.readlines())
    f1.seek(f1End)
    f1.write("234234244etetettwetrw\n")
    f1.flush()
    f1.seek(0)
    print(f1.readlines())

    

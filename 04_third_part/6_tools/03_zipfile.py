import zipfile

Zippy = zipfile.ZipFile('example.zip', 'w')
Zippy.write("D:\\data\\channel-proxy\\deduct\\batch\\20230410\\XPSBC005000001SS")
Zippy.close()
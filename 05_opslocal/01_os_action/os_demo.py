import os


def list_files():
    files = os.listdir("..")
    for f in files:
        print(f)


# os.path.exists(filename) 检查文件是否存在
# os.makedirs(directory, exist_ok=True) 创建文件夹，已存在了不会报错
# os.remove(filename) 删除文件
# os.rename(src, dst) 重命名或者移动文件都行


import subprocess


def run_command(command):
    """
    注意：shell=True允许直接传递字符串作为命令，但有安全风险，特别是当命令部分来自用户输入时。
    :param command:
    :return:
    """
    ret = subprocess.run(command, shell=True)
    print(type(ret))  # <class 'subprocess.CompletedProcess'>


# os.environ.get(var_name, "未找到") #获取环境变量
# os.chdir(new_dir) #切换工作目录，相当于cd
# result.strip() = subprocess.check_output(command, shell=True, text=True) #check_output()执行命令并返回其输出，text=True使输出为文本格式而非字节串。


import glob


def batch_rename(pattern, new_name_base, extension):
    """
    批量重命名
    :param pattern:
    :param new_name_base:
    :param extension:
    :return:
    """
    for count, filename in enumerate(glob.glob(pattern)):
        new_name = f"{new_name_base}_{count}.{extension}"
        os.rename(filename, new_name)
        print(f"重命名: {filename} -> {new_name}")


batch_rename("*.txt", "document", "txt")


if __name__ == "__main__":
    list_files()
    run_command("dir")  # 在Windows中列出目录，Linux下使用'ls'
    print("".join(["a", "b"]))
    a = "a"
    b = "b"
    print(f"{a}{b}")

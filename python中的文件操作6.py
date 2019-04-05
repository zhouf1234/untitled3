# 复制文件
# 导入一个模块
import sys

# 获取 源文件和目标文件
src_path = sys.argv[1]
dst_path = sys.argv[2]

# 执行复制
with open(src_path, 'rb') as src_file, open(dst_path, 'wb') as dst_file:
    # dst_file.write(src_file.read())  #
    for line in src_file:
        dst_file.write(line)


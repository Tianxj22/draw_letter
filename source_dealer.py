#————————————————————处理资源文件————————————————————————#
#——————————————————————————————————————————————————————#

import os
import json

cur_dir = os.path.dirname(os.path.realpath(__file__))
config = json.load(open(os.path.join(cur_dir, "config.json"), 'r'))
source_dir = os.path.join(cur_dir, config['source_folder'])

#——————————————————————————————————————————————————————#

def get_file_value(ch: str):
    '''返回对应名称的文件内容'''
    ans = []
    file = open(os.path.join(source_dir, f"{ch}.txt"))
    for line in file.readlines():
        temp = []
        for val in line.split(','):
            try:
                temp.append(float(val))
            except:
                temp.append(val)
        ans.append(temp)
    return ans

#——————————————————————————————————————————————————————#

# file_list = os.listdir(source_dir)
# file_list.sort()
# for idx in range(len(file_list)):
#     print(f"{idx}: {file_list[idx]}")
# idx = int(input("请输入您想要查看的文件： "))
# output_file = open(os.path.join(source_dir, file_list[idx]), 'r')
# for line in output_file.readlines():
#     print(line.rstrip('\n'))
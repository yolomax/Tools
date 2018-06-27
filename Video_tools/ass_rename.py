from pathlib import Path
import os

def file_abs_path(arg):
    return Path(os.path.realpath(arg)).parent


def name_match(s, t):
    s = str(s)
    t = str(t)
    t = t.split('*')
    assert len(t) == 2
    for i in t:
        if len(i) == 0:
            continue
        if i not in s:
            return False
    return True

def rename_ass(file_path, source_name, target_name, idx, num):
    name = str(target_name)
    name = name.split('*')
    assert len(name) == 2
    num_type = '%0' + str(num) + 'd'
    num_idx = num_type % idx
    target_name = name[0] + num_idx + name[1]
    raw_file = file_path / source_name
    return raw_file.rename(file_path / target_name)


file_folder = Path('D:\Files\迅雷\[Mirai_Nikki][TV_BDRIP][BIG5][1-26_SP][ASS][YYDM-SUB]')
match_name = '[Mirai Nikki][*][BDRIP][1080P][H264_FLACx2].YYDM.BIG5.ass'
target_name = '[YYDM-11FANS][Mirai Nikki][*][BDRIP][720P][X264-10bit_AACx2][7CBC4BA3].ass'
num = 2
num_range = [1, 26]

file_box = file_folder.glob(str('*.ass'))
file_box = sorted([x.name for x in file_box])
file_box = [x for x in file_box if name_match(x, match_name)]
assert len(file_box) == (num_range[1] - num_range[0] + 1)
for num_i, file_i in enumerate(file_box):
    rename_ass(file_folder, file_i, target_name, idx=(num_range[0]+ num_i), num=num)
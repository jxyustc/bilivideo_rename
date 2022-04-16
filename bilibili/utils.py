# coding=utf-8
import json
import os
import shutil


class BiliRename:
    def __init__(self,dir):
        self.path = os.path.realpath(dir)
        self.type = 0  # 0 for normal video, 1 for special 'ss' video

    def video_rename(self):
        print(self.path)
        filelist = os.listdir(self.path)
        print(filelist)

        bili_series_num = os.path.basename(self.path)
        if 'ss' in bili_series_num:
            self.type = 1

        if self.type:
            series_meta_file = bili_series_num.split('ss')[1] + ".info"
        else:
            series_meta_file = bili_series_num + ".dvi"

        series_meta_file = os.path.join(self.path, series_meta_file)
        if self.type:
            series_title = get_json_key_value(series_meta_file, 'SeasonTitle')
        else:
            series_title = get_json_key_value(series_meta_file, 'Title')
        series_combine_dir = os.path.join(self.path, series_title)
        os.mkdir(series_combine_dir)

        for file in filelist:
            # 分p文件夹
            part_dir = os.path.join(self.path, file)
            # 判断是文件夹
            if os.path.isdir(part_dir):
                dir_files = os.listdir(part_dir)
                for dir_file in dir_files:
                    if dir_file.endswith('mp4'):
                        # 分p的视频信息文件
                        part_meta_file = os.path.join(part_dir, bili_series_num) + '.info'
                        part_name = get_json_key_value(part_meta_file, 'PartName')
                        mp4_file_path = os.path.join(part_dir, dir_file)
                        print(part_name)
                        print(mp4_file_path)
                        target_mp4_file_path = os.path.join(series_combine_dir, part_name + ".mp4")
                        print(target_mp4_file_path)
                        shutil.copyfile(mp4_file_path, target_mp4_file_path)



def video_rename(dir):
    # E:\OneDrive\个人资料\英语\词汇\55852277
    path = os.path.realpath(dir)
    print(path)

    list = os.listdir(path)
    print(os.path.abspath(path))
    print(os.path.basename(path))

    # 55852277
    bili_series_num = os.path.basename(path)
    # 55852277.dvi
    if 'ss' in bili_series_num:  # 如果ss存在与文件夹名，dvi文件中并不存在会报错
        series_meta_file = bili_series_num.split('ss')[1] + ".info"
    else:
        series_meta_file = bili_series_num + ".dvi"
    # E:\OneDrive\个人资料\英语\词汇\55852277\55852277.dvi
    series_meta_file = os.path.join(path, series_meta_file)
    series_title = get_json_key_value(series_meta_file, 'Title')
    series_combine_dir = os.path.join(path, series_title)
    os.mkdir(series_combine_dir)

    for file in list:
        # 分p文件夹
        part_dir = os.path.join(path, file)
        # 判断是文件夹
        if os.path.isdir(part_dir):
            dir_files = os.listdir(part_dir)
            for dir_file in dir_files:
                if dir_file.endswith('mp4'):
                    # 分p的视频信息文件
                    part_meta_file = os.path.join(part_dir, bili_series_num) + '.info'
                    part_name = get_json_key_value(part_meta_file, 'PartName')
                    mp4_file_path = os.path.join(part_dir, dir_file)
                    print(part_name)
                    print(mp4_file_path)
                    target_mp4_file_path = os.path.join(part_dir, part_name + ".mp4")
                    print(target_mp4_file_path)
                    os.rename(mp4_file_path, target_mp4_file_path)
                    shutil.move(target_mp4_file_path, series_combine_dir)


def get_json_key_value(json_file, key_name):
    with open(json_file, 'r', encoding='utf8') as f:
        text = json.load(f)
        return text[key_name]

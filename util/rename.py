# coding=utf-8
import json
import os
import shutil


class BiliRename:
    def __init__(self, dir):
        self.path = os.path.realpath(dir)
        self.type = 0  # 0 for normal video, 1 for special 'ss' video
        self.decrypt = 1

    def _process_dir(self, raw_dir, target_dir):
        bili_series_num = os.path.basename(raw_dir)
        series_meta_file = os.path.join(raw_dir, bili_series_num + ".dvi")
        series_title = get_json_key_value(series_meta_file, 'Title')

        for f in os.listdir(raw_dir):
            part_dir = os.path.join(raw_dir, f)
            # 判断是文件夹
            if os.path.isdir(part_dir):
                dir_files = os.listdir(part_dir)
                for dir_file in dir_files:
                    if dir_file.endswith('mp4'):
                        if self.type == 1:
                            part_name = series_title
                        else:
                            part_meta_file = os.path.join(part_dir, bili_series_num) + '.info'
                            part_name = get_json_key_value(part_meta_file, 'PartName')
                        print(part_name)
                        mp4_file_path = os.path.join(part_dir, dir_file)
                        print(mp4_file_path)
                        target_mp4_file_path = os.path.join(target_dir, part_name + ".mp4")
                        print(target_mp4_file_path)
                        shutil.copyfile(mp4_file_path, target_mp4_file_path)

    def video_rename(self):
        print(self.path)
        filelist = os.listdir(self.path)
        print(filelist)

        bili_series_num = os.path.basename(self.path)
        if 'ss' in bili_series_num:
            self.type = 1

        if self.type:
            series_meta_file = os.path.join(self.path, bili_series_num.split('ss')[1] + ".info")
            series_title = get_json_key_value(series_meta_file, 'SeasonTitle')
        else:
            series_meta_file = os.path.join(self.path, bili_series_num + ".dvi")
            series_title = get_json_key_value(series_meta_file, 'Title')

        series_combine_dir = os.path.join(os.path.join(self.path, os.pardir), series_title)
        self.output_dir = series_combine_dir
        if not os.path.exists(series_combine_dir):
            os.mkdir(series_combine_dir)

        if self.type:
            for videos in os.listdir(self.path):
                full_path = os.path.join(self.path, videos)
                if os.path.isdir(full_path):
                    self._process_dir(full_path, series_combine_dir)
        else:
            self._process_dir(self.path, series_combine_dir)


def get_json_key_value(json_file, key_name):
    with open(json_file, 'r', encoding='utf8') as f:
        text = json.load(f)
        return text[key_name]

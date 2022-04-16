from bilibili.utils import BiliRename

target_dir = "C:\\Users\\splendor\\AppData\\Local\\Packages\\36699Atelier39.forWin10_pke1vz55rvc1r\\LocalCache" \
            "\\BilibiliDownload\\980230500"

# target_dir="C:\\Users\\splendor\\AppData\\Local\\Packages\\36699Atelier39.forWin10_pke1vz55rvc1r\\LocalCache" \
#              "\\BilibiliDownload\\424438019"

if __name__ == "__main__":
    renamer = BiliRename(target_dir)
    renamer.video_rename()

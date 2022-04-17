from util.rename import BiliRename
from util.decap import Decode

target_dir = "C:\\Users\\splendor\\AppData\\Local\\Packages\\36699Atelier39.forWin10_pke1vz55rvc1r\\LocalCache" \
            "\\BilibiliDownload\\ss39078"

if __name__ == "__main__":
    renamer = BiliRename(target_dir)
    renamer.video_rename()
    decoder=Decode(renamer.output_dir)
    decoder.decode_all(inplace=True)
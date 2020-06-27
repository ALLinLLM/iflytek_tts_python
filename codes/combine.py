import glob

if __name__ == "__main__":
    # 合并mp3
    MP3_list = glob.glob(r"../outputs/demo*.mp3")
    f3_write = open('../outputs/combine.mp3', 'wb')
    for mp3 in MP3_list:
        with open(mp3, 'rb') as f:
            f3_write.write(f.read())
    f3_write.flush()
    f3_write.close()
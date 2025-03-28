with open(".\mystudy\codes\水调歌头.txt" ,"r+", encoding="utf-8") as f:
    print(f.readline())
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.write("我欲乘风归去")
    f.write("又恐琼楼玉宇")
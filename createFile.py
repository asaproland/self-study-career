import os
import datetime

# 获取当前日期
now = datetime.datetime.now()
month = now.strftime("%m")
month_day = now.strftime("%m%d")

# 创建文件夹
folder_name = os.path.join(os.getcwd(), month, month_day)
os.makedirs(folder_name, exist_ok=True)

print("文件夹已创建：", folder_name)

# 添加.md文件
files = ["timeSpendWhere.md", "note.md", "thing-talkSelf.md", "review.md"]
for file in files:
    file_path = os.path.join(folder_name, file)
    with open(file_path, "w") as f:
        pass

print(".md文件已添加到文件夹：", folder_name)

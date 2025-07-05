import os

# 获取当前脚本所在目录
folder_path = os.path.dirname(os.path.abspath(__file__))

# 遍历目录中的所有文件
for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    # 只处理文件，不处理文件夹
    if os.path.isfile(old_path):
        # 处理逻辑：
        if filename.startswith("ch"):
            new_filename = "CH" + filename[2:]
        else:
            new_filename = filename[0].upper() + filename[1:]

        new_path = os.path.join(folder_path, new_filename)

        # 重命名（避免重复重命名）
        if new_filename != filename:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")

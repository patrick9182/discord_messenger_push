import os
import sys
import json
from datetime import datetime

# 從命令行參數獲取 JSON 文件路徑
if len(sys.argv) < 2:
    print("Please provide the JSON file path.")
    sys.exit(1)
json_file_path = sys.argv[1]

# 定義執行 Python 程序的函數
def run_python_program():
    # 執行 Python 程序
    print("Message sent")
    os.system(f".\\.venv\\Scripts\\python main.py {json_file_path}")
    
    # 將今天的日期寫入 JSON 文件
    with open(json_file_path, "r+", encoding="utf-8") as file:
        data = json.load(file)
        data["last_run_date"] = datetime.now().strftime("%Y%m%d")
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)

# 檢查是否存在上次執行日期的字段
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        last_run_date = data.get("last_run_date")
except FileNotFoundError:
    print(f"File {json_file_path} does not exist.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"File {json_file_path} is not a valid JSON file.")
    sys.exit(1)

# 獲取今天的日期
current_date = datetime.now().strftime("%Y%m%d")
# print("Current date:", current_date)
# print("Last run date:", last_run_date)

# 如果上次執行日期不等於今天的日期，則執行 Python 程序
if last_run_date != current_date:
    run_python_program()
else:
    print("The program has already been executed today.")
    print("Current date:", current_date)
    print("Last run date:", last_run_date)

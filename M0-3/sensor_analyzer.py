import csv
import os
import math

def load_data(file_path):
    """读取数据，并返回时间和数值列表"""
    times = []
    values = []
    try:
        with open(file_path, "r", encoding="utf-8") as f: # 这里我补了冒号
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # 你刚才说 CSV 已经改成英文表头了
                    t = float(row["time"])
                    v = float(row["value"]) # 这里我补全了你刚才断掉的代码
                    times.append(t)
                    values.append(v)
                except ValueError:
                    print(f"数据格式有误，跳过该行: {row}")
    except FileNotFoundError:
        print(f"找不到文件: {file_path}")
        return [], []
    
    return times, values

# 下面是主程序调用，保证跑起来有输出
if __name__ == "__main__":
    file_name = "sensor_data.csv"
    print(f"正在读取文件: {file_name}")
    
    # 调用函数
    t_list, v_list = load_data(file_name)
    
    # 打印结果看看
    if len(t_list) > 0:
        print("--- 读取成功！ ---")
        print(f"一共读取了 {len(t_list)} 行数据。")
        print(f"前 3 个时间点: {t_list[:3]}")
        print(f"前 3 个数值:   {v_list[:3]}")
    else:
        print("--- 读取失败或没有数据 ---")
import yaml  #引入配置
import csv   #引入数据文件
import math  #引入数学库

#定义函数load_config()，用于加载配置文件
def load_config(config_path):
    try:
        with open(config_path,encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        return cfg    
    except FileNotFoundError:
        print("Config file not found.")
        return None
    
cfg = load_config("config.yaml")

#CONFIG_PATH = "config.yaml"
#with open(CONFIG_PATH) as f:
#cfg = yaml.safe_load(f)

#从读取到的配置字典（cfg）中，提取出后续程序需要的具体参数（文件名和列名）
csv_path = cfg["input_csv"]
col_x = cfg["columns"]["x"]
col_y = cfg["columns"]["y"]

#定义函数load_data()，用于加载数据文件
def load_data(csv_path, col_x, col_y):
    xs = []
    ys = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try: 
                xs.append(float(row[col_x]))
                ys.append(float(row[col_y]))
            except ValueError:
                print("Data error in row:", row)
    return xs, ys
xs, ys = load_data(csv_path, col_x, col_y)

def mean(data):
    mean = sum(data) / len(data)
    return mean
n = len(xs)
sum_x = sum(xs)
sum_y = sum(ys)
mean_x = mean(xs)
mean_y = mean(ys)

#定义函数calculate_corr()，用于计算皮尔逊相关系数
def calculate_corr(xs, ys):
    mean_x = mean(xs)
    mean_y = mean(ys)
    dx = 0.0
    dy = 0.0
    prod = 0.0
    for i in range(n):
        a = xs[i] - mean_x
        b = ys[i] - mean_y
        dx += a * a
        dy += b * b
        prod += a * b
#求r的公式里要开平方，此处修改
    denom = math.sqrt(dx * dy)
    r = prod / denom if denom != 0 else 0
    return r
r = calculate_corr(xs, ys)

if __name__ == "__main__":
    # 下面的代码只在直接运行此文件时执行
    my_config = load_config("config.yaml")
    if my_config is not None:
        print("Configuration loaded successfully.")
    else:
        print("Failed to load configuration.")

print("n =", n)
print("mean_x =", mean_x)
print("mean_y =", mean_y)
print("r =", r)

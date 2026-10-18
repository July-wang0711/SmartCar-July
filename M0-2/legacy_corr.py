import yaml  #引入配置
import csv   #引入数据文件
import math  #引入数学库

#定义函数load_config()，用于加载配置文件
def load_config(config.yaml):
    try:
        with open(config.yaml) as f:
            cfg = yaml.safe_load(f)
        return cfg    
    except FileNotFoundError:
        print("Config file not found.")
        return None
   
#cfg = load_config("config.yaml")

if __name__ == "__main__":
    # 下面的代码只在直接运行此文件时执行
    my_config = load_config("config.yaml")
    if my_config is not None:
        print("Configuration loaded successfully.")
    else:
        print("Failed to load configuration.")

#CONFIG_PATH = "config.yaml"
#with open(CONFIG_PATH) as f:
#cfg = yaml.safe_load(f)

csv_path = cfg["input_csv"]
col_x = cfg["columns"]["x"]
col_y = cfg["columns"]["y"]

xs = []
ys = []

with open(csv_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        xs.append(float(row[col_x]))
        ys.append(float(row[col_y]))

n = len(xs)

sum_x = 0.0
sum_y = 0.0
for i in range(n):
    sum_x = sum_x + xs[i]
    sum_y = sum_y + ys[i]

mean_x = sum_x / n
mean_y = sum_y / n

dx = 0.0
dy = 0.0
prod = 0.0
for i in range(n):
    a = xs[i] - mean_x
    b = ys[i] - mean_y
    dx = dx + a * a
    dy = dy + b * b
    prod = prod + a * b

#求r的公式里要开平方，此处修改
denom = math.sqrt(dx * dy)  
r = prod / denom

print("n =", n)
print("mean_x =", mean_x)
print("mean_y =", mean_y)
print("r =", r)

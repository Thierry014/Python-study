from pathlib import Path

path = Path()

for file in path.glob('*'):
    print(file)

# 找到的是父级 开始
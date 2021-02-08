# 安装包
# pip install wheel
# pip install pandas

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# matplotlib inline
import seaborn as sns
print("Setup Complete")


# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Print the first/last 5 rows of the data
fifa_data.head()
fifa_data.tail()
fifa_data.all()

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# 线图 =>Trends
# Line chart showing how FIFA rankings evolved over time 
sns.lineplot(data=fifa_data)

list(spotify_data.columns)
# line chart based on column name 
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# 柱图 =>Relationship 
sns.barplot(x=..., y=....)
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# 热点图  =>Relationship (都是数字才看的清趋势)
sns.heatmap(data=flight_data, annot=True)

# 散点图 (看趋势)  =>Relationship 
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
# 给散点图添加回归线 // 根据回归线的斜率 来判断趋势
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

sns.swarmplot(x=insurance_data['smoker'],y=insurance_data['charges'])''

# 分布图 (Histgram, kdeplot, 2D kdeplot ) => Distribution 
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
# plt.legend() 强制出现 => 多图合并 

change style
sns.set_style("dark")
(1)"darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks"

绘图总结

1. 找到文件by path
2. 用 pandas 读取csv文件 (参数X2或3 文件本身, col-index, )
3. 规定成像大小 .figure
4. 作图
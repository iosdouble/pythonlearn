import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS  # 导入了pygal以及应用于图标的Pygal样式

# 1.执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:java&sort=stars"
r = requests.get(url)
print("status_code:", r.status_code)

# 2将API响应存储在一个变量中。
response_dict = r.json()

# 3.处理响应字典
print("Total repositories:", response_dict['total_count'])

# 4.将字典列表存储在repo_dict中，并打印获得了多少个仓库信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

# 5. 创建两个空列表，用于存储将包含在图表中的信息
names, stars = [], []

# 6.将项目的名称和获得的星数追加到这些列表的末尾
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 7.可视化
my_style = LS("#333366", base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

my_config = pygal.Config()
my_config.x_label_rotation = 45  # 让标签绕X轴旋转45度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 设置图标标题
my_config.label_font_size = 14  # 设置副标签字体大小（X轴的项目名以及Y轴的大部分字体）
my_config.major_label_font_size = 18  # 设置主标签字体大小（主标签是Y轴上为5000整数倍的刻度）
my_config.truncate_label = 15  # 将较长的项目名缩短为15个字符，鼠标悬停上去会显示全部
my_config.show_y_guides = False  # 隐藏表中的水平线
my_config.width = 1000  # 自定义宽度

# 9.给图标指定标题
chart = pygal.Bar(my_config, style=my_style)  # 创建Bar的实例时，将my_config作为第一个实参，通过一个实参传递所有配置
chart.title = 'Most-starred Python Project on GitHub'
chart.x_labels = names

# 10.生成图标
chart.add('', stars)
chart.render_to_file('python_repo2.svg')


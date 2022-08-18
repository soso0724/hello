import pandas as pd

# 导入pandas后需要处理excel文件还需要安装xlrd
# 保存为excel文件格式需要安装xlwt
# 需要筛选的表格
data = pd.read_excel("/Users/用户名/Desktop/2022年事业单位招考信息表.xls")
# 第一步筛选专业,.str.contains 的使用就要求这个字段必须是字符串，不能掺杂数字，有些表格带数字筛选时会有如下报错
# ValueError: Cannot mask with non-boolean array containing NA / NaN values
# 解决方法：na=False，意思就是，遇到非字符串的情况，直接忽略。也可以写na=True，意思就是遇到非字符串的情况，计为筛选有效。
# 参考方案：https://blog.csdn.net/chaodaibing/article/details/108138312
dtt = data[data["专业"].str.contains("计算机", na=False)]
# 筛选学历要求
www = dtt[dtt["学历要求"].str.contains("本科", na=False)]
# 筛选年龄限制,筛选表格前加"~"表示筛选不包含匹配条件的内容，反向筛选
third = www[~ www["其它要求"].str.contains("限2022届高校毕业生", na=False)]
# 保存结果
third.to_excel("/Users/用户名/Desktop/筛选后的职位2.xls")
print(third)
07【python提取省份地区地址以及地区编码】

# 方法一

使用正则表达式：

下面代码查找的优先级是 **市-->省-->自治区-->县-->区**

代码实现：

```python
import re

PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:市|省|自治区|县|区)){1}'  #这里的 1 代表提取市，如果是2的话运行出来的结果会是  ”深圳市罗湖区”
data = '''11111111111231231深圳市罗湖区中药制造业创新中心有限公司经典名方麦门冬汤复方制剂开发研究罗湖区'''
pattern = re.compile(PATTERN)
m = pattern.search(data)
place = m.group()
print(place)
#深圳市
```

运行结果：

![image.png](https://s2.loli.net/2022/11/24/zwhS5uPFoi3rUkq.png)

在练习一下：

```python
PATTERN_1 = r'([\u4e00-\u9fa5]{2,5}?(?:省|市|自治区|县|区)){1}'
place = "湖北省武汉市武昌区湖北大学368号"
pattern = re.compile(PATTERN_1)
m = pattern.search(place)
place_p = m.group()
print(place_p)

#湖北省
```



功能更加全面：

```python
#description: 从字符串中提取省市县等名称
 
import re
import sys
 
#匹配规则必须含有u,可以没有r
#这里第一个分组的问号是懒惰匹配,必须这么做
PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道)){1}'
data_list = ['北京市南瓜村', '陕西省西安市雁塔区大村', '西班牙镇街道', '北京市海淀区', '黑龙江省佳木斯市汤原县大村', '内蒙古自治区赤峰市',
'贵州省黔南州贵定县', '新疆维吾尔自治区伊犁州奎屯市']
 
for data in data_list:
    country = ''
    province = ''
    city = ''
    district = ''
    #pattern = re.compile(PATTERN3)
    pattern = re.compile(PATTERN)
    m = pattern.search(data)
    if not m:
        print (country + '|||')
        continue
    #print m.group()
    country = '中国'
    if m.lastindex >= 1:
        province = m.group(1)
    if m.lastindex >= 2:
        city = m.group(2)
    if m.lastindex >= 3:
        district = m.group(3)
    out = '%s|%s|%s|%s' %(country, province, city, district)
    print (out)
```

![](https://img-blog.csdnimg.cn/368f29c8b923449b960c92b7d6a6c541.png)

![](https://img-blog.csdnimg.cn/711330cb5e0b463b9122f39c175538e4.png)

# 方法二

安装 cpca

使用：

```python
import cpca

data = '''
(网)广州新溪项目河涌整治景观提升设计招标
'''
place = ''
place_list = list()
place_list.append(data)
integrity_place = cpca.transform(place_list)
print(integrity_place)
#      省    市     区                  地址  adcode
# 0  广东省  广州市  None  新溪项目河涌整治景观提升设计招标\n  440100
print(integrity_place['省'][0])
# 广东省
```

**注意事项**
cpca.transform()中的参数需为**可迭代类型**(如list，pandas的Series类型等)，函数会将其转换为一个DataFrame

![image.png](https://s2.loli.net/2022/11/24/nZ1AR5vVSheQdxE.png)
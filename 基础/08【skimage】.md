08【skimage】

# 1、skimage的简介

skimage即是Scikit-Image。基于python脚本语言开发的数字图片处理包，比如PIL,Pillow, opencv, scikit-image等。

PIL和Pillow只提供最基础的数字图像处理，功能有限。
opencv实际上是一个c++库，只是提供了python接口，更新速度非常慢。
scikit-image是基于scipy的一款图像处理包，**它将图片作为numpy数组进行处理**，正好与matlab一样，因此，我们最终选择scikit-image进行数字图像处理。

skimage包的全称是scikit-image SciKit (toolkit for SciPy) ，它对scipy.ndimage进行了扩展，提供了更多的图片处理功能。它是由python语言编写的，由scipy 社区开发和维护。
skimage包由许多的子模块组成，各个子模块提供不同的功能。

# 2、主要子模块列表如下

| 子模块名称   | 主要实现功能                                                |
| ------------ | ----------------------------------------------------------- |
| io           | 读取、保存和显示图片或视频                                  |
| data         | 提供一些测试图片和样本数据                                  |
| color        | 颜色空间变换                                                |
| filters      | 图像增强、边缘检测、排序滤波器、自动阈值等                  |
| draw         | 操作于numpy数组上的基本图形绘制，包括线条、矩形、圆和文本等 |
| transform    | 几何变换或其它变换，如旋转、拉伸和拉东变换等                |
| morphology   | 形态学操作，如开闭运算、骨架提取等                          |
| exposure     | 图片强度调整，如亮度调整、直方图均衡等                      |
| feature      | 特征检测与提取等                                            |
| measure      | 图像属性的测量，如相似性或等高线等                          |
| segmentation | 图像分割                                                    |
| restoration  | 图像恢复                                                    |
| util         | 通用函数                                                    |

## 安装：

```python
pip install scikit-image -i https://pypi.douban.com/simple/
```



![image.png](https://s2.loli.net/2022/11/25/GmFPQxAUvlg2j6a.png)

# 3、图片显示

在skimage中io.read可以读取目标路径下（需要自己导入）的图像，data库中则提供了可以直接使用的图片。

代码如下：

```python
# 运行以下代码，完成图片的显示

#导入数字图像处理包skimage的子模块data，便于之后使用其中的图片
from skimage import data

#导入绘图库（matplotlib.pyplot是一些命令行风格函数的集合，使matplotlib以类似于MATLAB的方式工作。）
import matplotlib.pyplot as plt

img = data.coffee()   #导入data模块中的coffee的图片
plt.imshow(img)     #接收img中的图像
plt.show()          #显示结果，展示图片
```

# 4、图片的基本属性信息

1. 路径表示：
   '/‘代表根目录或路径层次之间的分隔，’./'代表当前路径。
2. 使用skimage中的io子模块的图片读取、显示 。
3. 了解图片的基本属性，如图片的尺寸、像素个数、通道、宽度、高度、像素值等 

```python
from skimage import io        #导入io模块，以读取目标路径下的图片
img = io.imread('./dog.jpg')  #读取dog.jpg文件
print(type(img))     #显示类型
print(img.shape)     #显示尺寸
print(img.shape[0])  #显示高度
print(img.shape[1])  #显示宽度
print(img.shape[2])  #显示图片通道数
print(img.size)      #显示总像素数
print(img.max())     #显示最大像素值
print(img.min())     #显示最小像素值
print(img.mean())    #像素平均值
print(img[0][0])     #指定像素点的像素值
io.imshow(img)       #io模块下显示图像
io.show()            #显示图像
```

![image.png](https://s2.loli.net/2022/11/25/1UgwKurxlV8mYq9.png)

# 5、图像通道

RGB图像一般有三个通道，通过编程查看效果：

代码如下：

```python
from skimage import io           #导入io模块
img=io.imread('./dog.jpg')       #读取dog.jpg文件
import matplotlib.pyplot as plt  #导入绘图库

plt.figure(figsize=(16,10))        #figure(figsize=None); figsize:指定整体图像的宽和高，单位为英寸。

#显示R通道图像（灰度图像）；
plt.subplot(2,2,1) #把显示界面分割成2*2的网格；三个参数分别表示行数，列数，图形标号。
# img[:, :, 0]表示图像单通道的第一个通道。
# cmap = 'gray' 显示出来的图像为灰度图像。
plt.imshow(img[:,:,0],cmap='gray') 

#显示G通道图像（灰度图像）
plt.subplot(2,2,2)
plt.imshow(img[:,:,1],cmap='gray')

#显示B通道图像（灰度图像）
plt.subplot(2,2,3)
plt.imshow(img[:,:,2],cmap='gray')

#显示原图像（彩色图像）
plt.subplot(2,2,4)
plt.imshow(img)

#输入plt.show()指令才能使之前的图像全部显示
plt.show()
```

![image.png](https://s2.loli.net/2022/11/25/DcE41l5S7UTvRNO.png)

# 6、生成结构化元素

这个例子展示了如何使用skimage中的函数。生成结构元素的形态学。每个图的标题表示函数的调用。

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from skimage.morphology import (square, rectangle, diamond, disk, cube,
                                octahedron, ball, octagon, star)
#正方形、长方形、菱形、圆盘、立方体、八面体、球体、八角形、星形
# Generate 2D and 3D structuring elements.
struc_2d = {
    "square(15)": square(15),
    "rectangle(15, 10)": rectangle(15, 10),
    "diamond(7)": diamond(7),
    "disk(7)": disk(7),
    "octagon(7, 4)": octagon(7, 4),
    "star(5)": star(5)
}

struc_3d = {
    "cube(11)": cube(11),
    "octahedron(5)": octahedron(5),
    "ball(5)": ball(35),
"ball(5)": ball(35),
}

# Visualize the elements.
fig = plt.figure(figsize=(8, 8))

idx = 1
#tems()函数以列表返回可遍历的（键值）元组数组。
'''
plt.text(x, y, string, weight="bold", color="b")
x: 注释文本内容所在位置的横坐标
y：注释文本内容所在位置的纵坐标
string：注释文本内容,struc[i, j]为数0、1
weight：注释文本内容的粗细风格
'''
for title, struc in struc_2d.items():
    ax = fig.add_subplot(4, 4, idx)#3行3列，位置为
    ax.imshow(struc, cmap="Greens", vmin=0, vmax=12)#ax参数用于限定数值的范围，只将vmin和vmax之间的值进行映射，用法如下
    for i in range(struc.shape[0]):
        for j in range(struc.shape[1]):
            ax.text(j, i, struc[i, j], ha="center", va="center", color="w")
    ax.set_axis_off()
    ax.set_title(title)
    idx += 1

for title, struc in struc_3d.items():
    ax = fig.add_subplot(4, 4, idx, projection=Axes3D.name)
    ax.voxels(struc)
    ax.set_title(title)
    idx += 1

fig.tight_layout()
plt.show()
```

![image.png](https://s2.loli.net/2022/11/25/joel16bVx7aJYS8.png)

# 7、图像/阵列上的块视图

这个例子演示了`skimage.util()`中的view_as_blocks的使用。当一个人想对非重叠图像块执行局部操作时，块视图是非常有用的。我们用skimage中的astronaut数据，并将其“切分”为方方面面。然后，在每个块上，我们要么汇集该块的平均值，最大值或中值。结果显示在一起，连同一个三阶的样条插值的原始宇航员图像缩放
```python
import numpy as np
from scipy import ndimage as ndi
from matplotlib import pyplot as plt
import matplotlib.cm as cm

from skimage import data
from skimage import color
from skimage.util import view_as_blocks


# get astronaut from skimage.data in grayscale
l = color.rgb2gray(data.astronaut())
#img=skimage.io.imread('11.jpg',)
#l = color.rgb2gray(img)
# size of blocks
block_shape = (4,4)

#将宇航员图片分为矩阵块（大小为block_shape）
view = view_as_blocks(l, block_shape)

# 最后两个维度合二为一，变为数组方便操作
#img.shape[0]:图像的垂直尺寸(高度) img.shape[1]:图像的水平尺寸(宽度)
flatten_view = view.reshape(view.shape[0], view.shape[1], -1)

# 通过取每个块的“均值”、“最大值”或“中值”重新采样图像。mean()函数功能：求取均值
mean_view = np.mean(flatten_view, axis=2)
max_view = np.max(flatten_view, axis=2)
median_view = np.median(flatten_view, axis=2)

# 画子图，sharex和sharey：表⽰坐标轴的属性是否相同
fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
ax = axes.ravel()#将多维数据展平为⼀维数据，它相当于 reshape(-1, order=order) 。

'''
https://vimsky.com/examples/usage/python-scipy.ndimage.zoom.html
https://www.jianshu.com/p/909851f46411
ndi.zoom(input,zoom,output=None,order,mode='constant',cval=0.0,prefilter=True)缩放数组。使用请求顺序的样条插值对数组进行缩放。
input: 以数组形式输入图片
zoom:浮点数或数组。如果是一个浮点数，对每一个轴放缩相同的倍数。如果是一个数组，则对每一个轴分配一个值。
output:输出，默认为None
order:整型（范围0-5）样条插值的顺序，默认为3。详见后续
'''
l_resized = ndi.zoom(l, 2, order=3)
ax[0].set_title("Original rescaled with\n spline interpolation (order=3)")
ax[0].imshow(l_resized, extent=(-0.5, 128.5, 128.5, -0.5),
             cmap=cm.Greys_r)

ax[1].set_title("Block view with\n local mean pooling")
ax[1].imshow(mean_view, cmap=cm.Greys_r)

ax[2].set_title("Block view with\n local max pooling")
ax[2].imshow(max_view, cmap=cm.Greys_r)

ax[3].set_title("Block view with\n local median pooling")
ax[3].imshow(median_view, cmap=cm.Greys_r)

for a in ax:
    a.set_axis_off()

fig.tight_layout()
plt.show()
```

![image.png](https://s2.loli.net/2022/11/25/BbFRTkUDOouZNLK.png)

# 8、使用简单的 [NumPy](https://so.csdn.net/so/search?q=NumPy&spm=1001.2101.3001.7020) 操作来处理图像

此脚本说明了如何使用基本的 NumPy 操作，例如切片、屏蔽和花式索引，以修改图像的像素值。

![image.png](https://s2.loli.net/2022/11/25/ax1vz2Ir7opjwcs.png)

![image.png](https://s2.loli.net/2022/11/25/izceGHB3fogRvpr.png)





# 9、skimage自带图片

| 图片名称             | 说明     |
| -------------------- | -------- |
| astronaut            | 宇航员   |
| binary_blobs         | 二元斑点 |
| camera               | 相机     |
| checkerboard         | 棋盘     |
| chelsea              | 猫       |
| clock                | 时钟     |
| coffee               | 一杯咖啡 |
| coins                | 硬币     |
| horse                | 马       |
| hubble_deep_field    | 星空     |
| immunohistochemistry | 结肠图片 |
| logo                 | 商标     |
| moon                 | 月球表面 |
| page                 | 书页内容 |
| rocket               | 火箭     |
| text                 | 文字图片 |

```python
from skimage import io, data
img = data.hubble_deep_field()
io.imshow(img)
io.show()
```

​	![image.png](https://s2.loli.net/2022/11/26/SjgGZ8T5lI7H1AP.png)
​	打印出存储图片的地址：

```python
from skimage import data_dir
print (data_dir)
```

# 	10、保存图片

使用 **io.imsave(fname, arr)** 函数进行保存,

- 参数fname: 表示保存的路径和名称
- 参数arr：表示需要保存的数组变量

```python
from skimage import io, data

img = data.hubble_deep_field()
io.imshow(img)
io.imsave('hubble_deep_field.jpg', img)
```

> 注：保存图片同时也起到了转换格式的作用，若读取的是png格式图片，当保存为jpg时，则图片从png格式转换为jpg格式图片。

# 11、图像像素访问与裁剪

图片读入程序后，以numpy数组方式存储，因此对numpy数组的操作，都可以用于图片数组，对数组元素的访问，实际上就是对图片像素点的访问。

## 像素读取

对 **彩色图片** 的像素点访问方式如下

```python
img[i, j, c]
```

其中：

- i 表示图片的行数
- j 表示图片的列数
- c 表示图片的通道数(RGB三通道分别对应0, 1, 2)。

坐标从左上角开始

对 **灰度图片** 的像素点访问方式如下

```python
gray[i, j]
```

例如， 对data中宇航员图片的B通道中的第20行10列的像素值

```python
from skimage import io, data

img = data.astronaut()
pixel = img[20, 10, 2]
print(pixel)
```

例如，显示红色单通道图片的程序如下

```python
from skimage import io, data

img = data.astronaut()
R = img[:, :, 0]
io.imshow(R)
io.show()
```

## 像素修改

例如，对宇航员图片随机添加椒盐噪声

```python
from skimage import io, data
import numpy as np

img = data.astronaut()

# 随机生成5000个椒盐点
rows, cols, dims = img.shape

for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

io.imshow(img)
io.show()
```

![image.png](https://s2.loli.net/2022/11/26/Ku1tEUCLG9hM27N.png)

## 图片裁剪

由于图片是以numpy数组进行存储，因此对于数组的裁剪，就是对图片的裁剪

例如，对宇航员图片进行裁剪

```python
from skimage import io, data

img = data.astronaut()
partial_img = img[50:150, 170:270, :]
io.imshow(partial_img)
io.show()
```

对多个像素点进行操作时， 使用数组切片方式进行访问， 切片方式访问的是指定间隔内下标对应的像素点。以下是一些例子

```python
img[i,:] = im[j,:]      # 将第 j 行的数值赋值给第 i 行

img[:,i] = 100          # 将第 i 列的所有数值设为 100

img[:100,:50].sum()     # 计算前 100 行、前 50 列所有数值的和

img[50:100,50:100]      # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean()           # 第 i 行所有数值的平均值

img[:,-1]               # 最后一列

img[-2,:] (or im[-2])   # 倒数第二行
```

以下是两个对图片的像素值进行访问和修改的例子

例1： 将宇航员图片进行二值化，像素值大于128的变为1, 否在变为0

```python
from skimage import io, data, color

img = data.astronaut()

img_gray = color.rgb2gray(img)
rows, cols = img_gray.shape

for i in range(rows):
    for j in range(cols):
        if (img_gray[i, j] <= 0.5):
            img_gray[i, j] = 0
        else:
            img_gray[i, j] = 1
io.imshow(img_gray)
io.show()
```

![image.png](https://s2.loli.net/2022/11/26/Wg3pj1VnSqYlLUt.png)

例2： 使用color模块的rgb2gray()函数，将彩色三通道图片转换为灰度图片，转换结果为float64类型的数组，范围在[0,1]之间

```python
from skimage import io, data

img = data.astronaut()

img_idx_modified = img[:, :, 0] > 170
print(img_idx_modified)
img[img_idx_modified] = [0, 255, 0]

io.imshow(img)
io.show()
```

![image.png](https://s2.loli.net/2022/11/26/VWzFMjOXlpmiyYu.png)

> 这个例子先对R通道的所有像素值进行判断，如果大于170，则将这个地方的像素值变为[0,255,0], 即G通道值为255，R和B通道值为0

# 12、图像数据类型以及颜色空间转换

## 图像数据类型

在skimage中，一张图片以numpy数组形式存储，数组的数据类型有很多中，相互之间可以转换，数据类型以及取值范围如下表所示

| 数据类型 | 数值范围                                          |
| -------- | ------------------------------------------------- |
| uint8    | 0 to 255                                          |
| uint16   | 0 to 65535                                        |
| uint32   | 0 to 232−1232−1                                   |
| float16  | 半精度浮点数：16位，正负号1位，指数5位，精度10位  |
| float32  | 单精度浮点数：32位，正负号1位，指数8位，精度23位  |
| float64  | 双精度浮点数：64位，正负号1位，指数11位，精度52位 |
| float    | -1 to 1 or 0 to 1                                 |
| int8     | -128 to 127                                       |
| int16    | -32768 to 32767                                   |
| int32    | −231−231 to 232−1232−1                            |

一张图片的像素值范围是[0,255], 因此默认类型是unit8, 可用如下代码查看数据类型：

```python
from skimage import io, data

img = data.astronaut()

print(img.dtype.name)
```

在上面的表中，特别注意的是float类型，它的范围是[-1,1]或[0,1]之间。一张彩色图片转换为灰度图后，它的类型就由unit8变成了float

**uint8转为float**

```python
from skimage import data, img_as_float

img = data.astronaut()
print(img.dtype.name)

dst = img_as_float(img)
print(dst.dtype.name)
dst
```

**float转为uint8**

```python
from skimage import img_as_ubyte
import numpy as np

img = np.array([0, 0.5, 1], dtype=float)
print(img.dtype.name)

dst = img_as_ubyte(img)
print(dst.dtype.name)
```

float转为uint8,可能会造成数据损失，因此会有警告

除了如上两种转换以外，还有其他的一些类型转换，如下表:

| 函数名       | 描述                             |
| ------------ | -------------------------------- |
| img_as_float | Convert to 64-bit floating point |
| img_as_ubyte | Convert to 8-bit uint            |
| img_as_uint  | Convert to 16-bit uint           |
| img_as_int   | Convert to 16-bit int            |

# 13、颜色空间及转换	

除了直接转换可以改变数据类型外，还可以通过图像的颜色空间转换来改变数据类型。

常用的颜色空间有灰度空间、rgb空间、hsv空间和cmyk空间。颜色空间转换以后，图片类型都变成了float型。

所有的颜色空间转换函数，都放在skimage的color模块内

例1： **RGB转为灰度图**

```python
from skimage import io,data,color
img=io.imread('./蒜.jpg')
gray=color.rgb2gray(img)
io.imshow(gray)
io.show()
```

<img src="https://s2.loli.net/2022/11/26/z8by7pIoZvDmQl9.png" alt="image.png" style="zoom:50%;" />

其它的转换，用法都是一样的，列举常用的如下：

skimage.color.rgb2grey(rgb)

skimage.color.rgb2hsv(rgb)

skimage.color.rgb2lab(rgb)

skimage.color.gray2rgb(image)

skimage.color.hsv2rgb(hsv)

skimage.color.lab2rgb(lab)实际上，上面的所有转换函数，都可以用一个函数来代替

skimage.color.convert_colorspace(arr, fromspace, tospace)

```python
from skimage import io,data,color
from skimage.color import convert_colorspace
import skimage
img = io.imread('./蒜.jpg')
# img = color.convert_colorspace(img, , HSV)
img = skimage.color.convert_colorspace(img, 'RGB', 'rgb cie')
io.imshow(img)
```

表示将arr从fromspace颜色空间转换到tospace颜色空间。

例1： **RGB转为HSV**

```python
from skimage import io, data, color

img = data.coffee()
hsv = color.convert_colorspace(img, 'RGB', 'HSV')
io.imshow(hsv)
io.show()
```

<img src="https://s2.loli.net/2022/11/26/PmWYrM4j7gNqTOZ.png" alt="image.png" style="zoom:25%;" />

在color模块的颜色空间转换函数中，还有一个比较有用的函数是

skimage.color.label2rgb(arr), 可以根据标签值对图片进行着色。以后的图片分类后着色就可以用这个函数。

例：将coffee图片分成三类，然后用默认颜色对三类进行着色

```python
from skimage import io,data,color
import numpy as np

img=data.coffee()
gray=color.rgb2gray(img)
rows,cols=gray.shape

labels=np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if(gray[i,j]<0.4):
            labels[i,j]=0
        elif(gray[i,j]<0.75):
            labels[i,j]=1
        else:
            labels[i,j]=2
dst=color.label2rgb(labels)

io.imshow(dst)
io.show()
```

<img src="https://s2.loli.net/2022/11/26/Im3wdSN4ifAhT6l.png" alt="image.png" style="zoom:50%;" />



# 14、图片强度调整，如亮度、对比度、直方图均衡等

 

exposure.adjust_gamma(image, gamma=1)

##  亮度变亮

```python
img1 = skimage.exposure.adjust_log(img) #对数调整  变亮
io.imshow(img1)
```

<img src="https://s2.loli.net/2022/11/26/f6KVTmE3gQLJiWn.png" alt="image.png" style="zoom:33%;" />

## 判断图像对比度是否偏低

`exposure.is_low_contrast(image)`

## 增强对比度

```python
newImage=skimage.exposure.rescale_intensity(img, in_range='image', out_range='dtype') 
io.imshow(newImage)
```

<img src="https://s2.loli.net/2022/11/26/CAyRNeIEXopxk1T.png" alt="image.png" style="zoom:33%;" />

```tex
in_range 表示输入图片的强度范围，默认为'image', 表示用图像的最大/最小像素值作为范围
out_range 表示输出图片的强度范围，默认为'dype', 表示用图像的类型的最大/最小值作为范围
默认情况下，输入图片的[min,max]范围被拉伸到[dtype.min, dtype.max]，如果dtype=uint8, 那么dtype.min=0, dtype.max=255
 
如果想输入图片像素值等比例缩放，用in_range
mat=exposure.rescale_intensity(tmp,in_range=(0,255))
原像素值除以255，如果参数in_range的[min,max]范围要比原始像素值的范围[min,max] 大或者小，那就进行裁剪
 
如果一个数组里面有负数，现在想调整到正数，就使用out_range参数
exposure.rescale_intensity(image, out_range=(0, 127))
```

exposure.histogram(image, nbins=256)
在numpy包中，也提供了一个计算直方图的函数histogram(),两者大同小义。np.histogram(image, bins=2)


返回一个tuple（hist, bins_center), 前一个数组是直方图的统计量，后一个数组是每个bin的中间值
nbins的意思是分成几个级别的灰度进行统计。

##  直方图均衡化

```python
img2 = skimage.exposure.equalize_hist(img) 
io.imshow(img2)
```

<img src="https://s2.loli.net/2022/11/26/cYGP7glNO68RTqK.png" alt="image.png" style="zoom: 50%;" />

```python
clip_limitnumber=3
kernel_size = 64
img3 = skimage.exposure.equalize_adapthist(img, kernel_size=kernel_size, clip_limit=clip_limitnumber, nbins=256)  
io.imshow(img3)
```

<img src="https://s2.loli.net/2022/11/26/qLlUBbeE8nfaScF.png" alt="image.png" style="zoom: 50%;" />

如果一副图像的像素占有很多的灰度级而且分布均匀，那么这样的图像往往有高对比度和多变的灰度色调。直方图均衡化就是一种能仅靠输入图像直方图信息自动达到这种效果的变换函数。它的基本思想是对图像中像素个数多的灰度级进行展宽，而对图像中像素个数少的灰度进行压缩，从而扩展取值的动态范围，提高了对比度和灰度色调的变化，使图像更加清晰。

## 绘制直方图用 

```python
img = img.flatten()
plt.hist(img)
```

<img src="https://s2.loli.net/2022/11/27/nHthDaji1EleXco.png" alt="image.png" style="zoom: 50%;" />





# 15、姿态识别的相关：

https://github.com/google-coral/project-bodypix

https://github.com/guiggh/hand_pose_action#terms

https://github.com/hassony2/handobjectconsist

https://github.com/fmahoudeau/ShelfNet-Human-Pose-Estimation

https://github.com/DeepLabCut/DeepLabCut

https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases

https://www.aiuai.cn/aifarm712.html

https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/quick_start.md#quick-start


# 参考文献

参考1[点击跳转](https://blog.csdn.net/u012300744/article/details/80083282)

参考2[点击跳转](https://blog.csdn.net/lusics/article/details/89019453?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control)

参考3[点击跳转](https://blog.csdn.net/abcx3261/article/details/85987650)
# Wavelength_linearize
## 波长归一化程序使用说明

1. 文件名是`xx_single_csv2.py`
1. 先要用Excel之类的工具将原始标定数据打开，在波长那一栏，改小数点位数为零，然后文件另存为csv格式
1. `np.loadtxt()`函数中将文件名改成刚刚得到的csv文件
1. 观察原标定文件中有多少个整数波长点，在程序的矩阵定义`result=np.zeros((1027,3))`中手工改大小
1. 运行即可，生成文件`002.txt`即为各波长处的采样点分布

## 波长线性化处理程序集
一共有4个小程序

 - calculate_distribution_pattern.py
 - data_linearization.py
 - initialization.py
 - recalculation.py

具体操作规程如下：

1. 打开某一未标定的测量数据（我们称之为RAW数据），画折线图，记下正反两个相邻峰的横坐标位置，填入`initialization.py`中(分别是`peak_1`和`peak_2`)，滤色片的相应波长也在该文件中填入
1. 切换到`calculate_distribution_pattern.py`中，运行即可，将得到一个文件，`distribution.txt`，即分布列
1. 再切换到`data_linearization.py`中，`b=np.loadtxt()`里填入你要线性化的原始数据，运行，会输出线性化数据列到文件`linearization.txt`中。（此处将来可改进，根据`b=np.loadtxt()`中导入的原始数据动态改变输出的文件名。）
1. 这一步运行一个支线程序，是在线性化的基础上，利用ZEMAX中得到的波长-光栅摆角曲线，反过来计算线性采样点的波长。运行即可，标定后的结果保存为文件`recalculation.txt`。

这个计算方法的结果，目前还不太准确，需要进一步优化。

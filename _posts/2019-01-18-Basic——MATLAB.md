---
layout: post
title: "MATLAB操作整理"
date: 2019-01-18
description: ""
tag: MATLAB
---

```matlab
基本操作
	format格式
	;禁止输出
	... 代码延伸至下一行
	' 转置 （.' 转置不计算共轭）
	clear 清空工作区
	[a:b:c] 闭区间
	linspace logspace 自动确定间隔
	.^ 次方
	.* 数组乘法（对每个元素操作）
	*  数量乘法（单个数字*矩阵）/ 矩阵乘法
	.\ 左除 ./ 右除
	conj 共轭复数
	dot 点乘
	cross 叉乘
	A(1) 索引
	A(4:6) 切片

向量和矩阵
	eye(4) 单位阵
	zeros(m,n) 零矩阵
	ones(m,n)
	引用矩阵元素
		A(m,n) 索引
		A(:,2) 切片
		A(2,:)=[] 数组删除
		F = A([1,2,1],:)
	求解
		det(A) 行列式 系数矩阵A det!=0才有解
		线性系统求解 右除 P34
		rank 求秩 增广矩阵[A b] rank(A) = rank(A b)有一解 > 有无数解
	inv 求逆 pinv 伪逆
	高斯消元 rref
	LU QR SVD P42

绘图与图形
	基本绘图 plot 行标签 标题
	fplot 自动绘图 （矩阵相乘报错：Inner matrix dimensions must agree）
	网格 grid on
	坐标轴 axis
	多函数绘图 线形 plot(x,y,线,x2,y2,线...)
	图例 legend
	颜色 加参数... r,b 可以和线形叠加
	坐标轴比例 axis
	子图 subplot(row,col,n)
	图像重叠 hold on
	极坐标绘图 polar
	对数图像 loglog semilogx semilogy
	离散绘图 P67
		针头图 stem
	等高线图
		meshgrid 生成二维矩阵
		contour 等高线图 contour3 三维等高线图
		set 加说明标签 P72
		surface 加平面
	三维图像 mesh
		surf 颜色填充 surfc 带等高线
		surfl 光照和阴影

统计
	bar 柱状图 barh 水平柱状图 bar3 三维柱状图
	分组柱状图 P85
	mean 平均数/列平均数
	median 中位数 std 标准差

编程基础
	定义函数 P88 function 返回值 = 函数名(参数)
	不相等 ~= 不能用!
	disp 输出信息 input 获取输入
	循环都不用在条件加括号
		for循环 P90 for 变量 = 开始:步进[默认为1]:中止 语句块 end
		while 条件 语句块 end
	swtich P96 不需要break
	
代数方程求解
	syms 定义符号变量 （若使用2018版 大部分方程相关操作不再支持字符串输入 需要用syms先指定变量 再用eq输入）
	solve 解方程/方程组 
		多个变量时需要指定变量
		返回参数和条件
	ezplot 直接对方程画图 P101

符号工具
	expand 展开方程
	collect 分配多项式
	factor 因式分解
	simplify 化简
	taylor 泰勒展开

基本符号演算
	limit 求极限 isequal 判断相等 inf 无穷大
		左右极限 加参数 left/right P121
		渐近线 先求根 再画线  P123
	diff 求导数
		pretty 让表达式更好看 （在matlab控制台中）
		subs 带入值 （花括号替代多个 P160）
		画圈 plot(xpos,ypos,'o')

微分方程求解析解
	dsolve 求解微分方程 P129
		一阶导数 D 二阶导数 D2
		结尾指定独立变量
	循环画图显示通解 P132
	方程组和相平面图
		ezplot用set指定画图格式 P126
		
微分方程求数值解
	一阶微分
		工具 ODE23 ODE45 P144
		ODE45 精确度更高
		先用函数实现 再带入求解
		示例：P147 例题7-1
	二阶微分 P150
		先把二阶方程转换成一阶方程组 再用方程组求解

积分
	int 积分 
	int(F,a,b) 定积分 
	不定积分 用inf作为区间端点
	多重积分 嵌套多个int 就像手动解一样
	数值积分
		trapz 梯形积分 近似解 P167
		quad quadl 正交积分 （用二次函数近似） P171
		
变换
	拉普拉斯变换 laplace 拉普拉斯逆变换 ilaplace
	用拉普拉斯变换解微分方程 P179
	傅里叶变换 fourier 傅里叶逆变换 ifourier
	快速傅里叶变换 fft P185
		rand 随机产生数字

曲线拟合
	polyfit 线性拟合 使用最小二乘法
		计算r2 P192
		计算RMS 均方根误差 
		find 在数组中查找 返回数组中序号
	指数函数拟合 P201
		先变形成线性函数 再拟合 最后再恢复
	
特殊函数
	伽马函数 gamma 不完全伽玛函数 gammainc
	贝塞尔函数 besselj 汉克尔函数 besselh
	贝塔函数 beta
	幂积分 expint
	内置特殊函数集 mfun P216（可以计算大部分特殊函数 用mfunlist查看）
	相伴勒让德方程 legendre
	亚里函数 airy
```


* * *

卢之睿

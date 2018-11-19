---
layout: post
title: "聚类分析"
date: 2018-11-19
description: ""
tag: Theory
---

<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

# 聚类分析

&emsp;&emsp;在实际工作中，我们经常遇到分类问题。若事先已经建立类别，则使用判别分析，若事先没有建立类别，则使用聚类分析。

&emsp;&emsp;聚类分析主要是研究在事先没有分类的情况下，如何将样本归类的方法。聚类分析的内容包含十分广泛，
有系统聚类法、动态聚类法、分裂法、最优分割法、模糊聚类法、图论聚类法、聚类预报等多种方法。
聚类分析指将物理或抽象对象的集合分组成为由类似的对象组成的多个类的分析过程，
它是一种重要的人类行为。聚类分析的目标就是在相似的基础上收集数据来分类。

&emsp;&emsp;聚类源于很多领域，包括数学，计算机科学，统计学，生物学和经济学。
在不同的应用领域，很多聚类技术都得到了发展，这些技术方法被用作描述数据，衡量不同数据源间的相似性，以及把数据源分类到不同的簇中。

&emsp;&emsp;聚类与分类的不同在于，聚类所要求划分的类是未知的。

&emsp;&emsp;聚类是将数据分类到不同的类或者簇这样的一个过程，所以同一个簇中的对象有很大的相似性，而不同簇间的对象有很大的相异性。

&emsp;&emsp;从统计学的观点看，聚类分析是通过数据建模简化数据的一种方法。

## 聚类分析的基本知识

### 聚类分析的基本思想

&emsp;&emsp;我们所研究的样本或指标（变量）之间存在程度不同的相似性（亲疏关系）。于是根据一批样本的多个观测指标，具体找出一些能够度量样本或指标之间相似程度的统计量，以这些统计量为划分类型的依据，把一些相似程度较大的样本（或指标）聚合为一类，把另外一些彼此之间相似程度较大的样本（或指标）又聚合为另一类，关系密切的聚合到一个小的分类单位，关系疏远的聚合到一个大的分类单位，直到把所有的样本（或指标）聚合完毕，这就是分类的基本思想。例如，我们可以根据学校的研究实力、教学水平和学生素质等情况，将大学分成一流大学，二流大学等；国家之间根据其经济社会发展水平可以划分为发达国家、发展中国家；自然界生物可以分为动物和植物等等。根据上述的基本思想，我们可以把聚类分析理解为：根据已知数据，计算各观察个体或变量之间亲疏关系的统计量（距离或相似性程度）。根据某种准则（如最近距离法、最远距离法、中间距离法、重心法等）使同一类内的差别较小，而类与类之间的差别较大，最终将观察个体或变量分为若干类。

&emsp;&emsp;在实际研究中，既可以对样本个体进行聚类（clustering for individuals），也可以对研究变量进行聚类（clustering for variables），对样本个体进行聚类通常称为$Q$型聚类，对研究变量进行的聚类称为*R*型聚类。

&emsp;&emsp;*Q*型聚类分析的主要作用是：可以综合利用多个变量的信息对样本进行分类，分类结果是直观的，聚类分析谱系图非常清楚地表现其数值分类结果，聚类分析所得到的结果比传统分类方法更细致、全面、合理。

&emsp;&emsp;*R*型聚类分析的主要作用是：不但可以了解个别变量之间的关系的亲疏程度，而且可以了解各个变量组合之间的亲疏程度，根据变量的分类结果以及它们之间的关系，可以选择主要变量进行回归分析或*Q*型聚类分析。

### 距离和相似性

&emsp;&emsp;为了将样本（或指标）进行分类，就需要研究样本之间关系。目前用得最多的方法通常有两种：一种方法是将一个样本看作$p$维空间的一个点，并在空间定义距离，距离越近的点归为一类，距离较远的点归为不同的类。另一种方法是用相似系数，性质越接近的样本，它们的相似系数的绝对值越接近1，而彼此无关的样本，它们的相似系数的绝对值越接近于零。比较相似的样本归为一类，不怎么相似的样本归为不同的类。

&emsp;&emsp;设有*n*个样本，每个样本测得*p*项指标（变量），原始资料矩阵为

$$X=\begin{bmatrix}
x_{11} & x_{12} & \cdots & x_{1p} \\
x_{21} & x_{22} & \cdots & x_{2p} \\
\vdots & \vdots & \vdots & \vdots \\
x_{n1} & x_{n2} & \cdots & x_{np}
\end{bmatrix}
=
\begin{bmatrix}
{\bf X}_1 \\
{\bf X}_2 \\
\vdots\\
{\bf X}_n
\end{bmatrix}$$


&emsp;&emsp;其中$$x_{ij}$$为第*i*个样本的第*j*个指标的观测数据。
$${\bf X}_i=(x_{i1}, x_{i2}, \cdots, x_{ip})$$, $$(i=1,2,\cdots,n)$$为第*i*个样本。所以任何两个样本$${\bf X}_i$$与$${\bf X}_j$$之间的相似性，可以通过矩阵$X$中的第*i*行与第*j*行的相似程度来刻划。$${\bf x}_j=(x_{1j} , x_{2j}, \cdots, x_{nj})^T$$, $$(j=1,2,\cdots,p)$$为第*j*个指标变量，任何两个指标变量$${\bf x}_k$$与$${\bf x}_l$$之间的相似性，可以通过第*k*列与第*l*列的相似程度来刻划。

&emsp;&emsp;如果把*n*个样本，$$n\times p$$矩阵*X*中的*n*行，看成*p*维空间中*n*个点，则两个样本间相似程度可用*p*维空间中两点的距离来度量。令$$d_{ij}$$表示样本$${\bf
X}_i$$与$${\bf X}_j$$的距离。常用的距离有：明氏（Minkowski）距离；马氏（Mahalanobis）距离；余弦距离；相似距离。

#### 明氏（Minkowski）距离
$$d_{ij}(q)=\left(\sum\limits_{a=1}^p|x_{ia}-x_{ja}|^q\right)^{\frac{1}{q}}.$$

#### 马氏（Mahalanobis）距离

&emsp;&emsp;设$$\Sigma$$表示指标的协方差矩阵即：

$$\Sigma=(\sigma_{ij})_{p\times p}$$

&emsp;&emsp;其中$$\sigma_{ij}=\frac{1}{n-1}\sum\limits_{a=1}^{n}(x_{ai}-\overline{x}_{i})(x_{aj}-\overline{x}_{j})\quad(i,j=1,2,\cdots,p),$$

&emsp;&emsp;如果$$\Sigma^{-1}$$存在，则两个样本之间的马氏距离为

$$d_{ij}=\sqrt{({\bf X}_{i}-{\bf X}_{j})^T\Sigma^{-1}({\bf X}_{i}-{\bf X}_{j})}$$

#### 余弦距离

$$d_{ij}=1-\frac{X_iX_j^T}{\sqrt{X_iX_i^T}\sqrt{X_jX_j^T}}$$

$$
D={ \left[ {\begin{array}{*{20}c}
  d_{11} & d_{12} & \cdots & d_{1n} \\
d_{21} & d_{22} & \cdots & d_{2n} \\
 \vdots & \vdots & \vdots\\
d_{n1} & d_{n2} & \cdots & d_{nn}
  \end{array}} \right]}
$$

#### 夹角余弦

$$\cos \theta_{ij}=\frac{\sum\limits_{a=1}^p x_{ia}x_{ja}}{\sqrt{\sum\limits_{a=1}^p x_{ia}^2\sum\limits_{a=1}^p x_{ja}^2}}.$$

$$
H={ \left[ {\begin{array}{*{20}c}
\cos \theta_{11} & \cos \theta_{12}& \cdots & \cos \theta_{1n} \\
\cos \theta_{21} & \cos \theta_{22}& \cdots & \cos \theta_{2n} \\
\vdots & \vdots & \vdots\\
\cos \theta_{n1} & \cos \theta_{n2}& \cdots & \cos \theta_{nn} \\
\end{array}} \right]}
$$

#### 相关系数

$$r_{ij}=\frac{\sum\limits_{a=1}^p(x_{ia}-\overline{x}_{i})(x_{ja}-\overline{x}_{j})}{\sqrt{\sum\limits_{a=1}^p (x_{ia}-\overline{x}_{i})^2\sum\limits_{a=1}^p(x_{ja}-\overline{x}_{j})^2}}.$$

$$
R={ \left[ {\begin{array}{*{20}c}
r_{11} & r_{12}& \cdots &r_{1n} \\
r_{21} & r_{22}& \cdots & r_{2n} \\
\vdots & \vdots & \vdots\\
r_{n1} & r_{n2}& \cdots &r_{nn} \\
\end{array}} \right]}
$$



* * *

Iydon

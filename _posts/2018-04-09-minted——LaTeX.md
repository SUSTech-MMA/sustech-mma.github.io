---
layout: post
title: "minted——LaTeX"
date: 2018-04-09
description: ""
tag: LaTeX
---

# minted

&emsp;&emsp;本次推送主要介绍LaTeX中用于高亮显示代码的minted宏包。参考网站如下：[LaTeXStudio](http://www.latexstudio.net/archives/328)  
&emsp;&emsp;值得说明的是，minted需要使用pymentize库，并且需使用
```pdflatex -shell-escape```对源文件进行编译。另外，本文只介绍windows下的操作。  

## 一、安装pymentize库
首先需要安装[python](https://www.python.org/)环境，此处省略。打开命令行并输入：```pip install pygments```。

## 二、代码测试
代码如下图  
```LaTeX
\documentclass{ctexart}
\usepackage{minted}
\begin{document}
\begin{minted}[frame=single]{matlab}
f = @(n) plot(fft(eye(n)));
% 正n边形
figure();
hold on;
axis equal;
for i = 3:17
    f(i);
    pause(1)
    % 绘图
end
\end{minted}
\end{document}
```
&emsp;&emsp;大家可以编译一下查看效果（编译时需用命令行转到当前路径并使用：```pdflatex -shell-escape```）：  

## 三、解释说明
&emsp;&emsp;可见在代码中**\begin{minted}[frame=single]{matlab}**中，确定了**minted**参数，当然也可以在导言区设定，下面简要介绍几个常用的**option**，其余如果有兴趣，可以参看**LaTeX**的帮助文档。  

- **mathescape**，指定是否可以在展示代码中出现数学模式，默认值为**false**。
- **linenos**，出现行数，默认值为**false**。
- **numbersep**，Gap between numbers and start line(default: **12pt**)。
- **gobble**，Remove the first *n* characters from each input line(default: **0**)。
- **frame**，用以指定包围的frame的样式，默认值为**none**。
- **escaperinside**，可以参见上面**mathescape**。
- **xleftmargin**与**xrightmargin**，用以确定缩进大小。

&emsp;&emsp;最后，如果配上mdframed宏包一起配置使用，则会产生更好的效果。  

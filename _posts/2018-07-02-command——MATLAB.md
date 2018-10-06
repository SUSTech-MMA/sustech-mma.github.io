---
layout: post
title: "命令——MATLAB"
date: 2018-07-02
description: ""
tag: MATLAB
---

# 命令

|命令          |功能           |
|--------------|---------------|
|clear         |删除变量，也可以自定义删除特定变量(clear var-name)|
|clc           |清除命令行窗口|
|quit          |停止MATLAB|
|save          |将工作区的变量保存为后缀为mat的文件|
|load var-name |载入mat文件|
|help fun-name |显示函数名为fun-name的帮助|
|doc fun-name  |打开函数名为fun-name的帮助文档|

&emsp;&emsp;使用help命令：
```MATLAB
》help lu
lu - LU 矩阵分解

    此 MATLAB 函数 返回矩阵 Y，其中包含严格下三角矩阵 L（即不带其单位对角线）和上三角矩阵 U 作为子矩阵。也即，如果 [L,U,P] =
    lu(A)，Y = U+L-eye(size(A))。不会返回置换矩阵 P。

    Y = lu(A)
    [L,U] = lu(A)
    [L,U,P] = lu(A)
    [L,U,P,Q] = lu(A)
    [L,U,P,Q,R] = lu(A)
    [...] = lu(A,'vector')
    [...] = lu(A,thresh)
    [...] = lu(A,thresh,'vector')

    See also cond, det, ilu, inv, qr, rref

    Reference page in Doc Center
       doc lu

    Other functions named lu

       sym/lu
```

&emsp;&emsp;who列出当前变量，whos列出变量及其属性。
```MATLAB
》clear; clc;
》A = rand(1024);
》[L,U] = lu(A);
》[Q,R] = qr(A);
》[U,S,V] = svd(A);
》who

Your variables are:

A  L  Q  R  S  U  V  

》whos
  Name         Size                Bytes  Class     Attributes

  A         1024x1024            8388608  double              
  L         1024x1024            8388608  double              
  Q         1024x1024            8388608  double              
  R         1024x1024            8388608  double              
  S         1024x1024            8388608  double              
  U         1024x1024            8388608  double              
  V         1024x1024            8388608  double              

》
```

|命令           |解释         |
|---------------|------------|
|format short   |四位十进制数（默认）|
|format long    |15位定点表示|
|format short e |五位浮点表示|
|format long e  |15位浮点表示|
|format bank    |两个十进制数字|
|format +       |正，负或零|
|format rat     |有理数近似|
|format compact |变量之间没有空行|
|format loose   |变量之间有空行|

&emsp;&emsp;先为*format short*，后为*format rat*：
```MATLAB
》disp(1/5); format rat; disp(1/5)
    0.2000

       1/5
```
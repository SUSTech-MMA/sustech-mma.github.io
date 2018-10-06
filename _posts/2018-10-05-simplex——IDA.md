---
layout: post
title: "单纯形法——智能数据分析"
date: 2018-10-05
description: ""
tag: 智能数据分析
---

<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

[Simplex Algorithm(linear programming)](https://sustech-cs-courses.github.io/IDA/)
===
研究一组线性不等式或等式约束下使得某一线性目标函数取最大值（或最小值）的极值问题

# Standard Form

$$
\begin{equation}
\left\{
\begin{aligned}
max(z)&=CX\\
AX&=b\\
x_i>0\\
\end{aligned}
\right.
\end{equation}
$$

&ensp;&ensp;&ensp;&ensp;$$b\geq0$$, $$m\leq n$$, $$rank(A)=m$$, but Why $$rank(A)=m$$?

&ensp;&ensp;&ensp;&ensp;If not, the constraint $$AX=b$$ would have only one solution.

# Transform a general form into standard form

* Maxmium the objective function.
$$min(z)=CX\rightarrow max(w)=-CX(w=-z)$$
* Transform inequality into equality(Same thing for greater inequality)

$$a_{11}x_1+a_{12}x_2+...a_{1n}x_n\leq b_1$$

$$\downarrow$$

$$a_{11}x_1+a_{12}x_2+...a_{1n}x_n+y_k= b_1(y_k>0)$$

* Change unconstrait variable into two constraint variable.

$$x_i=y_k'-y_k''(y_k'>0,y_k''>0)$$

* When $$b_j<0$$ multiply (-1) in both side.

# Now we have the standard form. How to solve for the optimal solution?

&ensp;&ensp;&ensp;&ensp;Remember the $$y$$ variables we added for constriant?

&ensp;&ensp;&ensp;&ensp;These variables all have the same coefficient $$1$$, so these coefficient form a identity matrix $$I$$.

&ensp;&ensp;&ensp;&ensp;So we can write something like this
$$[A\space I]\begin{bmatrix}X\\Y\end{bmatrix}=b$$
We use what is called Simplex Tableau

# Example

$$max (x_1+x_2)$$

$$s.t.
\left\{
\begin{align}
2x_1+x_2+x_3=12 \\
x_1+2x_2+x_4=9 \\
x_i>0
\end{align}
\right|
\quad i=1,2,3,4
$$

&emsp;&emsp;$$x_3,x_4$$是基变量（basic variable也就是上面的y，辅助变量），$$x_1,x_2$$是非基变量，也就是要求的值。

## Simple Tableau

|     |$$x_1$$|$$x_2$$|$$x_3$$|$$x_4$$|$$b$$|
|-----|-----|-----|-----|-----|---|
|$$x_3$$|  2  |  1  |  1  |  0  | 12|
|$$x_4$$|  1  |  2  |  0  |  1  | 9 |
|$$ c $$|  1  |  1  |  0  |  0  | 0 |

&ensp;&ensp;&ensp;&ensp;We introduce a operation called povit(d,e).

&ensp;&ensp;&ensp;&ensp;We choose a non-basic variable $$x_e$$ $$s.t.\space c_e>0(Max\space c_e)$$

&ensp;&ensp;&ensp;&ensp;Then choose a basic variable $$x_d$$ $$s.t.\space A_{(d,e)}>0\space and \space min(\frac{b_d}{A_{(d,e)}})$$

&ensp;&ensp;&ensp;&ensp;Here we have the same $$c_e$$for both $$x_1$$ and $$x_2$$, we just go with $$x_1$$

&ensp;&ensp;&ensp;&ensp;So here we see that for $$x_3$$, $$b_3=12$$, $$A_{(3,1)}=2$$, for $$x_4$$, $$b_4=9$$, $$A_{(4,1)}=1$$

&ensp;&ensp;&ensp;&ensp;Because, $$\frac{12}{2}<\frac{9}{1}$$ we choose $$x_3$$

## After **Row Exchange**

|     |$$x_1$$|$$x_2$$|$$x_3$$|$$x_4$$|$$b$$|
|-----|-----|-------|-------|-----|---|
|$$x_3$$|  1  |  1/2  |   1/2 |  0  | 6 |
|$$x_4$$|  0  |  3/2  |  -1/2 |  1  | 3 |
|$$ c $$|  0  |  1/2  |  -1/2 |  0  |-6 |

## **Repeat until we have all $$c$$ variable into non-positive ones**

|     |$$x_1$$|$$x_2$$|$$x_3$$|$$x_4$$|$$b$$|
|-----|-----|-------|-------|-----|---|
|$$x_3$$|  1  |  0  |   2/3 |  -1/3  | 5 |
|$$x_4$$|  0  |  1  |  -1/3 |   2/3  | 2 |
|$$ c $$|  0  |  0  |  -1/3 |  -1/3  |-7 |

Now $$x_3=5,x_4=2$$ is the optimal solution.

* * *

作者：卢弘毅

---
layout: post
title: "数值微分与数值积分——Numerical"
date: 2018-10-09
description: ""
tag: Numerical
---

<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

# 数值微分

$$
\begin{align}
f(x) &= p_n(x)+R_n(x) \\
     &= \sum_{k=0}^{n}f(x_k)L_k(x) + \frac{f^{(n+1)}(\xi(x))}{(n+1)!}\prod_{k=0}^n(x-x_k) \\
\end{align}
$$

于是我们可以得到：

$$
\begin{align}
f'(x_j) &= \sum_{k=0}^{n}f(x_k)L_k'(x_j) \\
        &+ \frac{f^{(n+1)}(\xi(x_j))}{(n+1)!}
\end{align}
$$

## end-point

$$
\begin{align}
f'(x_0) &= \frac{-3f(x_0)+4f(x_0+h)-f(x_0+2h)}{2h} \\
        &+ \frac{h^2}{3}f^{(3)}(\xi)
\end{align}
$$

## mid-point

$$
\begin{align}
f'(x_0) &= \frac{f(x_0+h)-f(x_0-h)}{2h} \\
        &- \frac{h^2}{6}f^{(3)}(\xi)
\end{align}
$$

$$
\begin{align}
f''(x_0) &= \frac{f(x_0+h)-2f(x_0)+f(x_0-h)}{h^2} \\
        &- \frac{h^2}{12}f^{(4)}(\xi)
\end{align}
$$

# 数值积分
$$
\begin{align}
\int_b^a f(x)\,\mathrm{d}x &= \sum_{k=0}^nf(x_k)\int_b^aL_k(x)\,\mathrm{d}x \\
              &+ \frac{1}{(n+1)!}\int_b^af^{(n+1)}(\xi(x))\prod_{k=0}^n(x-x_k)\,\mathrm{d}x \\
              &= \sum_{k=0}^na_kf(x_k)+E(f)
\end{align}
$$

## Simpson's Rule
$$
\begin{align}
\int_b^af(x)\mathrm{d}x &= \frac{b-a}{6}\left(f(a)+4f(\frac{a+b}{2})+f(b)\right) \\
&- \frac{(b-a)^5}{2880}f^{(4)}(\xi)
\end{align}
$$

## 等距数值积分
如果$$x_0=a$$，$$x_a=\frac{a+b}{2}$$，$$x_2=b$$，$$h=\frac{b-a}{2}$$。

$$
\begin{align}
a_0 &= \int_{x_0}^{x_2}\frac{(x-x_1)(x-x_2)}{2h^2}\,\mathrm{d}x &= \frac13h \\
a_1 &= \int_{x_0}^{x_2}\frac{(x-x_0)(x-x_2)}{2h^2}\,\mathrm{d}x &= \frac43h \\
a_2 &= \int_{x_0}^{x_2}\frac{(x-x_0)(x-x_1)}{2h^2}\,\mathrm{d}x &= \frac13h \\
\end{align}
$$

于是我们得到

$$
\begin{align}
\int_b^af(x)\mathrm{d}x &= \frac{h}{3}\left(f(a)+4f(\frac{a+b}{2})+f(b)\right) \\
&+ \frac16\int_b^a(x-x_0)(x-x_1)(x-x_2)f'''(\xi)\mathrm{d}x
\end{align}
$$

再由泰勒展式，可以比较得到最后的余项为：

$$
\begin{align}
 -\frac{1}{36}h^5f^{(4)}(\xi_1)+\frac{1}{60}h^5f^{(4)}(\xi_2)
\end{align}
$$

## The degree of accuracy, or precision
使得 $$x^k$$ 精确的最大的整数。

## Newton-Cotes 公式
$$x_k=a+kh$$, for $$h=\frac{b-a}{2}$$ and $$k=0:n$$。

$$
\int_b^af(x)\mathrm{d}x\approx\sum_{k=0}^na_kf(x_k)
$$

其中

$$
a_k=\int_b^aL_k(x)\mathrm{d}x.
$$

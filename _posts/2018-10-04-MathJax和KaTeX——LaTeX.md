---
layout: post
title: "MathJax和KaTeX——LaTeX.md"
date: 2018-10-04
description: ""
tag: LaTeX
---

<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

## MathJax
&emsp;&emsp;在需要使用数学公式的**Markdown**文件中添加如下内容，即可使用**CDN**（Content Delivery Network）产生数学公式。注意数学公式需要使用**$$**包围。  
```
<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>
```

例如
```LaTeX
$$
f(x) = \int_{-\infty}^\infty\hat f(\xi\,e^{2 \pi i \xi x})\,d\xi
$$
```
&emsp;&emsp;即可渲染出如下公式：

$$
f(x) = \int_{-\infty}^\infty\hat f(\xi\,e^{2 \pi i \xi x})\,d\xi
$$

&emsp;&emsp;由于**MathJax**需要兼容东西太多，所以转化大规模数学公式性能较差，于是就有**KaTeX**  

## KaTeX

&emsp;&emsp;据说优点有快速、并发渲染、无需重排页面，但是个人没有配置出来，所以无法对其进行评价。以下为搜索到的资源，等待以后更进一步的探索。

> [Jekyll 中使用 KaTeX](https://frankindev.com/2017/02/08/using-katex-in-jekyll/ "frankindev.com")  
> [KaTeX官网](https://katex.org/ "katex.org")  
> [Github](https://github.com/Khan/KaTeX "github.com")
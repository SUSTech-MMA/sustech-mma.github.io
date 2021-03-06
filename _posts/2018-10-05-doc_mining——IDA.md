---
layout: post
title: "文本挖掘——智能数据分析"
date: 2018-10-05
description: ""
tag: 智能数据分析
---


<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


[Document Mining](https://sustech-cs-courses.github.io/IDA/)
===

* * *

# Data are now texted documents

- Transform data to vector

$$d^i\rightarrow \underline{d^i}=\begin{bmatrix}d^i_1\\ d^i_2\\ .\\.\\.\\d^i_T\end{bmatrix}\quad(\underline{d^i} \in R^T)$$

- Set of Terms


$$T = \{t_1t_2...t_T\}$$

- $$d_k^i$$ shows how important is term $$t_k$$ in $$d^i$$

* * *

# Ways of deciding $$d^i_k$$

* Binary: 

	$$d_k^i=
	\left\{
		\begin{array}{lr}
		0(t_k\space not\space exist)\\
		1(t_k\space exist)
		\end{array}
	\right.$$

* Frequency: 

$$d_k^i=N^i_k$$

* Relative Frequency: 

$$d_k^i=\frac{N^i_k}{|d^i|}$$

* Term frequency inverse doc frequency

$$d_k^i=\frac{N^i_k}{|d^i|}log\frac{N}{N_k}$$

* * *

# Information Theory View Point

$$d_k^i=\frac{N^i_k}{|d^i|}log\frac{1}{\frac{N_k}{N}}$$

$$\frac{N_k}{N}=P(t_k|Libary)$$

$$\frac{N_k^i}{|d^i|}=P(t_k|d^i)$$


&ensp;&ensp;&ensp;&ensp;**Consider 2 Dice with outcome $$\{1,2,3,4,5,6\}$$**, random vaiable $$X$$ with distribution $$P(X)$$, event set is $$A$$.

&ensp;&ensp;&ensp;&ensp;So we have Event $$x\in$$ A (eg. $$x=3$$), in the event we have:  

$$P(x)\uparrow$$ => Lower surprise => Low information.

$$P(x)\downarrow$$ => Higher surprise => Higher information.

Information = $$\frac{1}{P(x)}$$, **Consider info transfer situation**.

Binary info channel (N equally event)

* * *

# New Situation
&ensp;&ensp;&ensp;&ensp;Unfair Dice1: $$P(x)$$.

&ensp;&ensp;&ensp;&ensp;Infomartion: $$I(x)=log_2\frac{1}{P(x)}$$, optimal Average Code Length: 

$$E_{P(x)}[log_2\frac{1}{P(x)}]=\sum_{x\in A}P(x)log_2\frac{1}{P(x)}=H(x)(entropy)$$

&ensp;&ensp;&ensp;&ensp;But, we can only estimate the $$P(x)$$, the 'nature' is $$P(x)$$ but what we have is $$Q(x)$$(our estimation), so we have code length $$I(x)=log_2\frac{1}{P(x)}$$.

&ensp;&ensp;&ensp;&ensp;True Average Code Length: 

$$E_{P(x)}[log_2\frac{1}{Q(x)}]=\sum_{x\in A}P(x)log_2\frac{1}{Q(x)}$$

* * *

# 但是，古尔丹！代价是什么呢？
&ensp;&ensp;&ensp;&ensp;Cost K-L divergence:

$$E_{P(x)}[log_2\frac{1}{Q(x)}]-E_{P(x)}[log_2\frac{1}{P(x)}]$$

$$=\space\space\sum_{x\in A}P(x)[log_2\frac{1}{Q(x)}+log_2P(x)]$$

$$=\sum_{x\in A}P(x)log_2\frac{P(x)}{Q(x)}(Cross Entropy)$$

&ensp;&ensp;&ensp;&ensp;This can be used to evaluate the difference between two different prob distribution. That is also why the tdidf uses $$E_{P(x)}[log_2\frac{1}{Q(x)}]$$(allow the document to stand out in the distribution of the whole libary)

&ensp;&ensp;&ensp;&ensp;The term of $$E_{P(x)}[log_2\frac{1}{P(x)}]$$is just to normalize the difference.

* * *

# Some fact about entropy

$$H[X,Y]=H[X]+H[Y](independent)$$

$$H[X,Y]=H[X]+H[Y|X](dependent)$$

* * *

# Semantic Meaning

&ensp;&ensp;&ensp;&ensp;In document mining, a document vector usually has 1000 or more dimension. $$d^i\rightarrow d^i\in R^T(T\approx1000)$$

&ensp;&ensp;&ensp;&ensp;But words are usually **related**! If in a article it mentioned 'rain', it is very likely it will also mention 'cloud', so the PCA can give us a remarkable result.

* * *
作者：卢弘毅

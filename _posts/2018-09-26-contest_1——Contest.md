---
layout: post
title: "每周知识竞赛——竞赛"
date: 2018-09-26
description: ""
tag: 竞赛
---

<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

# 高等数学每周知识竞赛第1期

&emsp;&emsp;高等数学每周知识竞赛，每周一中午12开放题目，周五晚上12:00截止答题，请将手写版的答案提交至慧园3栋501陶金老师办公室，答案上面写上提交的日期和时间，我们根据答卷的得分和提交时间，每周评选出一位获胜者，奖励100块钱购书券。  

&emsp;&emsp;只限本人独立完成，不得商量，讨论或到网上去查答案。  

- - -

Given sequence $$x_0,x_1,x_2,\cdots$$ which satisfies $$x_0=0,x_1=1$$ and  

$$x_n=x_{n-1}+\frac12 x_{n-2},\quad n=2,3,4,\cdots$$  

Find the maximal positive integer $$l$$ such the $$x_l$$ is integer.  

- - -

![](/images/posts/2018-09-24-zhi-shi-jing-sai-1.png)

```Python
from fractions import Fraction

def contest(num:int=0):
	if num<2:
		return Fraction(num, 1)
	x0 = Fraction(0, 1)
	x1 = Fraction(1, 1)
	for i in range(num):
		tmp = x1
		x1 += x0/2
		x0 = tmp
	return x1

num = 0
try:
	while True:
		ans = contest(num)
		if ans._denominator==1:
			print(num)
		num += 1
except:
	print(num)
```
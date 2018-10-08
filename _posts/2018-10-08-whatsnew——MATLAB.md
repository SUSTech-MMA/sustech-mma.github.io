---
layout: post
title: "MATLAB Release Notes"
date: 2018-10-08
description: ""
tag: MATLAB
---

# MATALB String

&emsp;&emsp;*String*为*MATLAB*字符串数组，由此引出**MATLAB Release Notes**。本问题源自在*MATLAB 2016a*中使用半角双引号表示*string*会报错，错误信息为
> Error: Invalid text character. Check for unsupported symbol, invisible character,
or pasting of non-ASCII characters.

&emsp;&emsp;通过在高版本的*MATLAB*中输入帮助可以看到：
```MATLAB
》help string
string - 字符串数组

    从 R2016b 开始，您可以使用字符串数组而不是字符数组来表示文本。字符串数组的每个元素存储一个字符序列。序列可以具有不同长度，无需填充，例如 yes 和
    no。只有一个元素的字符串数组也称为字符串标量。

    str = string(A)
    str = string(D)
    str = string(D,fmt)
    str = string(D,fmt,locale)

    See also cellstr, char, isstring, isstrprop, strings, strlength

    Reference page in Doc Center
       doc string

    Other functions named string

       categorical/string    opaque/string    sym/string    tall/string
       mtree/string

```
&emsp;&emsp;所以在*string*是在*MATLAB 2016b*后才开始使用的，在之前版本的*MATLAB*就会报错。为避免此类问题再次发生，浪费过多精力，所以想到在运行不同版本的程序前，首先查看两个版本之间的差异，从而在一定程度上避免，于是发现了**whatsnew**命令，但是在*MATLAB 2018a*中说道，“在以后的版本中将会删除whatsnew”，具体替代的方法未知，如果大家知道欢迎告知。

&emsp;&emsp;目前输入在命令行输入**whatsnew**，通过填写*Release Range*，可以看到如下界面：

![](/images/posts/2018-10-08-fa-xing-1.jpg)

* * *

文字：Iydon

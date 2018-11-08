---
layout: post
title: "LaTeX宏包与文类简易海报"
date: 2018-11-08
description: ""
tag: LaTeX
---

# 代码
&emsp;&emsp;素材来自TeXBook，源码来自[Overleaf](https://www.overleaf.com/gallery/tagged/poster)。

&emsp;&emsp;由于时间仓促，所以一些细节内容未做修饰，目前效果可以参照[PDF](/pdf/2018-11-08-wen-lei-1.pdf)文件。

```LaTeX
\documentclass[10pt]{beamer}

\setbeamertemplate{navigation symbols}{}
\definecolor{OverleafGreen}{RGB}{103,155,67}
\definecolor{DarkGreen}{RGB}{50,90,37}
\usecolortheme[named=DarkGreen]{structure}
\usefonttheme{structurebold}
\setbeamertemplate{frametitle}[default][center]
\setbeamerfont{framesubtitle}{size=\normalsize}
\usepackage{xeCJK}
\usepackage{graphicx}
\setCJKmainfont{设置中文字体}
\setmainfont{设置英文字体}

\begin{document}
    \begin{frame}
    % \framesubtitle{\raisebox{-0.2ex}{\includegraphics[height=1em]{tor-en-lr.pdf}} \#Class and Style.}
    \framesubtitle{\#Class and Style.}
    \frametitle{拉泰赫 文类和宏包讨论小组}

    {\large\centering
    欢迎对拉泰赫宏包与文类创作感兴趣的同学一同交流！\par}

    \vfill
    \begin{columns}[b]
        \begin{column}{2.2in}
            \includegraphics[width=\linewidth]{左侧插图文件名称}
        \end{column}

        \begin{column}{2.7in}
            \small
            \begin{block}{Location}
            南方科技大学\\
            第一教学楼 306
            \end{block}

            \begin{block}{When}
            November 11, 2018 (Sun) 9\,:\,00\,\textsc{pm} -- 10\,:\,00\,\textsc{pm}
            \end{block}

            \begin{block}{Register!}
            \includegraphics[width=0.3\linewidth]{二维码图片文件名称}\enspace \LaTeX 学习交流群
            \end{block}
        \end{column}

    \end{columns}

    \end{frame}

\end{document} 
```

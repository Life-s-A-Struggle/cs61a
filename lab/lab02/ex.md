# Markdown Test
<h1>Heading level 1</h1>

Heading level 1
===============

### 段落
I really like using Markdown.

I think I'll use it to format all of my documents from now on.

不要用空格（spaces）或制表符（ tabs）缩进段落。

### 换行
This is the first line.  
And this is the second line.
两个或多个空格/制表位
<p>This is the first line.<br>
And this is the second line.</p>

### 加粗
Love**is**bold  
Love<strong>is</strong>bold

### 斜体
Italicized text is the *cat's meow*.  
Italicized text is the <em>cat's meow</em>.

### 加粗斜体
This text is ***really important***.  
This text is <strong><em>really important</em></strong>.

### 引用
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

### 列表
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item
<ol>
<li>Indented item</li>
<li>Indented item</li>
</ol>
</li>
<li>Fourth item</li>
</ol>

### 代码块
1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3.  Update the title to match the name of your website.

### 代码
At the command prompt, type `nano`.

At the command prompt, type <code>nano</code>.

### 三种分割线
***
---
_________________

### 链接
这是一个链接 [Markdown语法](https://markdown.com.cn)。

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。鼠标悬浮会有文字提示

网址<https://markdown.com.cn>

<a href="超链接地址" title="超链接title">超链接显示名</a>

不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。
[link](https://www.example.com/my%20great%20page)

### 图片
![这是图片](/assets/img/philly-magic-garden.jpg "Magic Gardens")

<img src="图片链接" alt="图片alt" title="图片title">

### 转义字符
要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 \ 。  
\* Without the backslash, this would be a bullet in an unordered list.

特殊字符自动转义

在 HTML 文件中，有两个字符需要特殊处理： `<` 和 `& `。 `< `符号用于起始标签，& 符号则用于标记 HTML 实体，如果你只是想要使用这些符号，你必须要使用实体的形式，像是 `&lt;` 和 `&amp;`

`& `符号其实很容易让写作网页文件的人感到困扰，如果你要打「AT&T」 ，你必须要写成`「AT&amp;T」`，还得转换网址内的 & 符号，如果你要链接到：
http://images.google.com/images?num=30&q=larry+bird
你必须要把网址转成：

http://images.google.com/images?num=30&amp;q=larry+bird

### Markdown 内嵌 HTML 标签
HTML 行级內联标签和区块标签不同，在內联标签的范围内， Markdown 的语法是可以解析的。

This **word** is bold. This <em>word</em> is italic.

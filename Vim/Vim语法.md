# Vim语法

Vim共有三种模式：命令模式（Command mode），输入模式（Insert mode）和底线
命令模式（Last line mode）：

1. 命令模式：刚开始启动Vim时便为命令模式，此时的按键输入视为命令。常见
命令有：

> `i`：切换到输入模式，以输入字符
> `x`：删除当前光标所在处字符
> `:`：切换到底线命令模式

2. 输入模式
3. 底线命令模式：`q`退出程序，`w`保存文件，在命令后加`!`表示强制执行

## 命令模式

移动光标：

* `h, j, k, l`：分别表示光标向左，下，上，右移动一格；使用
`<number><direction>`可以实现多行跳转
* `[Ctrl] + [f/b]`：相当于Page Down/Up
* `[Ctrl] + [d/u]`：向下/上移动半页
* `+/-`：光标移动到非空格符的下/上一行
* `<number>[Space]`：表示向右移动number格
* `0/[Home]`：移动到该行第一个字符
* `$/[End]`：移动到该行最后一个字符
* `H/M/L`：光标移动到屏幕最上方/中央/最下方的第一个字符
* `G`：移动到最后一行
* `<number>G`：移动到第number行
* `gg`：移动到第一行，相当于`1G`
* `n<Enter>`：光标向下移动number行

搜索替换：

* `/<word>`：在光标之下寻找第一个名称为word的字符串
* `?<word>`：在光标之上寻找第一关名称为word的字符串
* `n/N`：正向/反向继续上一次搜索
* `<number1>,<number2>s/<word1>/<word2>/g`：在第n1行到n2行之间搜索字符串
word1并替换为word2
* `:1,%s/<word1>/<word2>/g`或`:%s/<word1>/<word2>/g`：从第一行到最后
一行寻找字符串word1并替换为word2
* `:1,%s/<word1>/<word2>/gc`或`:%s/<word1>/`

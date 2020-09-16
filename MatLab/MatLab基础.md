# MatLab基础

MatLab命令有两种执行方式：交互式命令执行方式和M文件执行方式。其中M文件根据
调用方式的不同分为两类：脚本文件（Script File）和函数文件（Function File）
，两者的拓展名都是.m。

> 脚本文件没有输入参数，也不返回输出参数；脚本文件对工作空间的全局变量进行
操作，所有命令的执行效果都会返回工作空间中；脚本文件可以直接运行
> 函数文件可以带输入参数，也可以返回输出参数；在函数文件中定义的变量均为
局部变量；函数文件不可以直接运行，需要被调用

## 程序的控制结构

### 顺序结构

```Matlab
% 数据的输入
A = input('输入A矩阵'); % input函数：input(提示信息， 选项)
A = input('输入A矩阵', 's'); % 允许输入一个字符串

% 数据的输出
disp(A);

% 程序暂停
pause("程序暂停描述");

% 数字与字符串的转换
num2str(number);
```

### 选择结构

```Matlab
% if语句
if condition
    statement1
elseif condition
    statement2
else
    statement3
end

% switch语句
switch expression % switch后的expression应为一个标量或字符串
case expression1  % case后的expression可以为标量、切片或字符串，也可以为一个矩阵元胞('{}')
    statement1
case expression2
    statement2
case expression3
    statement3
otherwise
    statementn
end

% try语句
try
    statement1
catch % 若try语句出错，则执行catch语句
    statement2
end
```

### 循环结构

```Matlab
% for语句
for i = expression1: expression2: expression3 % 初值：步长：终止
    statement
end

% whlie语句
while condition
    statement
end

break
continue
```

由于MatLab的特点，经常可以用向量运算代替循环操作。下面的程序求解表达式
$y = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + ... + \frac{1}{n^2}$的值。

```Matlab
y = 0; n = 100;
for i = 1: n
    y = y + 1 / i / i;
end
y

n = 100;
i = 1: n;
f = 1 ./ (i .^ 2);
y = sum(f)
y
```

## 函数文件

函数文件由function语句引导，基本结构是：

```Matlab
function [a, b] = function_name(input_parameters)
% comment：当输出参数多于一个时，需要用方括号括起
% FUNCTION_NAME: to show the rule of writing a function
% input_parameters: ...

% xxx, wrote in August 19, 2020
statements
```

函数引导行之后以%开头的第一行注释一般包括函数名与函数描述、参数描述等，相隔一个空行的
注释行包括函数文件的编写和修改信息，如作者和版本等

函数名与文件名一般需要相同，若不相同，以文件名为准。

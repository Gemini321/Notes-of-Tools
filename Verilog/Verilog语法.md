# Verilog语法

## 语言要素

### 空白符

空白符包括空格('\b')，制表符('\t')，换行符和换页符。在编译和综合时，空白符
被忽略。空白符用于使代码更易读。

### 注释符

与C/C++相同。**注释，命名方式和路径都不能拥有中文**。

### 标识符

标识符用于命名，可以是任意一组字母、数字、$和_的组合，**标识符区分大小写**，
但最好不要因为大小写而产生歧义（VHDL不区分大小写）。

转义标识符使不满足语法的标识符合法。

### 关键字

### 数值

Verilog有4种逻辑数值状态：

| 状态  |       含义       |
| :---: | :--------------: |
|   0   |  低电平，逻辑0   |
|   1   |  高电平，逻辑1   |
|  x/X  | 不确定或未知状态 |
|  z/Z  |    高阻抗状态    |

当两个逻辑可能冲突（同时连接到一根线上），或信号悬空，
使用x/X；z/Z出现在三态门。

表示形式为：`+/- <size>'<base_format><number>`，其中对于base_format：
二进制(b/B)，八进制(o/O)，十进制(d/D)，十六进制(h/H)。
（e.g. 8'ha6为8位宽的十六进制数a6，4'b0001，5'o35）。
允许在number中间加'_'以区分，\<size\>和'和\<base_format\>中间不能有空格，
\<size\>不允许为表达式形式。

实数：将整数和小数分开，先固定小数点位置（定点数/浮点数），再分别表示整数和
小数。实数不能直接用于设计之中。

### 数据类型

根据对电流的驱动强度，分为如下数据类型：

| 标记符 |                 名称                 | 类型  |
| :----: | :----------------------------------: | :---: |
| supply |      电源级驱动（电源直接接0）       | 驱动  |
| strong |    强驱动（电源经过上拉电阻接0）     | 驱动  |
|  pull  | 上拉级驱动（比强驱动更大的上拉电阻） | 驱动  |
| large  |                大容性                | 存储  |
|  weak  |                弱驱动                | 驱动  |
| medium |               中性驱动               | 存储  |
| small  |                小容性                | 存储  |
| highz  |           高容性（无电流）           | 高阻  |

连线型数据类型：定义为`<net_declaration><drive_strength><range><delay><list_of_variables>;`
。其中`new_declaration`为数据类型，`range`为设置位宽，`delay`指定仿真延迟
时间，`drive_strength`表示驱动强度，`list_of_variables`为参数列表。

| 连线型数据类型 |                       功能说明                       |
| :------------: | :--------------------------------------------------: |
|   wire, tri    |              标准连线（缺省值为该类型）              |
|   wor, trior   | 多重驱动（多根导线直接相连）时，具有线或特征的连线型 |
|  wand, triand  |           多重驱动时，具有线与特征的连线型           |
|     trireg     |               具有电荷保持特性的连线型               |
|      tri1      |                       上拉电阻                       |
|      tri0      |                       下拉电阻                       |
|    supply1     |             电源线，作为电源，为高电平1              |
|    supply0     |             电源线，作为接地，为低电平0              |

寄存器类型：数据存储单元，用于行为级描述，由过程赋值语句对其赋值。
定义为`reg<range><list_of_variables>`，变量用','隔开。
`reg [8:1] c, d, e;`表示定义了三个位宽为8的reg型变量（默认为unsigned），
有符号数定义为`reg signed[3:0] rega;`，其中rega存储为补码形式。

存储器型：存储器型变量可以描述RAM, ROM以及reg文件。声明格式为
`reg<range1><name_of_register><range2>`，其中`range1`和`range2`
缺省值为1，前者表示存储器当中寄存器的位宽，后者表示寄存器的数量，均用
'[max:min]'表示（e.g. reg[7:0] mem1[255:0] 表示由256个8位寄存器的存
储器mem1，地址范围位0~255）

抽象数据类型：整型（integer），时间型（time），实型（real）和参数型
（parameter），声明为`<type><list_of_register_variables>`

## 运算符和表达式

优先级由单目 -> 双目 -> 三目递减。

### 算术操作符

算数操作符代表着一个个电路。表达式的运算结果由长度最长的操作数决定，
赋值时长度由最左边的目标长度决定。

```Verilog
reg[3:0] a;
reg[2:0] b;
begin
    a = 4'b1111;           // 15
    b = 3'b011;            // 3
    $display("%b", a * b); // 输出为4'b1101，为45的低四位
    $display("%b", a * b); // 输出为4'b0010
end
```

### 关系操作符

`>, <, >=, <=`，输出为一位的信号。任何数与不定状态比较都是不定状态。
`==, !=, ===, !==`，后两者分别为全等和不全等。`==, !=`只有在比较值为
有效值时才能返回正确结果，否则返回x；`===, !==`可以比较x和z，当且仅当
完全相等时返回1或0，当不定状态可能出现的时候，使得不定状态不会向下传播。
使用数据比较器实现。

### 逻辑运算符

`!`为取非，`~`为按位取反，`&&, ||`表示逻辑与和逻辑或。
注意`a = 4'b1001; !a = 1'b0;`，而`~a = 4'b0110`。任何不定状态
的逻辑操作结果均为不定状态。

### 按位操作符

`~, &, |, ^`分别为按位取反，按位与，按位或和按位异或。

### 归约操作符（缩位运算符）

`&, |, ^`为单目运算符，将自身每一位进行运算。

### 移位运算符

`>>, <<`左边为被操作数，右边为移位数。左右补0。

### 条件运算符

`<condition>?<statement1>:<statement2>`，使用二选一数据选择器实现。

### 连接和复制运算符

`{}`为连接运算符，而`{{}}`为复制运算符，而该操作不对应电路。

## 模块

类似于元件的概念，代表一个基本的功能块。一个模块包括模块的开始和结束，模块
端口的定义，模块数据类型说明和模块逻辑功能的描述。

* 开始和结束：使用`module`和`endmodule`，而且`module`必须以';'结束
* 端口定义：在端口列表内定义`input, output, inout`等端口
* 数据类型说明：声明变量的数据类型，例如`wire, reg`等
* 逻辑功能描述：产生各种逻辑，一般使用`initial`，`always`语句实现

## Verilog程序简要分析

![简单逻辑电路(1)](https://vlab.ustc.edu.cn/guide/images/verilog/2.png)

简单逻辑电路代码如下：

```Verilog
module example(
input a,
input b,
input c,
output y
);

assign y = ~a & ~b & ~c | a & ~b & ~c | a & ~b & c;

endmodule
```

语法结构分析：

1. `module/endmodule`：表示模块的开始与结束
2. `example`：模块名，命名规则与C/C++相同
3. `assign`：赋值操作关键词，后面为赋值表达式，由表达式实现组合逻辑操作
4. `input/outpur`：表示信号的方向，此外还有`inout`型

![简单逻辑电路(2)](https://vlab.ustc.edu.cn/guide/images/verilog/6.png)

代码如下：

```Verilog
module gates(
    input [3:0] a,
    input [3:0] b,
    output [3:0] y1,
    output [3:0] y2,
    output [3:0] y3,
    output [3:0] y4,
    output [3:0] y5,
    output y6
);

assign y1 = a & b;    // AND
assign y2 = a | b;    // OR
assign y3 = a ^ b;    // XOR
assign y4 = ~(a & b); // NAND
assign y5 = ~(a | b); // NOR
assign y6 = &a;       // easier than y6 = a[0] & a[1] & a[2];

endmodule
```

代码分析：

1. `[3:0]`：表示该信号的位宽，习惯上将大数写前面而小数写后面
2. 注释规则与C/C++相同
3. 逻辑操作符对于单个或两个操作数正常操作，对于多个信号数进行广义操作

![一位全加器](https://vlab.ustc.edu.cn/guide/images/verilog/10.png)

代码如下：

```Verilog
module fulladder(
    input a,
    input b,
    input cin,
    output s,
    output cout
);
wire p, g; // internal nodes/intermediate variable

assign p = a ^ b;
assign g = a & b;
assign cout = p & cin;
assign s = (p ^ cin) | g;

endmodule
```

代码分析：

1. `wire`：线网型数据结构，表示线网型信号，与实际电路的连线对应。当input/output未指定数据类型时，默认为wire。另一种数据类型为`reg`，表示寄存器类型数据。
2. 内部信号：相当于中间变量，简化表达式，提高可读性

代码分析：

## 操作符优先级

![常用操作符及其优先级](https://vlab.ustc.edu.cn/guide/images/verilog/4.png)

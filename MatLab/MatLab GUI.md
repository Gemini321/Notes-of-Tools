# MatLab GUI

GUI(graphical user interface)是用户图形界面，是指由窗口、菜单、图表、光标
等图形对象组成的用户界面。

## GUI的开发

在MatLab开发GUI有两种方式：代码或使用GUIDE。

GUIDE的使用：

1. 在命令行窗口输入`guide`，选择`Create New GUI`选项新建GUI窗口
2. 选择四种GUI模板中的一个：

> Blank GUI(Default)：空白模板
> GUI with Uicontrols：带控制对象的GUI模板
> GUI with Axes and Menu：带坐标轴和菜单的GUI模板
> Modal Question Dialog：带模式问题对话框的GUI模板

3. 保存该模型，此时生成.fig文件来保存界面图形，.m文件保存主函数
4. 需求分析，分析需要什么元素和所需数量

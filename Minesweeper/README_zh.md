# Minesweeper -- A game coding with Pygame Zero.

[toc]

## 开发环境

python 版本: `3.10.0`

pgzrun

win11 64位



打包工具: `pyinstaller`, `Inno Setup Compiler`



### 测试环境

​	python 到`3.12.0`也可以运行。

​	win7 64位,32位 下也可以运行。


## 游戏资源

爆炸的声音，以及游戏通关的声音来源于[`pixabay`](https://pixabay.com/).  

游戏样式 `mahjong`风格的 `mine.jpg` 由好友 `LKH`绘制.



## 运行

### python程序运行

#### 安装模块

安装 `pgzero`模块: `pip install pgzero -i https://pypi.tuna.tsinghua.edu.cn/simple`

> 如果安装失败，请使用 `pip install --upgrade pip -i https://mirrors.tuna.tsinghua.edu.cn/` 升级pip再进行尝试。

#### 运行启动程序

运行`mine_sweeper_run.py`文件：`python mine_sweeper_run.py`



### `exe`程序运行

进入`release\\1.0`文件夹，运行`Minesweeper.exe`程序，进行安装。

安装后，打开安装目录，选择`mine_sweeper_run.exe`运行。



### 游戏说明

在游戏已经进行一半后，如果更换主题，请在点击`保存`后点击`更改`，重新开始`新一轮`，否则会导致部分功能(比如双击)失效。



**按键说明**:

鼠标左键: 揭开方块

鼠标右键: 标记方块 （可以标记`雷`或者`未知`）

双击鼠标左键: 探测的雷数与四周标记的雷数相同时，则快速揭开四周未揭开的方块



**游戏点击指南**:

游戏开始后，请点击任意`关卡`进入游戏；

游戏内，点击`重来`重新开始游戏；点击`主页`返回关卡选择；点击`选项`进入游戏设置页面；

游戏设置页面中，点击左上角`返回符号`返回到游戏中；在更改游戏地图数值后，点击`更改` 应用到游戏中；点击`保存`则保存当前游戏设置。



**游戏地图数值设置**:

地图行数 `row`，列数`col`，雷数`mine`满足以下规律:  
$
\left\{
\begin{aligned}
& 1 \le row \le 27 \\
& 1 \le col \le 37 \\
& 0.08 < \frac{mine}{row  \times col} < 0.92
\end{aligned}
\right.
$

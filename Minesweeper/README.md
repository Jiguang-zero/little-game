# Minesweeper -- A game coding with Pygame Zero.

[toc]

## Development Enviroment

python version: `3.10.0`

pgzrun

win11 64 bit



Tools for packaging as `exe` application: `pyinstaller`, `Inno Setup Compiler`



### Test Environment

​	We can run the project with python `3.12.0`.

​	And the project can also run at win 7 , 64bit.

## Resource

The sound of explosions (losing the game) and the sound of wining the game come from [`pixabay`](https://pixabay.com/).

The image `mine.jpg` of the style `mahjong` was drawn by my friend `LKH`.



## Run

### Run with python

#### Install the module

Please use  `pip install pgzero -i https://pypi.tuna.tsinghua.edu.cn/simple` to install `pgzero` module.

> You can try to upgrade pip firstly with `pip install --upgrade pip -i https://mirrors.tuna.tsinghua.edu.cn/` if you cannot install the module.

#### Run python file.

Please run `mine_sweeper_run.py` file using `python mine_sweeper_run.py`. Please make sure you have python environment if you start the project this way.



### Run `exe` application for Windows

Please run the setup application `Minesweeper.exe` to install the application first, which is in the folder: `release\\1.0`.

Then go to the directory where you install the program to run `mine_sweeper_run.exe`.



### Instruction

If you want to change the theme halfway through the game, please click `保存` and then click `更改` to `start a new round`. Otherwise, it may cause some functions (such as double clicking) to fail.



**Key Description **:

Left mouse button: Uncover blocks

Right mouse button: Mark square (can be marked as `mine` or `unknown`)

Double click the left mouse button: When the number of detected mines is the same as the number of mines marked around it, quickly uncover the unopened blocks around it.



**Game Click Guide **:

After the game starts, please click on any `level` to enter the game;

In the game, click `重来` to restart the game; Click `主页` to return to level selection; Click `选项` to enter the game settings page;

On the game settings page, click on the 'Return Symbol' in the upper left corner to return to the game; After changing the game map values, click     `更改` to apply to the game; Click `保存` to save the current game settings.



**The value of the game map**:

The number of rows `row`, columns `col`,  and mines `mine` in the map should satisfy the following `formula`:  
$
\left\{
\begin{aligned}
& 1 \le row \le 27 \\
& 1 \le col \le 37 \\
& 0.08 < \frac{mine}{row  \times col} < 0.92
\end{aligned}
\right.
$
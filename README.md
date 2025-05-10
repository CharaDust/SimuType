# 模拟输入器 - SimuType

该项目复刻自由tushar5526开发的[Autotype](https://github.com/tushar5526/Autotype)。此复刻版本修复了无法运行的bug，并加入了针对第三方加密远控软件以及跨系统虚拟机的支持。  
This project is a fork of [Autotype](https://github.com/tushar5526/Autotype), originally developed by tushar5526. This forked version fixes the non-functioning bug and adds support for third-party encrypted remote control software and cross-system virtual machines.

一个简单且迷你的Python小脚本，针对剪贴板工作异常的远程控制进行预设文本的批量自动输入，适用于虚拟机，远程桌面，第三方远程控制混合使用的场景。  
A quick and small python script that batch automatic input of preset text for remote control with clipboard malfunction, suitable for scenarios involving mixed usage of virtual machines, remote desktops, and third-party remote control tools.

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/codingid6)
[![GitHub issues](https://img.shields.io/github/issues/CharaDust/SimuType)](https://github.com/CharaDust/SimuType/issues)
[![GitHub forks](https://img.shields.io/github/forks/CharaDust/SimuType)](https://github.com/CharaDust/SimuType/network)
[![GitHub stars](https://img.shields.io/github/stars/CharaDust/SimuType)](https://github.com/CharaDust/SimuType/stargazers)
[![GitHub license](https://img.shields.io/github/license/CharaDust/SimuType)](https://github.com/CharaDust/SimuType/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/CharaDust/SimuType)
<br>

**在Windows，mac OS，Linux均可使用**  
**Works for windows, mac and linux**

<img src="https://i.imgur.com/pUfYwD0.gif">

## 复刻版本漏洞修复与功能更新
- 修复了因代码内调用了已经弃用的函数导致无法运行的漏洞
- 修复了由于第三方远程控制平台（如向日葵和ToDesk）的加密传递算法导致输入异常
- 添加了随机输入延迟（线性）以防远程控制平台重复发包拦截
- 现在对于 Windows 平台中文用户打包了一个软件


# 前置环境 - Pre-requisites
`python3.9.x`
`pip`

# 开发配置 - Development Setup
- 创建一个虚拟环境`pipenv`，如果你不想在Windows创建虚拟环境（在你本身就是虚拟机的情况下），你可以直接使用文件夹内的cmd脚本，注意文件路径
- Create a new virtual environment using `pipenv`
```bash
# 注意：macOS 从 macOS 12.3（Monterey，2022年3月发布） 开始，
# 正式移除了系统内置的 Python 2.7 环境。
# 如果你使用的是早期版本的mac OS，
# 你可能需要将pip和python替换为pip3和python3
# Note: Starting with macOS 12.3 (Monterey, released March 2022),
# Apple has officially removed the built-in Python 2.7 environment.
# If you're using an earlier version of macOS,
# you may need to replace pip and python with pip3 and python3
pip install pipenv --user

# 创建一个虚拟环境然后安装前置
# create venv and install dependencies from Pipfile
pipenv install
```
- 激活这个环境
- Activate the environment
```bash
pipenv shell

# 检查pip是否工作正常
# check if activated
pip -V

# 安装依赖文件
# 
pip install -r requirements.txt
```

- For Linux
```bash

# For Ubuntu or other distros with Apt:
sudo apt-get install python3-tk

# For Fedora:
sudo dnf install python3-tkinter

# For Arch Based
sudo pacman -S tk

```

- 运行命令行程序（目前在Windows平台上有BUG导致无法运行，目前正在想办法修复）
- Run it as CLI app

> Provide the path of the file to be autotyped and the delay time through teminal/shell.

```bash
python3 command_line_script --path filePath --delay delay_before_typing
```

### 运行图形界面程序
### Run the GUI if you are not familiar with CLI apps.

- 运行脚本`python3 GUI_script.py`或者运行打包好的exe文件（Windows）
- Run the script `python3 GUI_script.py`
<img src="https://i.imgur.com/QhDjIqe.jpeg">

- 你可以简单地将要输入的文本让你放入大输入框，在左侧配置时间（留空输入默认值），然后点击`Start Typing`按钮后迅速点击需要模拟输入的虚拟机/远程界面。等待时间结束后，脚本就会模拟键盘自动输入内容
- You can simply type your code in the textbox , enter the time delay and click the `Start Typing` button.The script will then type your code for you.
<img src="https://i.imgur.com/3ysBzIT.gif">

- 如果你有准备好的文本文件，可以不向大输入框输入内容，直接点击`Start Typing`按钮就可以选择文件自动输入
- If your code is in a file , then leave the textbox blank , enter the time delay and click `Start Typing` button.A file exploror prompt will open asking you to select the file.Simply select your file and Done! Autotype will type your code for you.
<img src="https://imgur.com/SOauxRx.gif">

- There are two themes in the GUI Script: Dark and Light. By clicking the toggle in the bottom left corner of the window, you can switch between the two.
<img src="https://imgur.com/NjLfWcL.gif)">

### Run it as follows if you are not familiar with CLI apps.
Put the text inside `code` in `Simulator/simulate_keyboard.py` as follows

```
Line 13
code = """
    #include<bits/stdc++.h>
    {
        .
        .
        .
    }
"""
# Make sure to use triple quotes as it will preserve the code format.
```
- Run the script `python3 Simulator/simulate_keyboard.py`
- The script will start typing after 3s (wait or delay time can be tuned)
- After running the script click on the window to move your cursor wherever you want to auto-type.
<hr>

## 十分感谢原作者及其贡献者所提供的代码范例
## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping AutoType grow.
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=CharaDust/SimuType)](https://github.com/CharaDust/SimuType/graphs/contributors)

## 给予支持
## 🙏 Support++

这个项目需要你手里那颗闪亮的星星，不要忘记给[原作者](https://github.com/tushar5526/Autotype)留一颗星星哦~
This project needs your shiny star ⭐.
Don't forget to leave a star ⭐️

制作来自派森，构建来自爱
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)




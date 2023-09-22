# zhueBot

![GitHub Repo stars](https://img.shields.io/github/stars/zhue001/zhueBot)
![GitHub all releases](https://img.shields.io/github/downloads/zhue001/zhueBot/total)
![](https://img.shields.io/badge/Using-websocket-green)
![](https://img.shields.io/badge/Category-Gadget-green)
![](https://img.shields.io/badge/Formatted%20by-black-white)
![GitHub issues](https://img.shields.io/github/issues-raw/zhue001/zhueBot)

## 兼容于
1. Hack Chat
2. Light Chat

## 条件
要求安装一下运行库:
1. websocket
2. websocket-client
3. json
4. string
5. random
6. datetime
7. re
+ 请按照顺序安装，否则可能会出现问题
### 一键安装脚本
执行 `setup.bat` (Windows) 或 `setup.sh` (Linux族) 即可一键安装 （需确保`pip`可以调用）

## 配置
* 打开`main.py`，跳转到第178行，将debug变量的值替换为`True`(如果想要调试)或`False`(如果不想要调试)
* 打开`main.py`，跳转到第224行，将sysadmin变量的值替换为你的识别码
* 打开`main.py`，跳转到第884行，将botPass变量的值替换为你想要的机器人的密码
* 打开`main.py`，跳转到第876行和第1021行，将`zhueBot`替换为你想要的bot前缀
* 打开`main.py`，跳转到第906行，将color字段的值替换为你想要的bot颜色（16进制）（只适用于Hack Chat）
* 打开`main.py`，跳转到第558行，将head字段的值替换为你想要的bot头像地址（只适用于Light Chat）

## 使用
执行`python main.py`，并按照提示设置要想加入的频道（如`lounge`）
具体内容请使用在配置时设置的系统管理员识别码登录设置的频道，并发送`&help`查看使用帮助

## 提交问题
请在issue栏目提交问题，会尽快处理
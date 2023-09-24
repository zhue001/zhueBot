# 定义常量
SERVER = "wss://hack.chat/chat-ws"  # 别改
CHANNEL = input(
    "要加入哪个房间？"
)
# 程序内部代码，请勿随意更改
# 导入库
from websocket import (
    create_connection as connect,
)
from json import (
    loads,
    dumps,
)
from string import (
    ascii_lowercase,
    digits,
)
from random import (
    randint,
    choice,
)
from datetime import (
    datetime,
)
from re import (
    match,
    search,
)

# 定义变量
# 不可更改区
afks = (
    []
)
lastNoticefile = open(
    "lastnotice.txt",
    "r",
    encoding="utf-8",
)  # 打开存储d的最新公告
lastNotice = (
    lastNoticefile.read()
)  # 读取最新公告（解码）
lastNoticefile.close()  # 关闭文件
uhashfile = open(
    "userhashes.json",
    "r",
    encoding="utf-8",
)  # 打开存储的用户hash列表
uhash = loads(
    uhashfile.read()
)  # 读取用户hash列表（解码）
uhashfile.close()  # 关闭文件
utypefile = open(
    "usertypes.json",
    "r",
    encoding="utf-8",
)  # 打开存储的用户类型列表
utype = loads(
    utypefile.read()
)  # 读取用户类型列表（解码）
utypefile.close()  # 关闭文件
joinmsgfile = open(
    "joinmsgs.json",
    "r",
    encoding="utf-8",
)  # 打开存储的用户自定义欢迎语列表
joinmsg = loads(
    joinmsgfile.read()
)  # 读取用户自定义欢迎语列表（解码）
joinmsgfile.close()  # 关闭文件
allmsglog = (
    []
)
bansfile = open(
    "bans.txt",
    "r",
    encoding="utf-8",
)  # 打开存储的封禁列表
bans = bansfile.read().split(
    "\n"
)  # 读取封禁列表（解码）
bansfile.close()  # 关闭文件
warns = [
    None,
    None,
    None,
]
spam = [
    None,
    None,
    None,
]
noticedlang = (
    {}
)
privatemode = False
spamindex = 0
warnindex = 0
lastmsg = {
    "nick": "Radium",
    "time": 0,
}
lastmsg2 = {
    "nick": "Radium",
    "time": 0,
}
lastmsg3 = {
    "nick": "Radium",
    "time": 0,
}
needdaming = True
gameflag = 0
needconfirm = 0
confirmer = "Radium"
confirmflag = 0
idiomfile = open(
    "idiom.txt",
    "r",
    encoding="utf-8",
)  # 打开成语列表
idiom = (
    idiomfile.read()
)  # 读取文件
idiom = idiom.split(
    "\n"
)  # 把文本格式的成语列表转为数组
idiomfile.close()  # 关闭文件
idiomsolitaire = False
# 可更改区
hellos = [
    "Hi",
    "hi"
    "早上好",
    "中午好",
    "晚上好",
    "hello",
    "Hello",
    "你好",
    "大家好",
]
animalsounds = [
    {
        "text": "哼哼",
        "img": None,
    },
    {
        "text": "嗷呜",
        "img": None,
    },
]
randommax = 1000
randommin = 0
mml = 200
girls = [
    "西施",
    "黑丝",
    "白丝",
]
goodword = (
    []
)
badword = (
    []
)
advusrfile = open(
    "advusrs.txt",
    "r",
    encoding="utf-8",
)  # 打开高级用户列表
advusr = advusrfile.read().split(
    "\n"
)  # 把文本格式的高级用户列表转为数组
advusrfile.close()  # 关闭文件
imgs = [
    "蔡旭坤裸奔.png"
]
debug = True
afkactions = [
    "吃饭",
    "睡觉",
    "上学",
    "写作业",
    "写代码",
    "自杀",
    "念经",
    "涅磐",
    "圆寂",
]
buddhas = (
    {}
)
welcomemsgpart1 = [
    "我去，",
    "早上好，",
    "Hello ",
    "嘿，",
]
welcomemsgpart2 = [
    "，热烈欢迎你！",
    "，你来啦！",
    "，嘿，大家都想你了呢",
    "，你终于到了，我们太想你了！",
]
awa = [
    "qwq",
    "qaq",
    "awa",
    "uwu",
    "uvu",
    "pwp",
    "paq",
    "pwq",
    "nvn",
    "owo",
    "ovo",
    "pap",
    "nvn",
    "pap",
    "ava",
]

# 设置系统管理员
sysadmin = ""


# 定义工具函数
def calculate(
    expression,
):  # 算数
    if not match(
        r"^[0-9+\-*/.π\^\(\)\[\]\{\}\s]+$",
        expression,
    ):
        raise ValueError(
            "Invalid expression"
        )

    expression = expression.replace(
        "π",
        "3.141",
    )

    # 处理最内层的括号
    def calculate_inner(
        expression,
    ):
        # 处理"^"运算符
        while (
            "^"
            in expression
        ):
            isMatch = search(
                r"(\d+(\.\d+)?)\s*\^\s*(\d+(\.\d+)?)",
                expression,
            )
            if isMatch:
                base = float(
                    isMatch.group(
                        1
                    )
                )
                exponent = float(
                    isMatch.group(
                        3
                    )
                )
                result = (
                    base
                    ** exponent
                )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

        # 处理乘法和除法
        while (
            "*"
            in expression
            or "/"
            in expression
        ):
            isMatch = search(
                r"(\d+(\.\d+)?)\s*([*/])\s*(\d+(\.\d+)?)",
                expression,
            )
            if isMatch:
                num1 = float(
                    isMatch.group(
                        1
                    )
                )
                operator = isMatch.group(
                    3
                )
                num2 = float(
                    isMatch.group(
                        4
                    )
                )
                if (
                    operator
                    == "*"
                ):
                    result = (
                        num1
                        * num2
                    )
                else:
                    result = (
                        num1
                        / num2
                    )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

        # 处理加法和减法
        while (
            "+"
            in expression
            or "-"
            in expression
        ):
            isMatch = search(
                r"(\d+(\.\d+)?)\s*([+\-])\s*(\d+(\.\d+)?)",
                expression,
            )
            if isMatch:
                num1 = float(
                    isMatch.group(
                        1
                    )
                )
                operator = isMatch.group(
                    3
                )
                num2 = float(
                    isMatch.group(
                        4
                    )
                )
                if (
                    operator
                    == "+"
                ):
                    result = (
                        num1
                        + num2
                    )
                else:
                    result = (
                        num1
                        - num2
                    )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

        return float(
            expression
        )

    # 处理括号
    while (
        "("
        in expression
        or "["
        in expression
        or "{"
        in expression
    ):
        # 处理最内层的圆括号
        while (
            "("
            in expression
        ):
            isMatch = search(
                r"\(([^\(\)]+)\)",
                expression,
            )
            if isMatch:
                sub_expression = isMatch.group(
                    1
                )
                result = calculate_inner(
                    sub_expression
                )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

        # 处理最内层的方括号
        while (
            "["
            in expression
        ):
            isMatch = search(
                r"\[([^\[\]]+)\]",
                expression,
            )
            if isMatch:
                sub_expression = isMatch.group(
                    1
                )
                result = calculate_inner(
                    sub_expression
                )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

        # 处理最内层的花括号
        while (
            "{"
            in expression
        ):
            isMatch = search(
                r"\{([^\{\}]+)\}",
                expression,
            )
            if isMatch:
                sub_expression = isMatch.group(
                    1
                )
                result = calculate_inner(
                    sub_expression
                )
                expression = expression.replace(
                    isMatch.group(
                        0
                    ),
                    str(
                        result
                    ),
                )
            else:
                raise ValueError(
                    "Invalid expression"
                )

    result = calculate_inner(
        expression
    )
    return result


def WhoIsbjcb(
    user,
):  # 找被继承佛
    for (
        key,
        value,
    ) in (
        buddhas.items()
    ):
        if (
            value[
                "jicheng"
            ]
            == user
        ):
            return key
    return False


def isArrayAllItemSame(
    arr,
):  # 检查数组每个项是否一致
    unique_items = set(
        arr
    )  # 将数组转换为集合，去除重复项
    if (
        len(
            unique_items
        )
        == 1
    ):
        return True
    else:
        return False


def isJiChengSame():  # 判断有无一样的继承者
    jicheng_values = [
        value[
            "jicheng"
        ]
        for value in buddhas.values()
        if value[
            "jicheng"
        ]
    ]
    unique_values = set(
        jicheng_values
    )

    return len(
        jicheng_values
    ) != len(
        unique_values
    )


def send(
    msg,
):  # 公屏发消息
    ws.send(
        dumps(
            {
                "cmd": "chat",
                "text": msg,
                "head": "https://www.zhue.com.cn/uploads/litimg/230901/094531443SY548.jpg",
            }
        )
    )


def w(
    user,
    msg,
):  # 私聊发消息
    ws.send(
        dumps(
            {
                "cmd": "whisper",
                "text": msg,
                "nick": user,
                "head": None,
            }
        )
    )


def getPartOfDay():  # 获取当前时间属于上午、中午还是晚上
    current_hour = (
        datetime.now().hour
    )

    if (
        current_hour
        < 12
    ):
        return "早上好"  # 早上
    elif (
        current_hour
        < 18
    ):
        return "中午好"  # 中午
    else:
        return "晚上好"  # 晚上


def unAFK(
    user,
):  # 解除AFK
    new_afks = [
        afk
        for afk in afks
        if afk[
            "user"
        ]
        != user
    ]
    return new_afks


def removeArrayItem(
    arr,
    target,
):  # 删除数组中某个字符串
    return [
        item
        for item in arr
        if item
        != target
    ]


def removeDictItem(
    dictionary,
    target,
):  # 删除字典中某个值
    return {
        key: value
        for key, value in dictionary.items()
        if key
        != target
    }


def isAFK(
    user,
):  # 判断是否在挂机
    for afk in afks:
        if (
            user
            == afk[
                "user"
            ]
        ):
            return afk[
                "user"
            ]
    return False


def isAFK_unfull(
    string,
):  # 粗略判断是否在挂机
    for afk in afks:
        if (
            afk[
                "user"
            ]
            in string
        ):
            return afk[
                "user"
            ]
    return False


def getAFKListIndex(
    user,
):  # 获取AFK索引
    for (
        index,
        afk,
    ) in enumerate(
        afks
    ):
        if (
            afk[
                "user"
            ]
            == user
        ):
            return index
    return (
        -1
    )


def isHave(
    string,
    arr,
):  # 判断字符串是否包含数组中的任意内容
    for item in arr:
        if (
            item
            in string
        ):
            return item
    return False


def isValidRGB(
    color,
):  # 判断是否是有效RGB颜色
    color = (
        color.strip()
    )  # 去除首尾空格
    if color.startswith(
        "#"
    ):
        color = color[
            1:
        ]  # 去除开头的 #
    if (
        len(
            color
        )
        == 6
    ):
        try:
            int(
                color,
                16,
            )  # 尝试将颜色值转换为整数
            return True
        except ValueError:
            return False
    elif (
        len(
            color
        )
        == 3
    ):
        try:
            int(
                color
                * 2,
                16,
            )  # 将三位颜色值复制并转换为整数
            return True
        except ValueError:
            return False
    return False


def HexToRgb(
    hex_value,
):  # 将 RGB 颜色值转换为十六进制颜色代码
    if hex_value.startswith(
        "#"
    ):
        hex_value = hex_value[
            1:
        ]  # 移除"#"前缀

    if (
        len(
            hex_value
        )
        == 3
    ):
        red = int(
            hex_value[
                0
            ]
            * 2,
            16,
        )
        green = int(
            hex_value[
                1
            ]
            * 2,
            16,
        )
        blue = int(
            hex_value[
                2
            ]
            * 2,
            16,
        )
    elif (
        len(
            hex_value
        )
        == 6
    ):
        red = int(
            hex_value[
                0:2
            ],
            16,
        )
        green = int(
            hex_value[
                2:4
            ],
            16,
        )
        blue = int(
            hex_value[
                4:6
            ],
            16,
        )
    else:
        return "Invalid hex value"

    return "{},{},{}".format(
        red,
        green,
        blue,
    )


def RgbToHex(
    rgb_value,
):
    try:
        # 将输入的字符串按逗号分隔成红、绿、蓝三个通道的值
        (
            red,
            green,
            blue,
        ) = map(
            int,
            rgb_value.split(
                ","
            ),
        )

        # 将每个通道的值转换为两位的十六进制字符串，并拼接在一起
        hex_value = "#{:02X}{:02X}{:02X}".format(
            red,
            green,
            blue,
        )
    except:
        return "Invalid rgb value"

    return hex_value


def findKey(
    mydict,
    finding,
):  # 查找字典中值是finding的所有项
    result = (
        []
    )
    for (
        key,
        value,
    ) in (
        mydict.items()
    ):
        if (
            value
            == finding
        ):
            result.append(
                key
            )
    return result


# 建立连接
ws = connect(
    SERVER
    + "/chat-ws/"
    + CHANNEL
)
botNick = (
    "zhueBot"
    + str(
        randint(
            100,
            999,
        )
    )
)
botPass = ""
whitelist = [
    botNick,
]  # 设置白名单
# 加入房间
ws.send(
    dumps(
        {
            "cmd": "join",
            "channel": CHANNEL,
            "nick": botNick
            + "#"
            + botPass,
            "head": None,
        }
    )
)
# 设置颜色
ws.send(
    dumps(
        {
            "cmd": "changecolor",
            "color": "008F64",
            "head": None,
        }
    )
)
# 主循环
while True:
    try:
        if (
            needdaming
            == True
            and datetime.now().strftime(
                "%M"
            )
            == "00"
        ):  # 判断是否需要报时
            file = open(
                "bans.txt",
                "w+",
            )  # 打开文件（自动保存配置）
            file.write(
                "\n".join(
                    bans
                )
            )  # 保存
            file.close()  # 关闭
            file = open(
                "lastnotice.txt",
                "w+",
                encoding="utf-8",
            )  # 打开文件（自动保存配置）
            file.write(
                ""
                if lastNotice
                == None
                else lastNotice
            )  # 保存
            file.close()  # 关闭
            file = open(
                "userhashes.json",
                "w+",
                encoding="utf-8",
            )  # 打开文件（自动保存配置）
            file.write(
                dumps(
                    uhash
                )
            )  # 保存
            file.close()  # 关闭
            file = open(
                "usertypes.json",
                "w+",
                encoding="utf-8",
            )  # 打开文件（自动保存配置）
            file.write(
                dumps(
                    utype
                )
            )  # 保存
            file.close()  # 关闭
            file = open(
                "joinmsgs.json",
                "w+",
                encoding="utf-8",
            )  # 打开文件（自动保存配置）
            file.write(
                dumps(
                    joinmsg
                )
            )  # 保存
            file.close()  # 关闭
            file = open(
                "advusrs.txt",
                "w+",
                encoding="utf-8",
            )  # 打开文件（自动保存配置）
            file.write(
                "\n".join(
                    advusr
                )
            )  # 保存
            file.close()  # 关闭
            send(
                "&daming"
            )  # 报时
            if (
                lastNotice
                != None
            ):  # 判断是否有公告
                send(
                    lastNotice
                )  # 发送公告
            needdaming = False  # 设置为假，确保每小时只自动报时一次
        if (
            datetime.now().strftime(
                "%M"
            )
            != "00"
        ):  # 判断是否需要更改标记等到下一次报时
            needdaming = True  # 设置为真，等待下一次报时
        try:  # 尝试接收数据
            data = loads(
                ws.recv()
            )  # 获取数据
        except:  # 连接断开，重新连接
            # 重连服务器
            ws = connect(
                SERVER
                + "/"
                + CHANNEL
            )
            # 复制旧机器人名称
            botOldNick = botNick
            # 设置新名称
            botNick = (
                "zhueBot"
                + str(
                    randint(
                        100,
                        999,
                    )
                )
            )
            # 加入房间
            ws.send(
                dumps(
                    {
                        "cmd": "join",
                        "channel": CHANNEL,
                        "nick": botNick
                        + "#"
                        + botPass,
                        "head": None,
                    }
                )
            )
            # 踢出旧机器人
            ws.send(
                dumps(
                    {
                        "cmd": "kickzom",
                        "nick": botOldNick,
                    }
                )
            )
        if (
            data[
                "cmd"
            ]
            == "onlineAdd"
        ):  # 欢迎用户、设置hash、踢出被封用户、检查是否为私有模式
            if (
                privatemode
                and data[
                    "nick"
                ]
                not in whitelist
            ):
                randomChannel = "".join(
                    choice(
                        ascii_lowercase
                        + digits
                    )
                    for _ in range(
                        10
                    )
                )
                w(
                    data[
                        "nick"
                    ],
                    f"非常抱歉，目前该房间处于私有模式，您不在白名单中，你目前已被移动到 ?{randomChannel}",
                )
                ws.send(
                    dumps(
                        {
                            "cmd": "moveuser",
                            "nick": data[
                                "nick"
                            ],
                            "channel": randomChannel,
                        }
                    )
                )
            if (
                data[
                    "nick"
                ]
                in bans
                or data[
                    "trip"
                ]
                in bans
            ):
                ws.send(
                    dumps(
                        {
                            "cmd": "kick",
                            "nick": data[
                                "nick"
                            ],
                        }
                    )
                )
            uhash[
                data[
                    "nick"
                ]
            ] = data[
                "hash"
            ]  # 设置hash
            try:
                send(
                    joinmsg[
                        data[
                            "nick"
                        ]
                    ]
                )  # 发送用户设置的欢迎语
            except:
                send(
                    choice(
                        welcomemsgpart1
                    )
                    + data[
                        "nick"
                    ]
                    + choice(
                        welcomemsgpart2
                    )
                )  # 发送预设欢迎语
        if (
            data[
                "cmd"
            ]
            == "chat"
        ):  # 判断是否有消息
            # 开始下一步处理
            u = data[
                "nick"
            ]
            m = data[
                "text"
            ]
            s = data[
                "time"
            ]
            try:
                t = data[
                    "trip"
                ]
            except:
                # 对无识别码用户的处理
                t = "000000"
            if (
                u
                in bans
                and t
                != sysadmin
                and t
                not in advusr
                and u
                != botNick
            ):
                # 跳过被封禁用户的处理
                continue
            if (
                isArrayAllItemSame(
                    warns
                )
                and warns[
                    0
                ]
                != None
            ):  # 判断是否达到三次警告自动封禁
                send(
                    f"&ban {warns[0]}"
                )  # 封禁
                warns[
                    0
                ] = None  # 重置
            if (
                u
                == lastmsg[
                    "nick"
                ]
                and u
                == lastmsg2[
                    "nick"
                ]
                and u
                == lastmsg3[
                    "nick"
                ]
                and t
                != sysadmin
                and t
                not in advusr
                and u
                != botNick
            ):  # 高级用户、系统管理员和Bot本身跳过刷屏检测
                if (
                    s
                    - lastmsg[
                        "time"
                    ]
                    < 2001
                ):
                    if (
                        lastmsg[
                            "time"
                        ]
                        - lastmsg2[
                            "time"
                        ]
                        < 2001
                    ):
                        if (
                            lastmsg2[
                                "time"
                            ]
                            - lastmsg3[
                                "time"
                            ]
                            < 2001
                        ):
                            spam[
                                spamindex
                            ] = u
                            spamindex += 1
                            if (
                                spamindex
                                == 3
                            ):  # 重置刷屏数组索引，防止溢出
                                spamindex = 0
            if debug:
                print(
                    spam
                )  # debug
            if (
                isArrayAllItemSame(
                    spam
                )
                and spam[
                    0
                ]
                != None
            ):  # 判断是否已经刷屏
                send(
                    f"&warning {spam[0]}"
                )
                spam[
                    0
                ] = None  # 重置刷屏数组
            if m.startswith(
                "# "
            ):  # 大字警告
                send(
                    f"@{u} 请不要经常发大字"
                )  # 提醒
            if (
                m
                in hellos
            ):  # 判断是否在打招呼
                send(
                    f"@{u} {getPartOfDay()}"
                )
            if (
                isHave(
                    m,
                    badword,
                )
                and u
                != botNick
                and t
                not in advusr
                and t
                != sysadmin
            ):  # 判断是否包含屏蔽词，系统管理员、bot本身、高级用户不做处理
                send(
                    f"&warning {u}"
                )  # 警告
            if isHave(
                m,
                goodword,
            ):  # 判断是否包含优秀词
                w(
                    u,
                    "没想到你连这个词都会，厉害呀",
                )  # 表扬
            if (
                len(
                    m
                )
                > mml
                and u
                != botNick
                and t
                not in advusr
                and t
                != sysadmin
            ):  # 长文本警告，机器人本身、高级用户和系统管理员不判断
                send(
                    f"@{u} 请不要发送过长的内容"
                )  # 提醒
            # 检测刷屏用
            lastmsg3 = lastmsg
            lastmsg2 = lastmsg
            lastmsg = data
            if debug:
                print(
                    lastmsg
                )  # debug
                print(
                    lastmsg2
                )  # debug
                print(
                    lastmsg3
                )  # debug
            if debug:
                print(
                    data
                )  # debug
            # 记录消息
            allmsglog.append(
                f"{u}在{datetime.now().strftime('%m-%d %a %H:%M')}说了{m}"
            )
            if (
                len(
                    allmsglog
                )
                == 100
            ):  # 判断是否达到100条
                allmsglog = (
                    []
                )  # 重置

            if (
                isAFK_unfull(
                    m
                )
                and u
                != botNick
            ):  # 判断是否有人正在找挂机者，机器人本身跳过
                reason = afks[
                    getAFKListIndex(
                        u
                    )
                ][
                    "reason"
                ]  # 获取原因
                send(
                    f"@{u} 抱歉，{isAFK_unfull(m)}正在{reason}呢，等会儿吧"
                )  # 提醒

            if isAFK(
                u
            ):  # 判断发消息的是不是挂机者
                afks = unAFK(
                    u
                )
                send(
                    f"@{u} 欢迎回来，大家都想死你了！"
                )
            # 添加用户类型记录
            utype[
                u
            ] = "user"
            if (
                m
                in awa
                and u
                != botNick
            ):
                send(
                    f"@{u} {choice(awa)}"
                )
            if (
                "@"
                in m
                and u
                != botNick
            ):
                w(
                    m.split()[
                        0
                    ][
                        1:
                    ],
                    f"{u}: {' '.join(m.split()[1:])}",
                )
            # 从现在开始正式判断指令
            if m.startswith(
                "&"
            ):  # 判断是否在执行指令
                fcommand = (
                    m.split()
                )  # 初解析指令
                command = fcommand[
                    0
                ]  # 获取是什么指令（去除参数）
                if (
                    len(
                        fcommand
                    )
                    > 1
                ):  # 判断是否带参
                    parm = " ".join(
                        fcommand[
                            1:
                        ]
                    )  # 设置参数
                else:
                    parm = ""  # 对不带参数时进行特殊处理
                if (
                    t
                    in advusr
                ):  # 设置权限
                    perm = 2
                elif (
                    t
                    == sysadmin
                ):  # 设置权限
                    perm = 3
                elif (
                    t
                    in bans
                    or u
                    in bans
                ):  # 设置权限
                    perm = 0
                else:  # 设置权限
                    perm = 1
                if (
                    data[
                        "nick"
                    ]
                    == botNick
                ):  # 如果是机器人本身，单独执行判断，不列入普通执行队列
                    if (
                        command
                        == "&ping"
                    ):
                        global ping_value
                        global ping_request_time
                        if (
                            parm
                            != ping_value
                        ):
                            send(
                                "参数不匹配"
                            )
                        else:
                            send(
                                f"延迟: {s - ping_request_time}毫秒"
                            )
                    elif (
                        command
                        == "&daming"
                    ):
                        send(
                            f"嗷嗷！现在已经{datetime.now().strftime('%H')}点了"
                        )
                    elif (
                        command
                        == "&warning"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            warns[
                                warnindex
                            ] = parm
                            warnindex += 1
                            if (
                                warnindex
                                == 3
                            ):
                                warnindex = 0
                            send(
                                f"@{parm} 警告，不要继续违规行为"
                            )
                    elif (
                        command
                        == "&ban"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                in bans
                            ):
                                send(
                                    "此人已经被阻止访问"
                                )
                            else:
                                bans.append(
                                    parm
                                )
                                send(
                                    f"成功阻止访问{parm}"
                                )
                                ws.send(
                                    dumps(
                                        {
                                            "cmd": "kick",
                                            "nick": parm,
                                        }
                                    )
                                )
                    continue  # 防止进入普通判断
                if (
                    perm
                    >= 3
                ):  # 系统管理员才能执行的权限
                    if (
                        command
                        == "&help"
                    ):
                        w(
                            u,
                            """
        您的用户组: 系统管理员
        可用指令：
        `&help`:获得帮助
        `&addadvusr`:添加高级用户
        `&deladvusr`:删除高级用户
        `&addyxc`:添加优秀词
        `&delyxc`:删除优秀词
        `&ping`:获取bot到服务器延迟
        `&allmsglog`:获取最近100条消息
        `&setcolor`:设置机器人颜色
        `&daming`:获取时间
        `&pbclist`:屏蔽词列表
        `&setjoinmsg`:设置欢迎语
        `&getusrtype`:获取某用户类型
        `&getusrhash`:获取某用户hash
        `&bans`:封禁列表
        `&ban`:封禁用户
        `&unban`:解封用户
        `&addwhitelist`:添加白名单
        `&delwhitelist`:删除白名单
        `&kick`:踢出用户
        `&kill`:击杀用户
        `&privatemode`:私有模式
        `&publicmode`:公众模式
        `&setmml`:设置最大消息长度
        `&addpbc`:添加屏蔽词
        `&delpbc`:删除屏蔽词
        `&gn`:猜数字
        `&calc`:计算器
        `&reset`:重置
        `&girl`:看辣妹
        `&animal`:随机动物叫声
        `&rand`:随机数
        `&warning`:警告用户
        `&afk`:挂机
        `&update`:检查更新
        `&randomimg`:获取随机美女图片
        `&rgb2hex`:RGB颜色转HEX
        `&hax2rgb`:HEX颜色转RGB
        `&setrandmax`:设置随机数最大值
        `&setrandmin`:设置随机数最小值
        `&getpubyhash`:通过hash获取与他IP相同的用户
        `&newanimal`:新动物
        `&newanimalwithimg`:新动物（带图片）
        `&mybuddha`:查看自己是什么佛
        `&buddhas`:查看佛列表
        `&setjcb`:设置佛位继承者
        `&niepan`:涅磐成佛
        `&yuanji`:圆寂自杀
        `&forceyj`:强制一个用户圆寂
        `&sendnotice`:发送公告
        `&idiomsolitaire`:成语接龙
        `&save`:手动保存配置
                            """,
                        )
                        continue
                    elif (
                        command
                        == "&setcolor"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`color`"
                            )
                        elif (
                            isValidRGB(
                                parm
                            )
                            == False
                        ):
                            send(
                                "颜色值无效"
                            )
                        else:
                            ws.send(
                                dumps(
                                    {
                                        "cmd": "changecolor",
                                        "color": parm,
                                        "head": None,
                                    }
                                )
                            )
                            send(
                                "颜色更改成功"
                            )
                    elif (
                        command
                        == "&save"
                    ):
                        file = open(
                            "bans.txt",
                            "w+",
                        )  # 打开文件（保存配置）
                        file.write(
                            "\n".join(
                                bans
                            )
                        )  # 保存
                        file.close()  # 关闭
                        file = open(
                            "lastnotice.txt",
                            "w+",
                            encoding="utf-8",
                        )  # 打开文件（保存配置）
                        file.write(
                            ""
                            if lastNotice
                            == None
                            else lastNotice
                        )  # 保存
                        file.close()  # 关闭
                        file = open(
                            "userhashes.json",
                            "w+",
                            encoding="utf-8",
                        )  # 打开文件（保存配置）
                        file.write(
                            dumps(
                                uhash
                            )
                        )  # 保存
                        file.close()  # 关闭
                        file = open(
                            "usertypes.json",
                            "w+",
                            encoding="utf-8",
                        )  # 打开文件（保存配置）
                        file.write(
                            dumps(
                                utype
                            )
                        )  # 保存
                        file.close()  # 关闭
                        file = open(
                            "joinmsgs.json",
                            "w+",
                            encoding="utf-8",
                        )  # 打开文件（保存配置）
                        file.write(
                            dumps(
                                joinmsg
                            )
                        )  # 保存
                        file.close()  # 关闭
                        file = open(
                            "advusrs.txt",
                            "w+",
                            encoding="utf-8",
                        )  # 打开文件（保存配置）
                        file.write(
                            "\n".join(
                                advusr
                            )
                        )  # 保存
                        file.close()  # 关闭
                        send(
                            "配置保存成功"
                        )
                    elif (
                        command
                        == "&addadvusr"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            advusr.append(
                                parm
                            )
                            send(
                                f"成功升级{parm}的权限"
                            )
                    elif (
                        command
                        == "&deladvusr"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                not in advusr
                            ):
                                send(
                                    f"{parm}的权限已经是最低级"
                                )
                            else:
                                advusr = removeArrayItem(
                                    advusr,
                                    parm,
                                )
                                send(
                                    f"成功降级{parm}的权限"
                                )
                    elif (
                        command
                        == "&update"
                    ):
                        send(
                            "# 当前版本: 10.4.5312.1827 P1I1G3 \r\n # 已经是最新版本 \r\n # zhueBot is created by zhue001 (Python Edition)"
                        )
                    elif (
                        command
                        == "&setrandmax"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`max`"
                            )
                        else:
                            randommax = int(
                                parm
                            )
                            send(
                                f"随机数最大值已设置为{parm}"
                            )
                    elif (
                        command
                        == "&setrandmin"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`min`"
                            )
                        else:
                            randommin = int(
                                parm
                            )
                            send(
                                f"随机数最小值已设置为{parm}"
                            )
                    elif (
                        command
                        == "&newanimal"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`animal`"
                            )
                        else:
                            animalsounds.append(
                                {
                                    "text": parm,
                                    "img": "0.png",
                                }
                            )
                            send(
                                "动物创建完成"
                            )
                    elif (
                        command
                        == "&newanimalwithimg"
                    ):
                        parm = (
                            parm.split()
                        )
                        try:
                            if (
                                parm[
                                    0
                                ]
                                == ""
                            ):
                                send(
                                    "缺失参数`animal`"
                                )
                        except:
                            send(
                                "缺失参数`animal` and `img`"
                            )
                        try:
                            if (
                                parm[
                                    1
                                ]
                                == ""
                            ):
                                send(
                                    "缺失参数`img`"
                                )
                            else:
                                animalsounds.append(
                                    {
                                        "text": parm[
                                            0
                                        ],
                                        "img": parm[
                                            1
                                        ],
                                    }
                                )
                                send(
                                    "动物创建完成"
                                )
                        except:
                            send(
                                "缺失参数`img`"
                            )
                if (
                    perm
                    >= 2
                ):  # 高级用户、系统管理员才能执行的权限
                    if (
                        command
                        == "&help"
                    ):
                        w(
                            u,
                            """
        您的用户组: 高级用户
        可用指令：
        `&help`:获得帮助
        `&addyxc`:添加优秀词
        `&delyxc`:删除优秀词
        `&ping`:获取bot到服务器延迟
        `&allmsglog`:获取最近100条消息
        `&daming`:获取时间
        `&pbclist`:屏蔽词列表
        `&setjoinmsg`:设置欢迎语
        `&getusrtype`:获取某用户类型
        `&getusrhash`:获取某用户hash
        `&bans`:封禁列表
        `&ban`:封禁用户
        `&unban`:解封用户
        `&addwhitelist`:添加白名单
        `&delwhitelist`:删除白名单
        `&kick`:踢出用户
        `&kill`:击杀用户
        `&privatemode`:私有模式
        `&publicmode`:公众模式
        `&setmml`:设置最大消息长度
        `&addpbc`:添加屏蔽词
        `&delpbc`:删除屏蔽词
        `&gn`:猜数字
        `&calc`:计算器
        `&reset`:重置
        `&girl`:看辣妹
        `&animal`:随机动物叫声
        `&rand`:随机数
        `&warning`:警告用户
        `&afk`:挂机
        `&randomimg`:获取随机美女图片
        `&rgb2hex`:RGB颜色转HAX
        `&hax2rgb`:HEX颜色转RGB
        `&getpubyhash`:通过hash获取与他IP相同的用户
        `&mybuddha`:查看自己是什么佛
        `&buddhas`:查看佛列表
        `&setjcb`:设置佛位继承者
        `&niepan`:涅磐成佛
        `&yuanji`:圆寂自杀
        `&forceyj`:强制一个用户圆寂
        `&sendnotice`:发送公告
        `&idiomsolitaire`:成语接龙
                        """,
                        )
                        continue
                    elif (
                        command
                        == "&sendnotice"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`notice`"
                            )
                        else:
                            lastNotice = f"公告: {parm} (创建者: {u})"
                            send(
                                "公告设置成功，将在报时时显示"
                            )
                    elif (
                        command
                        == "&forceyj"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                not in buddhas
                            ):
                                send(
                                    "该用户还不是佛"
                                )
                            elif (
                                buddhas[
                                    parm
                                ][
                                    "jicheng"
                                ]
                                == False
                            ):
                                send(
                                    "该用户尚未设置继承佛"
                                )
                            else:
                                buddhas[
                                    parm
                                ][
                                    "jichengstatus"
                                ] = 2
                                send(
                                    "成功强制该用户圆寂"
                                )
                                w(
                                    buddhas[
                                        parm
                                    ][
                                        "jicheng"
                                    ],
                                    f"{parm}圆寂了，您作为他的继承佛，可以使用`&niepan`涅磐成佛",
                                )
                    elif (
                        command
                        == "&setmml"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`mml`"
                            )
                        else:
                            try:
                                mml = int(
                                    parm
                                )
                                send(
                                    f"最大消息长度成功设置为{parm}"
                                )
                            except:
                                send(
                                    "参数无效"
                                )
                    elif (
                        command
                        == "&ban"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                in bans
                            ):
                                send(
                                    "此人已经被阻止访问"
                                )
                            else:
                                bans.append(
                                    parm
                                )
                                send(
                                    f"成功阻止访问{parm}"
                                )
                                ws.send(
                                    {
                                        "cmd": "kick",
                                        "nick": parm,
                                    }
                                )
                    elif (
                        command
                        == "&addwhitelist"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            whitelist.append(
                                parm
                            )
                            send(
                                "成功将此人加入白名单"
                            )
                    elif (
                        command
                        == "&delwhitelist"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                not in whitelist
                            ):
                                send(
                                    "此人不在白名单中"
                                )
                            else:
                                whitelist = removeArrayItem(
                                    whitelist,
                                    parm,
                                )
                                send(
                                    f"成功删除白名单用户{parm}"
                                )
                    elif (
                        command
                        == "&unban"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            if (
                                parm
                                not in bans
                            ):
                                send(
                                    "此人没有被阻止访问"
                                )
                            else:
                                bans = removeArrayItem(
                                    bans,
                                    parm,
                                )
                                send(
                                    f"成功取消阻止访问{parm}"
                                )
                    elif (
                        command
                        == "&kick"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            ws.send(
                                dumps(
                                    {
                                        "cmd": "kick",
                                        "nick": parm,
                                    }
                                )
                            )
                            send(
                                f"系统已踢出用户{parm}！"
                            )
                    elif (
                        command
                        == "&kill"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            ws.send(
                                dumps(
                                    {
                                        "cmd": "disconnect",
                                        "nick": parm,
                                    }
                                )
                            )
                            send(
                                f"系统已击杀用户{parm}！"
                            )
                    elif (
                        command
                        == "&privatemode"
                    ):
                        privatemode = True
                        send(
                            "已经设为私有模式"
                        )
                    elif (
                        command
                        == "&publicmode"
                    ):
                        privatemode = False
                        send(
                            "已经设为公众模式"
                        )
                    elif (
                        command
                        == "&addpbc"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`word`"
                            )
                        else:
                            if (
                                parm
                                in badword
                            ):
                                send(
                                    "它已经是屏蔽词了"
                                )
                            else:
                                badword.append(
                                    parm
                                )
                                send(
                                    "成功将它设为屏蔽词"
                                )
                    elif (
                        command
                        == "&delpbc"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`word`"
                            )
                        else:
                            if (
                                parm
                                not in badword
                            ):
                                send(
                                    "它还不是屏蔽词"
                                )
                            else:
                                badword = removeArrayItem(
                                    badword,
                                    parm,
                                )
                                send(
                                    f"成功删除屏蔽词{parm}"
                                )
                    elif (
                        command
                        == "&addyxc"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`word`"
                            )
                        else:
                            goodword.append(
                                parm
                            )
                            send(
                                f"添加优秀词{parm}成功"
                            )
                    elif (
                        command
                        == "&delyxc"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`word`"
                            )
                        else:
                            if (
                                parm
                                not in goodword
                            ):
                                send(
                                    f"{parm}还不是优秀词"
                                )
                            else:
                                goodword = removeArrayItem(
                                    goodword,
                                    parm,
                                )
                                send(
                                    f"{parm}不再是优秀词了"
                                )
                    elif (
                        command
                        == "&reset"
                    ):
                        needconfirm = 1
                        confirmer = u
                        confirmflag = 1
                        w(
                            u,
                            "使用`&confirm`确认重置",
                        )
                    elif (
                        command
                        == "&confirm"
                    ):
                        if (
                            needconfirm
                            == 1
                        ):
                            if (
                                u
                                == confirmer
                            ):
                                if (
                                    confirmflag
                                    == 1
                                ):
                                    ws.close()
                                    ws = connect(
                                        SERVER
                                        + "/chat-ws/"
                                        + CHANNEL
                                    )
                                    ws.send(
                                        dumps(
                                            {
                                                "cmd": "join",
                                                "channel": CHANNEL,
                                                "nick": botNick,
                                                "head": None,
                                            }
                                        )
                                    )
                                    needconfirm = 0
                                    confirmer = "Radium"
                                    confirmflag = 0
                    elif (
                        command
                        == "&warning"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            warns[
                                warnindex
                            ] = parm
                            warnindex += 1
                            if (
                                warnindex
                                == 3
                            ):
                                warnindex = 0
                            send(
                                f"@{parm} 警告，不要继续违规行为"
                            )
                if (
                    perm
                    >= 1
                ):  # 限制用户、高级用户、系统管理员才能执行的权限
                    if (
                        command
                        == "&help"
                    ):
                        w(
                            u,
                            """
        您的用户组: 限制用户
        可用指令：
        `&help`:获得帮助
        `&ping`:获取bot到服务器延迟
        `&allmsglog`:获取最近100条消息
        `&daming`:获取时间
        `&pbclist`:屏蔽词列表
        `&setjoinmsg`:设置欢迎语
        `&getusrtype`:获取某用户类型
        `&getusrhash`:获取某用户hash
        `&bans`:封禁列表
        `&gn`:猜数字
        `&calc`:计算器
        `&girl`:看辣妹
        `&animal`:随机动物叫声
        `&rand`:随机数
        `&afk`:挂机
        `&randomimg`:获取随机美女图片
        `&rgb2hex`:RGB颜色转HAX
        `&hax2rgb`:HEX颜色转RGB
        `&getpubyhash`:通过hash获取与他IP相同的用户
        `&mybuddha`:查看自己是什么佛
        `&buddhas`:查看佛列表
        `&setjcb`:设置佛位继承者
        `&niepan`:涅磐成佛
        `&yuanji`:圆寂自杀
        `&idiomsolitaire`:成语接龙
                        """,
                        )
                        continue
                    elif (
                        command
                        == "&ping"
                    ):
                        ping_value = str(
                            randint(
                                10453121827,
                                104531218270,
                            )
                        )
                        ping_request_time = s
                        send(
                            f"&ping {ping_value}"
                        )
                    elif (
                        command
                        == "&allmsglog"
                    ):
                        w(
                            u,
                            "\r\n".join(
                                allmsglog
                            ),
                        )
                    elif (
                        command
                        == "&daming"
                    ):
                        if (
                            parm
                            == "full"
                        ):
                            send(
                                f"当前时间：{datetime.now().strftime('%H:%M:%S')}"
                            )
                        else:
                            send(
                                f"嗷嗷！现在已经{datetime.now().strftime('%H')}点了，要想获取精确时间，请使用`&daming full`"
                            )
                    elif (
                        command
                        == "&pbclist"
                    ):
                        send(
                            str(
                                badword
                            )
                        )
                    elif (
                        command
                        == "&setjoinmsg"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`joinmsg`"
                            )
                        else:
                            joinmsg[
                                u
                            ] = parm
                            send(
                                f"你的欢迎语已被设为{parm}"
                            )
                    elif (
                        command
                        == "&getusrtype"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            try:
                                send(
                                    utype[
                                        parm
                                    ]
                                )
                            except:
                                send(
                                    "抱歉，暂未收录此用户"
                                )
                    elif (
                        command
                        == "&getusrhash"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`user`"
                            )
                        else:
                            try:
                                send(
                                    uhash[
                                        parm
                                    ]
                                )
                            except:
                                send(
                                    "抱歉，暂未收录此用户"
                                )
                    elif (
                        command
                        == "&bans"
                    ):
                        send(
                            str(
                                bans
                            )
                        )
                    elif (
                        command
                        == "&gn"
                    ):
                        gameflag = 1
                        gnrandom = randint(
                            1,
                            1000,
                        )
                        send(
                            "我已经准备好了一个1到1000的数字，快用&guess <一个数字>猜测吧！"
                        )
                    elif (
                        command
                        == "&guess"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`num`"
                            )
                        else:
                            if (
                                gameflag
                                == 1
                            ):
                                try:
                                    guessed = int(
                                        parm
                                    )
                                    if (
                                        guessed
                                        > gnrandom
                                    ):
                                        w(
                                            u,
                                            "猜的太大了点儿",
                                        )
                                    elif (
                                        guessed
                                        < gnrandom
                                    ):
                                        w(
                                            u,
                                            "猜的太小了点儿",
                                        )
                                    else:
                                        w(
                                            u,
                                            "你赢啦！恭喜你！",
                                        )
                                        gameflag = 0
                                except:
                                    send(
                                        "参数无效"
                                    )
                            else:
                                send(
                                    "游戏还没开始呢"
                                )
                    elif (
                        command
                        == "&girl"
                    ):
                        send(
                            choice(
                                girls
                            )
                        )
                    elif (
                        command
                        == "&animal"
                    ):
                        randomanimal = choice(
                            animalsounds
                        )
                        if (
                            randomanimal[
                                "img"
                            ]
                            == None
                        ):
                            send(
                                randomanimal[
                                    "text"
                                ]
                            )
                        else:
                            send(
                                f"![{randomanimal['text']}.png]({randomanimal['img']})"
                            )
                    elif (
                        command
                        == "&rand"
                    ):
                        send(
                            str(
                                randint(
                                    randommin,
                                    randommax,
                                )
                            )
                        )
                    elif (
                        command
                        == "&afk"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            afks.append(
                                {
                                    "user": u,
                                    "reason": "Undefined",
                                }
                            )
                        else:
                            afks.append(
                                {
                                    "user": u,
                                    "reason": parm,
                                }
                            )
                        send(
                            f"@{u} 你已经设为挂机状态了，去{choice(afkactions)}吧"
                        )
                    elif (
                        command
                        == "&randomimg"
                    ):
                        send(
                            f"![]({choice(imgs)})"
                        )
                    elif (
                        command
                        == "&rgb2hex"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`rgb`"
                            )
                        else:
                            try:
                                send(
                                    RgbToHex(
                                        parm
                                    )
                                )
                            except:
                                send(
                                    "参数无效"
                                )
                    elif (
                        command
                        == "&hex2rgb"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`hex`"
                            )
                        else:
                            try:
                                send(
                                    HexToRgb(
                                        parm
                                    )
                                )
                            except:
                                send(
                                    "参数无效"
                                )
                    elif (
                        command
                        == "&getpubyhash"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`hash`"
                            )
                        else:
                            send(
                                str(
                                    findKey(
                                        uhash,
                                        parm,
                                    )
                                )
                            )
                    elif (
                        command
                        == "&mybuddha"
                    ):
                        if (
                            u
                            in buddhas
                        ):
                            send(
                                buddhas[
                                    u
                                ][
                                    "name"
                                ]
                            )
                        else:
                            send(
                                "您还没有成佛"
                            )
                    elif (
                        command
                        == "&buddhas"
                    ):
                        buddhaDetail = (
                            []
                        )

                        for (
                            key,
                            value,
                        ) in (
                            buddhas.items()
                        ):
                            name = value[
                                "name"
                            ]
                            jicheng = (
                                value[
                                    "jicheng"
                                ]
                                if value[
                                    "jicheng"
                                ]
                                else "未设置"
                            )

                            detail = f"{key}: {name} (继承人: {jicheng})"
                            buddhaDetail.append(
                                detail
                            )

                        send(
                            "\r\n".join(
                                buddhaDetail
                            )
                        )
                    elif (
                        command
                        == "&setjcb"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`jcb`"
                            )
                        else:
                            if (
                                u
                                not in buddhas
                            ):
                                send(
                                    "你还不是佛"
                                )
                            elif (
                                buddhas[
                                    u
                                ][
                                    "jicheng"
                                ]
                                != False
                            ):
                                send(
                                    "你已经设置过继承佛了"
                                )
                            elif (
                                parm
                                in buddhas
                            ):
                                send(
                                    "他已经成佛了"
                                )
                            else:
                                buddhas[
                                    u
                                ][
                                    "jicheng"
                                ] = parm
                                buddhas[
                                    u
                                ][
                                    "jichengstatus"
                                ] = 1
                                if (
                                    isJiChengSame()
                                ):
                                    send(
                                        "抱歉，已经有其他佛设置此人为继承佛了"
                                    )
                                    buddhas[
                                        u
                                    ][
                                        "jicheng"
                                    ] = False
                                    buddhas[
                                        u
                                    ][
                                        "jichengstatus"
                                    ] = 0
                                else:
                                    send(
                                        "设置成功，您圆寂后对方即可涅磐"
                                    )
                    elif (
                        command
                        == "&yuanji"
                    ):
                        if (
                            u
                            not in buddhas
                        ):
                            send(
                                "你还不是佛"
                            )
                        elif (
                            buddhas[
                                u
                            ][
                                "jicheng"
                            ]
                            == False
                        ):
                            send(
                                "请先设置继承佛"
                            )
                        else:
                            buddhas[
                                u
                            ][
                                "jichengstatus"
                            ] = 2
                            send(
                                "圆寂成功"
                            )
                            w(
                                buddhas[
                                    u
                                ][
                                    "jicheng"
                                ],
                                f"{u}圆寂了，您作为他的继承佛，可以使用`&niepan`涅磐成佛",
                            )
                    elif (
                        command
                        == "&calc"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`expression`"
                            )
                        else:
                            send(
                                str(
                                    calculate(
                                        parm
                                    )
                                )
                            )
                    elif (
                        command
                        == "&niepan"
                    ):
                        if WhoIsbjcb(
                            u
                        ):
                            buddhas[
                                u
                            ] = {
                                "name": buddhas[
                                    WhoIsbjcb(
                                        u
                                    )
                                ][
                                    "name"
                                ],
                                "jicheng": False,
                                "jichengstatus": 0,
                            }
                            buddhas = removeDictItem(
                                buddhas,
                                WhoIsbjcb(
                                    u
                                ),
                            )
                            send(
                                "您涅盘了"
                            )
                        else:
                            send(
                                "还没有人设置你为继承佛"
                            )
                    elif (
                        command
                        == "&idiomsolitaire"
                    ):
                        if (
                            idiomsolitaire
                            == True
                            or idiomsolitaire
                            == "playing"
                        ):
                            send(
                                "游戏已经存在"
                            )
                        else:
                            idiomsolitaire = True
                            idiomsol_timeout = (
                                int(
                                    datetime.now().timestamp()
                                )
                                + 180
                            )
                            idiomsol_players = [
                                u
                            ]
                            send(
                                "已经创建成语接龙游戏，使用`&joinidiom`加入，使用`&leaveidiom`退出，使用`&startidiom`开始，使用`&updateidiomdb`更新成语列表"
                            )
                    elif (
                        command
                        == "&joinidiom"
                    ):
                        if (
                            idiomsolitaire
                            == False
                        ):
                            send(
                                "游戏还未创建"
                            )
                        else:
                            if (
                                idiomsolitaire
                                == "playing"
                            ):
                                send(
                                    "游戏已经开始"
                                )
                            else:
                                if (
                                    u
                                    in idiomsol_players
                                ):
                                    send(
                                        "你已经加入游戏了！"
                                    )
                                else:
                                    idiomsol_players.append(
                                        u
                                    )
                                    send(
                                        "成功加入游戏"
                                    )
                    elif (
                        command
                        == "&leaveidiom"
                    ):
                        if (
                            idiomsolitaire
                            == False
                        ):
                            send(
                                "游戏还未创建"
                            )
                        else:
                            if (
                                idiomsolitaire
                                == "playing"
                            ):
                                send(
                                    "游戏已经开始"
                                )
                            else:
                                if (
                                    u
                                    not in idiomsol_players
                                ):
                                    send(
                                        "你根本没有加入"
                                    )
                                else:
                                    idiomsol_players = removeArrayItem(
                                        idiomsol_players,
                                        u,
                                    )
                                    send(
                                        "成功离开游戏"
                                    )
                    elif (
                        command
                        == "&updateidiomdb"
                    ):
                        oldLength = len(
                            idiom
                        )
                        idiomfile = open(
                            "idiom.txt",
                            "r",
                            encoding="utf-8",
                        )
                        idiom = idiomfile.read().split(
                            "\n"
                        )
                        idiomfile.close()
                        newLength = len(
                            idiom
                        )
                        send(
                            f"更新成功，原有{str(oldLength)}个，现有{str(newLength)}个"
                        )
                    elif (
                        command
                        == "&startidiom"
                    ):
                        if (
                            idiomsolitaire
                            == False
                        ):
                            send(
                                "游戏还未创建"
                            )
                        else:
                            if (
                                idiomsolitaire
                                == "playing"
                            ):
                                send(
                                    "游戏已经开始"
                                )
                            else:
                                if (
                                    len(
                                        idiomsol_players
                                    )
                                    > 2
                                ):
                                    idiomsolitaire = "playing"
                                    currentWord = choice(
                                        idiom
                                    )
                                    currentPlayer = idiomsol_players[
                                        0
                                    ]
                                    playerIndex = 1
                                    idiomsol_timeout = (
                                        datetime.now().timestamp()
                                        + 1800
                                    )
                                    send(
                                        f"游戏已经开始！现在请通过`&idiom`接龙，第一个词语是，{currentWord}，现在轮到{currentPlayer}接龙"
                                    )
                                else:
                                    send(
                                        "人数不足"
                                    )
                    elif (
                        command
                        == "&idiom"
                    ):
                        if (
                            parm
                            == ""
                        ):
                            send(
                                "缺失参数`idiom`"
                            )
                        else:
                            if (
                                idiomsolitaire
                                != "playing"
                            ):
                                send(
                                    "游戏还未开始"
                                )
                            else:
                                if (
                                    parm
                                    not in idiom
                                ):
                                    send(
                                        "输入不是成语"
                                    )
                                else:
                                    if (
                                        parm[
                                            0
                                        ]
                                        != currentWord[
                                            len(
                                                currentWord
                                            )
                                            - 1
                                        ]
                                    ):
                                        send(
                                            "首尾没有对应"
                                        )
                                    else:
                                        currentWord = parm
                                        currentPlayer = idiomsol_players[
                                            playerIndex
                                        ]
                                        send(
                                            f"现在的词语是，{currentWord}，现在轮到{currentPlayer}接龙"
                                        )
                                        playerIndex = (
                                            playerIndex
                                            + 1
                                        )
                                        if (
                                            playerIndex
                                            == len(
                                                idiomsol_players
                                            )
                                        ):
                                            playerIndex = 0
        if (
            idiomsolitaire
            == True
            and idiomsol_timeout
            - int(
                datetime.now().timestamp()
            )
            < 0
        ):
            idiomsolitaire = False
            send(
                "成语接龙已超时，请重新创建"
            )
        if (
            data[
                "cmd"
            ]
            == "warn"
            and debug
        ):
            print(
                data
            )  # debug
    except Exception as err:
        send(
            f"系统错误: `{err}`"
        )

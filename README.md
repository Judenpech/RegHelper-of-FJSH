# 福建省口腔医院/福建医科大学附属口腔医院挂号助手

## 免责声明

用户应仔细阅读此声明，默认用户已了解并接受此声明：

1. 用户需遵守《中华人民共和国网络安全法》；
2. 本项目代码仅供学习、科研使用，切勿用于商业行为及其他任何用途；
3. 因使用本项目造成的任何意外以及损失，作者不负任何责任；
4. 任何修改后所发布的代码文件与作者无关；
5. 请于24小时之内删除与本项目相关的一切内容，出现问题作者概不负责。

以上若触犯了贵公司的权益，请与作者联系（issue），我们会尽快停止使用！

## 功能

一般情况下，GoGuaHao.py就足够使用了，除非碰上**选择排班**页面显示**马上预约**，但实际就诊信息页面显示**暂无号源**的情况，使用GoGuaHaoPro.py。

#### GoGuaHao.py

- 自动刷新**选择排班**页面
- 当显示**马上预约**时，发送邮件至用户指定的邮箱提醒用户挂号

![](https://github.com/Judenpech/RegHelper-of-FJSH/blob/main/images/book.png)

#### GoGuaHaoPro.py

- 自动刷新**就诊信息**页面
- 当**预约号源**不为0时，发送邮件至用户指定的邮箱提醒用户挂号

![](https://github.com/Judenpech/RegHelper-of-FJSH/blob/main/images/num.png)

## 配置

### Requirements

```python
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
import datetime as dt
import time
```

### GoGuaHao.py

简单修改以下信息即可。

```python
# 医生信息
docName = '黄晓晶'
# 选择排班页面url
url = 'http://fjkqyy.yihugz..' 

# 邮件信息
msg_from = '123456789@qq.com'  # 发送方邮箱
passwd = 'asdfghjklzxcvbnm'  # 发送方邮箱的授权码
msg_to = '987654321@qq.com'  # 收件人邮箱
```

### GoGuaHaoPro.py

简单修改以下信息即可。

```python
# 医生信息
docName = '黄晓晶'
# 就诊时间
reg_time = '2020-11-18'
# 就诊信息页面url
url = 'http://fjkqyy.yihugz..'

# 邮件信息
msg_from = '123456789@qq.com'  # 发送方邮箱
passwd = 'asdfghjklzxcvbnm'  # 发送方邮箱的授权码
msg_to = '987654321@qq.com'  # 收件人邮箱
```

## 运行

- `python GoGuaHao.py`
- `python GoGuaHaoPro.py`


from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
import datetime as dt
import time

# 医生信息
docName = '黄晓晶'
# 选择排班页面url
url = 'http://fjkqyy.yihugz.com/Hos-WeiXin/business/yygh/yygh_schedule_list.html?docCode=086591000A1000000001&deptCode=086591000A1980000010&deptName=%u7259%u4F53%u7259%u9AD3%u4E00%u79D1&datetext='


def sendEmail():
    msg_from = '123456789@qq.com'  # 发送方邮箱
    passwd = 'asdfghjklzxcvbnm'  # 发送方邮箱的授权码
    msg_to = '987654321@qq.com'  # 收件人邮箱

    subject = "挂号提醒"  # 邮件主题
    content = '你关注的' + docName + '医生已放号，快去挂号！\n' + url  # 邮件正文

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    flag = 0
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("#### 邮件发送成功 ", dt.datetime.now().strftime('%F %T'), '####')
        flag = 1
    except:
        print("#### 邮件发送失败 ", dt.datetime.now().strftime('%F %T'), '####')
    finally:
        s.quit()
        return flag


def main():
    global driver
    driver = webdriver.Edge('..\edgedriver_win64\msedgedriver.exe')
    driver.set_window_size(480, 400)

    driver.get(url)

    def isElementExist():
        flag = True
        try:
            driver.find_element_by_link_text('马上预约')
            return flag
        except:
            flag = False
            return flag

    while 1:
        if isElementExist():
            print('#### 可预约 ', dt.datetime.now().strftime('%F %T'), '####')
            while 1:
                flag = sendEmail()
                if flag:
                    break
            if flag:
                break

        time.sleep(30)  # 刷新频率(秒)
        driver.refresh()
        print('刷新页面 ', dt.datetime.now().strftime('%F %T'))
    driver.quit()
    print('#### 退出挂号助手 ####')


if __name__ == "__main__":
    main()

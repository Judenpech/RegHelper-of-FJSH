from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
import datetime as dt
import time

# 医生信息
docName = '张三'
# 就诊时间
reg_time = '2020-11-18'
# 就诊信息页面url
url = 'http://fjkqyy.yihugz.com/Hos-WeiXin/business/yygh/yygh_clinic_msg.html?deptname=%E7%89%99%E4%BD%93%E7%89%99%E9%AB%93%E4%B8%80%E7%A7%91&remark=%E7%89%99%E4%BD%93%E7%89%99%E9%AB%93%E7%97%85%E7%9A%84%E8%AF%8A%E6%B2%BB%E3%80%81%E5%8F%A3%E8%85%94%E6%BF%80%E5%85%89%E5%BA%94%E7%94%A8&doctorname=%E7%8E%8B%E7%87%95%E7%85%8C&registrationfee=30&scheduleid=415A14D548ED4954AE25692F3ED0AFCA&registerdate=' + reg_time + '%2000:00:00&timeid=2&deptCode=086591000A1980000010&doctorCode=086591000A1000000511'


def sendEmail():
    msg_from = '123456789@qq.com'  # 发送方邮箱
    passwd = 'asdfghjklzxcvbnm'  # 发送方邮箱的授权码
    msg_to = '987654321@qq.com'  # 收件人邮箱

    subject = "挂号提醒"  # 邮件主题
    content = '你关注的' + docName + '医生已放号，快去挂号！' + url  # 邮件正文

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

    driver.find_element_by_xpath('//*[@id="pophtml"]/div[3]/label').click()
    driver.find_element_by_link_text('确认').click()

    jiuZhenRen = driver.find_element_by_xpath('//*[@id="default"]/ul/li[1]/span')
    driver.execute_script("arguments[0].innerText = '12345'", jiuZhenRen)

    def get_lis_len():
        try:
            time.sleep(15)
            driver.find_element_by_xpath('//*[@id="default"]/ul/li[2]').click()
            time.sleep(15)

            ul = driver.find_element_by_xpath('//*[@id="numlist"]')
            lis = ul.find_elements_by_tag_name('li')

            return len(lis)
        except:
            print('出现错误，重试中...')
            return -1

    while 1:
        lis_len = get_lis_len()
        print(dt.datetime.now().strftime('%F %T'))
        print('号数: ', lis_len, '\n')
        if lis_len > 0:
            print('#### 可预约 ', dt.datetime.now().strftime('%F %T'), '####')
            while 1:
                flag = sendEmail()
                if flag:
                    break

            break

        try:
            driver.find_element_by_xpath('/html/body/div[2]/span/i').click()
        except:
            print('出现错误，重试中...')
            continue

    driver.quit()
    print('#### 退出挂号助手 ####')


if __name__ == "__main__":
    main()

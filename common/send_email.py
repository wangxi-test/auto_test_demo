import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

con=smtplib.SMTP_SSL('smtp.163.com','465')
con.login(user='test_wangxi@163.com',password='NNAMSQXVGUWBTUGP')
sender='test_wangxi@163.com'
recevier=['302858210@qq.com','test_wangxi@163.com']

# 发送附件
# 创建信封
message = MIMEMultipart()
# 读取附件内容
image=open('../log/u=3540254304,2721513969&fm=26&fmt=auto.webp','rb').read()
# 将附件读取的内容写入到信封本文中
image_data = MIMEImage(image)
# 信封取个名字
image_data['Content-Disposition']='attachment;filename="picture.webp"'
# 将信封内容加载到邮箱发送器中
message.attach(image_data)


# 设置邮件头部信息
message['From']=Header('wangxi302858210@qq.com','utf-8')
message['To']=Header('收件人')
message['Subject']=Header('这是一封邮件')
# 发送邮件
con.sendmail(sender,recevier,message.as_string())



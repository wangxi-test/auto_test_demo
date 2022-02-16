import logging

# 方式一
# log_format = "%(levelname)s %(pathname)s %(module)s line:%(lineno)d %(message)s"
# logging.basicConfig(level=logging.DEBUG,format=log_format,filename='../log/run.log')
#
# logging.debug('这是debug日志')
# logging.info('这是info日志')
# logging.warning('这是warning日志')
# logging.error('这是error日志')
# logging.critical('这是critical日志')

# 方式二
# # 创建日志器
# logger=logging.getLogger('logger')
# # 设置日志级别
# logger.setLevel(logging.DEBUG)
# # 创建格式器
# log_format = "%(levelname)s %(pathname)s %(module)s line:%(lineno)d"
# formater = logging.Formatter(fmt=log_format)
# # 创建一个处理器，输出到指定文件
# fh=logging.FileHandler('../log/run.log',encoding='utf-8')
# # 创建一个处理器，输出到控制台
# sh=logging.StreamHandler()
# # 把控制台加载到日志其中
# logger.addHandler(sh)
# # 把文件加载到日志器中
# logger.addHandler(fh)
# # 把格式器放入控制台
# sh.setFormatter(formater)
# # 把格式器放入文件
# fh.setFormatter(formater)
#
# logger.debug('这是debug日志')
# logger.info('这是info日志')
# logger.warning('这是warning日志')
# logger.error('这是error日志')
# logger.critical('这是critical日志')




class DemoLog:
    def log_alarm(self):
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        log_format = "%(levelname)s %(pathname)s %(module)s line:%(lineno)d"
        formater = logging.Formatter(fmt=log_format)
        fh = logging.FileHandler('../log/run.log', encoding='utf-8')
        sh = logging.StreamHandler()
        logger.addHandler(sh)
        logger.addHandler(fh)
        sh.setFormatter(formater)
        fh.setFormatter(formater)
        return logger

    def test(self, a, b):
        try:
            sum = a + b
            return sum
        except Exception:
            self.log_alarm().error('计算错误{}+{}'.format(a, b))

if __name__ == '__main__':
    DemoLog().test('a', 2)
# logging模块
# 介绍
# logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等

# **消息等级**
# logging中可以选择很多消息级别，如debug、info、warning、error以及critical。通过赋予logger或者handler不同的级别，开发者就可以只输出错误信息到特定的记录文件，或者在调试时只记录调试信息。
# 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# **基本例子**
"""
import logging
import os.path
import time
logging.basicConfig(level=logging.NOTSET, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug(u"如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s:%(message)s')
# logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
# 默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了

"""

# **输出到文件**、终端
# 输入到文件

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")


# 输入到文件和终端
"""
import logging

logger = logging.getLogger(__name__)        # 实例化
logger.setLevel(level=logging.DEBUG)      # 设置日志级别，大于等于这个级别的信息才会输出
handler = logging.FileHandler("Beautiful Day.txt")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Good morning")
logger.debug("Good afternoon")
logger.warning("Good afternoon")
logger.info("Good evening ")
"""

# 加载配置
# 通过JSON加载配置文件，然后通过logging.dictConfig配置logging
"""
import json
import logging.config
import os

def setup_logging(default_path = "logging.json", default_level = logging.INFO, env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def func():
    logging.info("start func")

    logging.info("exec func")

    logging.info("end func")

if __name__ == "__main__":
    setup_logging(default_path="logging.json")
    func()
"""

# 通过YAML加载配置文件，然后通过logging.dictConfig配置logging
"""
import yaml
import logging.config
import os

def setup_logging(default_path = "logging.yaml",default_level = logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def func():
    logging.info("start func")

    logging.info("exec func")

    logging.info("end func")

if __name__  ==  "__main__":
    setup_logging(default_path="logging.yaml")
    func()
"""

# （了解）回滚、过期删除
"""
import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def backroll():
    # 日志打印格式
    log_fmt = '%(asctime)s/tFile /"%(filename)s/",line %(lineno)s/t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)
    # 创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename="ds_update", when="M", interval=2, backupCount=2)
    # log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.addHandler(log_file_handler)
    # 循环打印日志
    log_content = "test log"
    count = 0
    while count < 30:
        log.error(log_content)
        time.sleep(20)
        count = count + 1
    log.removeHandler(log_file_handler)


if __name__ == "__main__":
    backroll()
"""
# 收集日志，整理、数据可视化
"""
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
try:
    open("sklearn.txt", "rb")
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)

logger.info("Finish")

"""

# 看不懂请参考网页
"""
https://www.cnblogs.com/liujiacai/p/7804848.html
https://www.cnblogs.com/CJOKER/p/8295272.html
"""

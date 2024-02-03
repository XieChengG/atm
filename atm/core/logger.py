import logging

from conf import settings


def logger(log_type):
    """
    打印日志
    :param log_type:
    :return:
    """

    # 创建一个logger日志记录器
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 创建stream handler处理器
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # 创建file handler处理器
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # 创建一个格式化器 formatter
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # 添加formatter到handler
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把handler添加到logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

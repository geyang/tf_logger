from .tf_logger import TF_Logger, Color, percent


def test():
    d = Color(3.1415926, 'red')
    s = "{:.1}".format(d)
    print(s)

    TEST_LOG_DIR = '/tmp/tf_logger/test'

    logger = TF_Logger(TEST_LOG_DIR)
    logger.log(0, some=Color(0.1, 'yellow'))
    logger.log(1, some=Color(0.28571, 'yellow', lambda v: f"{v * 100:.5f}%"))
    logger.log(2, some=Color(0.85, 'yellow', percent))
    logger.log(3, {"some_var/smooth": 10}, some=Color(0.85, 'yellow', percent))
    logger.log(4, some=Color(10, 'yellow'))

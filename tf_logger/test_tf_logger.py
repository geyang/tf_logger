from tf_logger import TF_Logger, Color, percent

TEST_LOG_DIR = '/tmp/tf_logger/test'
logger = TF_Logger(TEST_LOG_DIR)

print(f"logging to {TEST_LOG_DIR}")


def test():
    d = Color(3.1415926, 'red')
    s = "{:.1}".format(d)
    print(s)

    logger.log_params(G=dict(some_config="hey"))
    logger.log(0, some=Color(0.1, 'yellow'))
    logger.log(1, some=Color(0.28571, 'yellow', lambda v: f"{v * 100:.5f}%"))
    logger.log(2, some=Color(0.85, 'yellow', percent))
    logger.log(3, {"some_var/smooth": 10}, some=Color(0.85, 'yellow', percent))
    logger.log(4, some=Color(10, 'yellow'))


def test_image():
    import scipy.misc
    import numpy as np

    image_bw = np.zeros((64, 64, 1))
    image_bw_2 = scipy.misc.face(gray=True)
    image_rgb = np.zeros((64, 64, 3))
    image_rgba = scipy.misc.face()
    logger.log_image(4, black_white=image_bw)
    logger.log_image(4, bw_face=image_bw_2)
    logger.log_image(4, rgb=image_rgb)
    logger.log_image(4, rgba_face=image_rgba)


if __name__ == "__main__":
    test()
    test_image()

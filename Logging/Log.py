import logging

logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler('example.log')
file_handler.setLevel(logging.ERROR)

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


logger.debug('This is a debug message')
logger.info('This is a info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')

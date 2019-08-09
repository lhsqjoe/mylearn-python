import logging

# logging.basicConfig(level=log_level,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='parser_result.log',
#                     filemode='w')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my.log',
                    filemode='a')
logging.debug('Hello')

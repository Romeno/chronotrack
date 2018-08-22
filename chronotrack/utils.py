import logging


def init_logger(filename):
    from logging.config import dictConfig

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'f': {
                'format':
                    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'h': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'f',
                'level': 'DEBUG',
                'filename': filename,
                'maxBytes': 1048576,
                'backupCount': 20,
                'encoding': 'utf8'
            }
        },
        'root': {
            'handlers': ['h'],
            'level': logging.INFO,
        },
    }

    dictConfig(logging_config)
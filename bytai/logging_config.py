# import logging.config


# LOGGING_CONFIG = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'formatter': 'verbose'
#         }
#     },
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'bytai': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }

# logging.config.dictConfig(LOGGING_CONFIG)
# import os

# logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'logging_config'))

# # Create a logger object
# logger = logging.getLogger(__name__)

# # Example usage of logger
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')
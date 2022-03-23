from utils.logging_handler import LoggingHandler

logger = LoggingHandler.get_logger('behave-environment')

WAIT = 8

def before_all(context):
    context.config.setup_logging()

def after_all(context):
    pass
from utils.logging_handler import LoggingHandler
from behave import *

logger = LoggingHandler.get_logger('smoke_test')

@given('print start notice {start_notice}')
def step_impl(context, start_notice):
    logger.info('Logger: {}'.format(start_notice))
    print('\nPrint: {}'.format(start_notice))

@then('print preparedness notice {prep_notice}')
def step_impl(context, prep_notice):
    logger.info('Logger: {}'.format(prep_notice))
    print('\nPrint: {}'.format(prep_notice))

@then('print greeting {greeting_notice}')
def step_impl(context, greeting_notice):
    logger.info('Logger: {}\n'.format(greeting_notice))
    print('\nPrint: {}'.format(greeting_notice))

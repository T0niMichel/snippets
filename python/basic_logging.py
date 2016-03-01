"""
basic logging
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.debug('debug msg')
    logger.info('info msg')

#!/usr/env python3.7

import configparser
import logging
import os
import sys
import time

from bs4 import BeautifulSoup

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    while True:
        try:
            time.sleep(0.1)
        
        except Exception as e:
            logger.exception(e)
        
        except KeyboardInterrupt:
            logger.info('Exit signal received.')
            sys.exit()
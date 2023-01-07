import os
import logging

# logs to file
logging.basicConfig(filename='.log', format='%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

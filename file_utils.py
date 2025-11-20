import logzero
from logzero import logger, setup_logger
import math_utils

vel = math_utils.vel

setup_logger()

logger.info('This logger is correctly outputed')

def escrever_resultado(velocidade):
    with open('result.txt','w') as f:
        f.write(str(velocidade))

escrever_resultado(vel)
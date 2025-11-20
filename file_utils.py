import logzero
from logzero import logger

logger.setup.logging()

vel = 7.73


def escrever_resultado(velocidade):
    with open('result.txt','w') as f:
        f.write(str(velocidade))

escrever_resultado(vel)
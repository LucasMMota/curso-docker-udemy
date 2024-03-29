import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)

    print('Aguardando recbimento de mensagens ...')

    while True:
        mensagem = json.loads(r.blpop('sender')[1])

        # Simulando envio do email
        print('Mandando a mensagem', mensagem['assunto'])
        sleep(5)
        print('Mensagem', mensagem['assunto'], 'enviada')
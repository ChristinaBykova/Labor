# from multiprocessing import Process
#
#
# def print_func(continent='Asia'):
#     print(f'Это - {continent}')
#
#
# if __name__ == '__main__':
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)
#     procs.append(proc)
#     proc.start()
#
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     for proc in procs:
#         proc.join()
#
# import threading
#
#
# def print_cube(num):
#     """
#     вычисляет куб от заданного числа num
#     """
#     print(f'Куб {num} -> {num * num * num}')
#
#
# def print_square(num):
#     # вычисляет куб от заданного числа num
#
#     print(f'Квадрат {num} -> {num * 2}')
#
#
# if __name__ == '__main__':
#     #создание двух потоков
#     thread1 = threading.Thread(target=print_square, args=(10,))
#     thread2 = threading.Thread(target=print_cube, args=(10,))
#     #запуск потоков
#     thread1.start()
#     thread2.start()
#
#     thread1.join() #ождание выполнения первого потока
#     thread2.join()
#
#     print('Процессы завершены')
#
# def print_name(prefix):
#     print(f' {prefix}')
#     try:
#         while True:
#             name = (yield)
#             if prefix in name:
#                 print(name)
#     except GeneratorExit:
#         print('Корутина (coroutine) завершина')
#
# corou = print_name('Уважаемый')
# corou.__next__()
# corou.send('товарищ')
# corou.send('Уважаемый товарищ')
# corou.close()

# import signal
# import sys
# import json
# import asyncio
# import aiohttp
#
# loop = asyncio.get_event_loop()
# client = aiohttp.ClientSession(loop=loop)
#
#
# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200
#         return await response.read()
#
#
# async def get_reddit_top(subredit, client):
#     url = 'https://www.reddit.com/r/' + subredit + '/top.json?sort=top&t=day&limit=5'
#     print(url)
#     data1 = await get_json(client, url)
#     j = json.loads(data1.decode('utf-8'))
#     for i in j['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + ' (' + link + ')')
#     print('Готово:', subredit + '\n')
#
#
# def signal_handler(signal, frame):
#     loop.stop()
#     client.close()
#     sys.exit(0)
#
#
# signal.signal(signal.SIGINT, signal_handler)
# asyncio.ensure_future(get_reddit_top('python', client))
# asyncio.ensure_future(get_reddit_top('programming', client))
# asyncio.ensure_future(get_reddit_top('compsci', client))
# loop.run_forever()

from lib import count_word_at_url
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())
job = q.enqueue(count_word_at_url, 'http://nvie.com')



import random
from time import sleep
from tqdm import tqdm

init()

name2 = input("Номер тел/URL: ")
input("Прокси: ")
name = input("Сколько сообщений/ботов: ")
print("Атака!")
for i in tqdm(range(100), colour="green"):
	sleep(random.uniform(0.01, 0.1))

input() 

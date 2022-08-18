import random,time

start_time=time.time()

random_number = random.randint(1, 10)

time.sleep(random_number)

end_time=time.time()

print('Time in seconds: ',end_time-start_time,' generated number is : ', random_number)
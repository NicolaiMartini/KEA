from time import ticks_us,ticks_diff

def fill_list1():
	test_list=[]
	for i in range(10000):
		test_list.append(i)

def fill_list2():
	test_list=[]
	for i in range(10000):
		test_list.insert(0,i)

start=ticks_us()
fill_list1()
delta1=ticks_us()-start
print(f"It took {delta1} microseconds to execute fill_list1")

start=ticks_us()
fill_list2()
delta2=ticks_us()-start
print(f"It took {delta2} microseconds to execute fill_list2")
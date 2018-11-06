import time
a,b = (0,0)
while(True):
	if(b-a>1):
		print("eh maior")
	a = time.time()
	print("a = ")
	print(a)
	print("b = ")
	print(b)
	time.sleep(1.3)
	b = time.time()

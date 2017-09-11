
num=int(input('enter the no of elements'))
if num<0:
 	print("enter a positive number")
else:
	sum=0
	while(num>0):
		sum+=num
		num-=1
	print('the sum is {0}'.format(sum))

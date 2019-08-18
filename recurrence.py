import os 

def getsize(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path,filename)
			total = total + getsize(childpath)
	print('{0:<8}'.format(total),path)
	return total

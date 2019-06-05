import os
import optparse
from winreg import *
def sid2user(sid):
	try:
		key=OpenKey(HKEY_LOCAL_MACHINE,reserved=0,access=KEY_READ)
		(value,type)=QueryValueEx(key,'ProfileImagePath')
		user =value.split('\\')[-1]
		return user
	except:
		return sid
def returnDir():
	dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
	for recycleDir in dirs:
		if os.path.isdir(recycleDir):
			return recycleDir
		return None		



def main():
	print(returnDir())

if __name__ == '__main__':
			main()
					
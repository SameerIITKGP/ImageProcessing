import ftplib
session = ftplib.FTP('localhost','sameer','SamH1/0P')
filename = 'form.jpg'
if filename in session.nlst():
	print 'File already present!'
else:
	print 'File not Found'
	file = open(filename,'rb')
	session.storbinary('STOR ' + filename, file)
	file.close()
	print 'File Copied!'
session.quit()

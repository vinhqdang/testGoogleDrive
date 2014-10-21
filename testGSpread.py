import gspread
import threading
from time import sleep
from datetime import datetime

# Login with your Google account
#gc1 = gspread.login('score.inria.test.001@gmail.com', 'scoreINRIA')
#gc2 = gspread.login('inria.score.test.002@gmail.com', 'scoreINRIA')
#gc2 = gspread.login('score.inria.test.001@gmail.com', 'scoreINRIA')

# Open a worksheet from spreadsheet with one shot
# wks1 = gc1.open("testSCOREINRIA").sheet1
# wks2 = gc2.open("testSCOREINRIA").sheet1

NUM_USERS = 500
gc = list ()
wks = list ()

#test how many users can login at the same time
for i in range (NUM_USERS):
	print i
	gc.append (gspread.login('score.inria.test.001@gmail.com', 'scoreINRIA'))
	wks.append (gc[i].open("testSCOREINRIA").sheet1)
	if (i > 0):
		lines = file('file1.txt', 'r').readlines() 
		#print lines 
		del lines[-1] 
		#print lines 
		file('file1.txt', 'w').writelines(lines) 
	file('file1.txt', 'a').write (str(i + 1) + '\n')
	
# def thread_write (index):
	# CELL = "A" + str (index)
	# while (True):
		# wks[index].update_acell (CELL, str(index))
		
# for i in range (NUM_USERS):
	# t = threading.Thread (target = thread_write, args = (i))
	# t.start ()

# try to modify and read cell B4
# TEST_CELL = "B4"

# wks1.update_acell (TEST_CELL,"0")

# modify_time = list ()
# retrieve_time = list ()

# NUM_TEST = 10
# SLEEP = 2

# print "Until Here"

# def thread_modify ():
	# for i in range (NUM_TEST):
		# print i
		# modify_time.append (datetime.now())
		# wks1.update_acell (TEST_CELL, "5")
		# sleep (SLEEP)

# def thread_retrieve ():
	# while (True):
		# print wks2.acell (TEST_CELL).value
		# if (wks2.acell (TEST_CELL).value == "5"):
			# retrieve_time.append (datetime.now())
			# if (len (retrieve_time) == NUM_TEST): 
				# for i in range (NUM_TEST):
					# print retrieve_time[i] - modify_time [i]
				# break
			# wks2.update_acell (TEST_CELL, "0")
			
# t1 = threading.Thread(target=thread_modify, args=[])
# t2 = threading.Thread(target=thread_retrieve, args=[])
# t1.start()
# t2.start()	




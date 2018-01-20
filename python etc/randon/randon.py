import datetime
import time

def minutes_to_hours(minutes):
	hours = minutes /60
	return hours

def seconds_to_hours(seconds):
	hours = seconds /3600
	return hours

def cel_to_fahr(c):
	f = c* 9/5 +32
	return f

def string_length(string):
	if(type(string)==int):
		return ("Integers don't have length"+ "!"*5)
	elif (type(string)==float):
		return "Floats don't have length"
	return len(string)

def is_even_number(number):
	if number%2 == 0:
		return True
	else:
		return False

def print_list(list):
	for item in list:
		print (item)

def print_2lists(list1,list2): 
	for i,j in zip(list1,list2): #majorated by the smallest list
		print(i,j)

def is_prime_number(number):
	if number == 1:
		return False
	it = number-1
	while number%it != 0:
		it-=1
	return bool(it ==1)

def print_content_of_file(file_path):
	file = open(file_path,"r")
	content=file.read()
	file.close
	print (content)

def file_lines_to_list(file_path):
	file = open(file_path,'r')
	list = file.readlines()
	file.close
	return list

def file_overwrite(file_path,string):
	with open(file_path,"w") as file:
		file.write(string)

def file_append(file_path,string):
	with open(file_path,"a") as file:
		file.write(strin)

def create_file_time():
	filename = datetime.datetime.now()
	with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
		for i in range(5):
			line = str(datetime.datetime.now())+ "\n"
			file.write(line)
			time.sleep(1) #wait 1 second

def merge_all_files_in_folder():
	import glob2
	filenames = glob2.glob("*.txt")
	print(filenames)
	with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
		for filename in filenames:
			with open(filename,"r") as f:
				file.write(f.read()+'\n')



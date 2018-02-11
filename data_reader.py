#!C:\Python\python.exe

import csv

def baca_csv(file_name,delimit):
	#Fungsi untuk membaca semua data csv
	data_all = []
	with open(file_name) as csv_file:
		csv_obj = csv.reader(csv_file,delimiter=delimit)
		for baris in csv_obj:
			data_all.append(baris)
	return data_all

def user_loc_extractor(data_all,user_index,loc_index):
	#Fungsi untuk mengekstrak data user dan lokasi
	data = []
	for dt in data_all:
		data.append([int(dt[user_index]),str(dt[loc_index])])
	return data
	
def user_list(data_user_loc,index):
	#Fungsi untuk mendata user/location yang ada
	data = []
	for dt in data_user_loc:
		if dt[index] not in data:
			data.append(dt[index])
	data = sorted(data,reverse=False)
	return data
	
def info_dataset(data_all,data_user,data_location):
	print 'Jumlah record dataset\t: %d' % (len(data_all))
	print 'Jumlah user          \t: %d' % (len(data_user))
	print 'Jumlah lokasi        \t: %d' % (len(data_location))
	
def matrix_maker(data_user_loc,data_user,data_location):
	#Fungsi untuk membuat matrix
	data_all = []
	for dt_user in data_user:
		data_temp = []
		for dt_loc in data_location:
			if [dt_user,dt_loc] in data_user_loc:
				#jika lokasi pernah dikunjungi
				data_temp.append(1)
			else:
				#jika lokasi belum pernah dikunjungi
				data_temp.append(0)
		data_all.append(data_temp)
	return data_all

def tampil_matrix(matrix):
	for m in matrix:
		print m
	
file_name_input = "trainA.csv" #input nama file yang akan diformat
input_delimiter = ","
data_all = baca_csv(file_name_input,input_delimiter)
data_user_loc = user_loc_extractor(data_all,0,1)
data_user = user_list(data_user_loc,0)
data_location = user_list(data_user_loc,1)

info_dataset(data_all,data_user,data_location)


matrix = matrix_maker(data_user_loc,data_user,data_location)  #Ini matrix yang dihasilkan
tampil_matrix(matrix)

output = open("hasil.csv","a")
output.write(str(matrix))
output.close()
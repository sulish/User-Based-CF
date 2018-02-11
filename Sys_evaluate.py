

import timeit
import reco

# Melakukan perhitungan MAE dengan menghitung jumlah absolute dri selisih antara rating hasil prediksi dengan rating pada matrix rating test data, kemudian dibagi dengan jumlah item 
# dalam list rekomenda/home/arynas/Documents/Code/sandbox/DOOTwitterSentimentsi yang terdpat pada matrik rating test data
def evaluate(ranks, testData, user):
	n=0
	i=0
	sum_abs=0

	#hitung mae
	for(x,y) in ranks:
		try:
			sum_abs += abs(testData[user][y]-float(x))
			n +=1
		except KeyError:
			pass
# penghitungan rata" nilai MAE dan jumlah total yang direkomendasikan
	if n == 0:return "NA"
	mae = sum_abs/n
	# print (mae)
	totalRec = len(ranks)

	return mae, totalRec


# input : matrix ratin dari data training dan testing , digunakan untuk menghitung nilai MAE. 
def uAverageEval(trainData,testData):
	n=0
	sum_m=0
	sum_p=0
	sum_t=0

	# path = "/home/arynas/Documents/Code/sulis's-tesis/080218/Dataset1/"
	path= "D:/DATA MINING/Dataset1/"
	# path = "G:/Pandu/movieLens/"
	with open(path+'user.data') as f:
		lines=f.readlines()
	totaluser=len(lines)

	userList=list(range(1,totaluser+1))

	for user in userList:
		try:
			start=timeit.default_timer()
			ranks=reco.uRecommendCos(trainData,str(user))		#ambil dri fungsi item recomenda based
			#print ranks
			stop=timeit.default_timer()
			time=stop-start
			a=evaluate(ranks,testData,str(user))
		except KeyError: a="NA"

		if a != "NA":
			sum_m += a[0]
			print (sum_m)
			sum_p += a[1]
			print (sum_p)
			sum_t += time
			n+=1
	if n==0:
		print("not available")
	else:
		print(n)
		print("rata-rata MAE=",sum_m/n)
		print("rata-rata prediction=", sum_p/n)
		print("rata-rata runtime=",sum_t/n)

def userTest (dataset = 1):
	print ("Ini adalah pengujian dataset: " +str(dataset))
	print ("Menggunakan metode similarity cosine")
	i=1
	while i<= 1:
		train = reco.loadData("train", dataset,i)
		#print (train)
		test = reco.loadData("test", dataset,i)
		#print (test)
		uAverageEval(train,test)
		i += 1

userTest()
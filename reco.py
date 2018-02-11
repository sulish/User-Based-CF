# def loadData(purpose, dataset,number,path="D:/THESIS/PENELITIAN/Sistem Rekomendasi/User-Based-CF/Dataset/"):
def loadData(purpose, dataset,number,path="D:/DATA MINING/"):
	ratingMatrix={}
	
	#Membangun rating matrix
	for line in open (path+"Dataset"+str(dataset)+"/"+purpose+str(number)+'.csv'):  #purpose(training atau testing)
	# for line in open (path+"Dataset"+str(dataset)+"-"+purpose+str(number)+'.csv'):  #purpose(training atau testing)
	# for line in open ('traincoba.csv'):  #purpose(training atau testing)
		(user,location,rating)=line.rstrip("\n").split(',')
		ratingMatrix.setdefault(user,{})
		ratingMatrix[user][location]=float(rating)

	return ratingMatrix
	

		
	# a=loadData(train,0,0,path)
	# print (a)


from math import sqrt

def cosineSim(itemmatrix,p1,p2):
	top=0
	bot1=0
	bot2=0

	for user in itemmatrix[p1]:		#pencarian item yang sama sama diberi rating oleh user atau bisa disebut item irisan yang dirating oleh kedua user
		if user in itemmatrix[p2]:
			x=itemmatrix[p1][user]	#dot product
			y=itemmatrix[p2][user]
			top += x*y
			bot1 += x**2
			bot2 += y**2

	bottom =sqrt(bot1)*sqrt(bot2)
	#rint (bottom)

	if bottom == 0:

		return 0
	sim=top/bottom
	#print (sim)
	return sim

#input: itemmatrik(matrik rating dictioary), item(target yang akan dibandingkan similarirynya .kalau user based, targetnya user kalo itembased targetnya item), k(target sepanjang dataset) 
def nearestneighborCos(itemmatrix,target,k):
	values=[(cosineSim(itemmatrix,target,other),other) for other in itemmatrix if other !=target]
	values.sort()
	values.reverse()
	return values[0:k]


import pickle

def matrixconvert(ratingMatrix):	#konversi matriks dari bentuk user-item menjadi bentuk item-user
	itemmatrix={}
	for user in ratingMatrix:
		for item in ratingMatrix[user]:
		#Mengubah item menjadi key dan user menjadi subkey
			itemMatrix.setdefault(item,{})
			itemMatrix[item][user]=ratingMatrix[user][item]
	return itemMatrix
	
#membuka file pickle
# def readpickle(path="C:/Python27/Lib/site-packages/xy/"):
# 	with open(path+"filenamecluster.txt","rb") as f:
# 		model=pickle.load(f)
# Output fungsi merupakan dictionary dengan judul film sebagai key dan list neighbor sebagai value. kemudian dict ini di save dalam bentuk .txt menggunakan modul pickle dengan nama file path yang telah
# ditentukan dalam fungsi ini
# pembentukan model data merupakan matriks yang berisi similaritas item

def modelBuildCos(output,filename,ratingMatrix):
	result={}
	itemmatrix=matrixconvert(ratingMatrix)			#konversi matrix user-item ke item-user
	current=0
	total=len(itemmatrix)

	for item in itemmatrix:
		#Melihat progress pembentukan matrik
		current +=1
		if current %100==0:
			print("%d / %d" % (current,total))

			# Menghitung k-most similar neigbors dari item
		neighbors=nearestneighborCos(itemmatrix,item,k=(total-1))
		result[item]=neighbors
		# print result

	with open(output+filename+".txt","wb") as f:
		pickle.dump(result,f)

# Generasi Prediksi
# input : rating matrix user

def uRecommendCos(ratingMatrix,user):
	totals={}
	simtotal={}
	rangkings=[]

	neighborMax=len(ratingMatrix)-1
	# print (neighborMax)
	neighborhood= nearestneighborCos(ratingMatrix,user,k=neighborMax)
	# print (neighborhood)

	for (sim,other) in neighborhood:
		if sim <= 0 :continue
		for item in ratingMatrix[other]:
			#Hanya perhitungkan item yang belum diberi rating
			if item not in ratingMatrix[user] or ratingMatrix[user][item] == 0:
				#Similarity*score
				totals.setdefault(item,0)
				totals[item]+= ratingMatrix[other][item]*sim
				#Jumlah dari nilai similarity
				simtotal.setdefault(item,0)
				simtotal[item] += abs(sim)
				# print simtotal


		rangkings=[(total/simtotal[item],item) for item, total in totals.items()]
		# print (rangkings)

	rangkings.sort()
	# rangking.sort()
	rangkings.reverse()
	# rangking.reserve()
	return rangkings
	
# uRecommendCos()

# def uRecommendCos(ratingMatrix,user):

# 	# Gets recommendations for a person by using a weighted average of every other user's rankings
# 	totals = {}
# 	simSums = {}
# 	rankings_list =[]

# 	for other in ratingMatrix:
# 		# don't compare me to myself
# 		if other == user:
# 			continue
# 		sim = cosineSim(ratingMatrix, user,other)
# 		#print ">>>>>>>",sim

# 		# ignore scores of zero or lower
# 		if sim <=0: 
# 			continue
# 		for item in ratingMatrix[other]:

# 			# only score movies i haven't seen yet
# 			if item not in ratingMatrix[user] or ratingMatrix[user][item] == 0:

# 			# Similrity * score
# 				totals.setdefault(item,0)
# 				totals[item] += ratingMatrix[other][item]* sim
# 				# sum of similarities
# 				simSums.setdefault(item,0)
# 				simSums[item]+= sim

# 		# Create the normalized list

# 	rankings = [(total/simSums[item],item) for item,total in totals.items()]
# 	rankings.sort()
# 	rankings.reverse()
# 	# returns the recommended items
# 	recommendataions_list = [recommend_item for score,recommend_item in rankings]
# 	return recommendataions_list
# 		
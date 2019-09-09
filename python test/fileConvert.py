import csv 
import os 


class fileConvert:
	#function for read file
	def readFile(self):
		fileData = open("C:\\New folder\\text files\\DumbFile.txt","r");   
  
		#stores all the data of the file into the variable content  
		content = fileData.read(); 
		dataList=content.split(" \n");

		#closes the opened file  
		fileData.close()  

		return dataList;

	#read data from existing file
	def readCSV(self,path):
		with open(path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			list_CSV_Data=[]
			for row in csv_reader:
				list_CSV_Data.append(row)
		return list_CSV_Data

	#wwrite data into csv file
	def writeData(self,path,fileData,index):
		with open(path,'a') as csvfile:
			filename = ['data']
			writer = csv.DictWriter(csvfile, fieldnames=filename)
			writer.writerow({'data':fileData[index]})


	#function for write CSV file
	def writeCSV(self):
		# readFile()
		fileNameList=[];
		fileData=[];
		dataList=self.readFile()
		
		loop_control=0;
		data_control=0

		#cut data into desire format
		for i in dataList:
			fileNameList.append(i[5:13]);
			fileData.append(i[5:21]+","+i[22:36]);

		#check folder if it exist
		while (1):
			path_check=os.path.isdir(".\\csv_files")
			#if folder is not exist create new folder
			if path_check==False:
				os.makedirs('.\\csv_files')
			else:
				break
		index = 0
		for j in fileNameList:
			#check file if it exist
			file_check=os.path.isfile('.\\csv_files\\'+j+'.csv')
			if file_check == True:
				readData=self.readCSV('.\\csv_files\\'+j+'.csv')

				#check data is duplicate
				for a in readData:
					#check list is not empty
					if len(a)!=0:
						print(fileData[index],a[0])
						#check two Strings are equal
						if sorted(fileData[index]) == sorted(a[0]):
							data_control=1

				#write data
				if data_control==0:
					self.writeData('.\\csv_files\\'+j+'.csv',fileData,index)


			#write new data in new file
			else:
				self.writeData('.\\csv_files\\'+j+'.csv',fileData,index)

			index=index+1
		print("Writing complete")

#main method
if __name__ == '__main__':
	obj = fileConvert()
	obj.writeCSV()
	
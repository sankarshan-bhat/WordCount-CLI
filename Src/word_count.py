import json
from collections import defaultdict
import os
import sys
import re
import codecs
from prettytable import PrettyTable
import argparse
import time

'''
Author: Sankarshan Umesh Bhat
Date: 03/02/2019

'''
class WordCount:
	def __init__(self):
		self.word_count = defaultdict(dict)

	'''
	Counts the number of occurence of each words in the input_file(single) and stores them in a dictionary.
	Note : Only Englsih Alphabetic word is considered as a valid word (no Alphanumeric as mentioned in the requirement)
	'''
	def count_words(self,file_name):
		try:
			#with codecs.open(file_name, encoding='ISO-8859-1') as fp:
			with codecs.open(file_name,encoding='utf8') as fp:
				for line in fp:
					#Only Alphabetic word is considered, if we need to consider alphanumeric then condition
					#should be r'[a-zA-z0-0]+
					#Note: All the words are considered as case insensitive and hence converting it to the lower case while stroing it in the dictionary
					words = re.findall(r'[a-zA-Z]+',line.strip().lower()) 
					for w in words:
						if w in self.word_count:
							# if the word is present in the dictionary then increment count for a particuale file
							if file_name in self.word_count[w]:
								self.word_count[w][file_name] += 1
							else:
								self.word_count[w][file_name] = 1

							self.word_count[w]['total_count'] += 1

						else:
							# if the word is not present in the dictionary then add it
							self.word_count[w] = {}
							self.word_count[w][file_name] = 1
							self.word_count[w]['total_count'] = 1
		except Exception as e:
				#if the file is not utf-8 encoded exception is thrown and the file is ignored
				print("exception:",e)

		return self.word_count


	def process_input_file(self,input_file):
		#print (input_file)
		file_list = []
		if not os.path.isfile(input_file):
			print ("Error: Invalid file path/name. Input File: ",input_file," does not exist.")
			return
		try:
			with open(input_file,encoding="utf-8") as ifp:
				for line in ifp:
					if line.strip() !="":
						file_list.append(line.strip())
			#handling duplicate file names in the input
			file_list = list(set(file_list))
			for file in file_list:
					#make sure input file path is valid before processing!
					if os.path.isfile(file):
						self.count_words(file)
					else:
						print ("Error No such File!",file,"Please make sure you have correct path mentioned")
		except Exception as e:
				print("exception:",e)

		return self.word_count		

	def display(self):
		x = json.dumps(self.word_count, indent=4, sort_keys=True)
		open("output.json","w").write(x)
		print(json.dumps(self.word_count, indent=4, sort_keys=True))

	def list_all_words(self):
		table = PrettyTable()

		table.field_names = ["Word", "Total Number of occurence(All files)"]

		for k,v in self.word_count.items():
			table.add_row([k,int(v['total_count'])])
		print (table)
		return table

	def display_top_k(self,k):
		table = PrettyTable()
		words_dict = sorted(self.word_count.items(), key = lambda tup: (tup[1]["total_count"]),reverse =True)

		table.field_names = ["Word", "Total Number of occurence(All files)"]
		count = 0
		for i in range(len(words_dict)):
			table.add_row([words_dict[i][0],int(words_dict[i][1]['total_count'])])
			count +=1
			if count == int(k):
				break
		print (table)
		return table

	def search_word(self,word):
		table = PrettyTable()
		table.field_names = ["FileName","Count"]

		if word in self.word_count:
			word_info = self.word_count[word]
			print ("\n Occurence in each file:")
			for k,v in word_info.items():
			#dont add total_count, since it is displayed seperatly
				if k != 'total_count':
					table.add_row([k,int(v)])
			print (table)
			print("----------------------------------------------------------------------")
			print ("Total occurence:    ",word_info['total_count'])
			print("----------------------------------------------------------------------")
		else:
			print ("word not found! please input the word which exist in the file")
		return table
		
	def print_help(self):
		print("\n \n ----------------------------------------------------------------------")
		print ("Input Menu: Please choose one from the below options")
		print ("1. Load file,  Usage: '-c [input_file]' ")
		print ("2. List All words,  Usage: '-l [input_file]' ")
		print ("3. Search word, Usage: '-s [search_word]'")
		print ("4. Top k words(most frequent), Usage: '-t [topk_num]'")
		print ("5. Help, Usage: -h")
		print ("6. Exit: -e")


def main():

	# create parser object 
	parser = argparse.ArgumentParser(description = "An Interactive Application to check the occurence of the word across the files!") 

	# defining arguments for parser object 
	parser.add_argument("-c", "--create", type = str, nargs = 1, 
	                    metavar = "input_file_name", default = None, 
	                    help = "Load the input file into the system") 
	  
	parser.add_argument("-l", "--list", action='store_true',
	                    help = "Display the total number of occurence of the words among all the input files") 

	parser.add_argument("-s", "--search", type = str, nargs = 1, 
	                    metavar = "search_word", default = None, 
	                    help = "Display total occurence of the input word along with the occurence of the word across the files") 
	  
	parser.add_argument("-t", "--topk", type = str, nargs = 1, 
	                    metavar = "top_k_value", default = None, 
	                    help = "Display the top k words based on the total number of occurence") 

		  
	wordCount_obj = WordCount()
	 
	while True:
		wordCount_obj.print_help()

		# parse the arguments from standard input 
		astr = input('$: ')
		if astr =="-e" or astr =="--exit":
			break

		try:
		    args = parser.parse_args(astr.split())
		except SystemExit:
		    print ('error')
		    continue

		# calling functions depending on the type of argument
		if args.create != None: 
			wordCount_obj = WordCount()
			#start_time = time.time()
			wordCount_obj.process_input_file(args.create[0])
			#print("--- %s seconds ---" % (time.time() - start_time))
		elif args.search != None: 
			#start_time = time.time()
			if len(wordCount_obj.word_count) >1:
				wordCount_obj.search_word(args.search[0])
			else:
				print ("Error:  Please load the file using -c [input_file_name] before searching!")

			#print("--- %s seconds ---" % (time.time() - start_time))
		elif args.topk != None:
			if len(wordCount_obj.word_count) >1:
				wordCount_obj.display_top_k(args.topk[0])
			else:
				print ("Error: Please load the file using -c [input_file_name] before invoking top k words!")
		elif args.list: 
			if len(wordCount_obj.word_count) >1:
				wordCount_obj.list_all_words()
			else:
				print ("Error: Please load the file using -c [input_file_name] before listing!")

			

if __name__ == '__main__':
	main()


import sys

from word_count import WordCount
import os
import unittest


FAILURE = 'incorrect value'


class WordCountTest(unittest.TestCase):
    '''
    generate test input files and use them for invoking the tests
    '''
    def setUp(self):
        self.wc = WordCount()
        self.word_dict_counts = {"this":1,"is":2,"a":2,"test":1,"file":2,"contents":1,"are":1,"written":1,"to":1,"used":1,"it":1,"for":2,"the":1,"purpose":1,"testing":2}
        self.word_dict_counts_total = {"this":5,"is":10,"a":10,"test":5,"file":10,"contents":5,"are":5,"written":5,"to":5,"used":5,"it":5,"for":10,"the":5,"purpose":5,"testing":10}
        self.file_list = []
        fp2 =open("test_path.txt","w")
        for i in range(1,6):
            file_name = str(i)+".txt"
            fp =open(file_name,"w")
            fp.write("This is a test file. Contents are written to the file for testing!\n")
            fp.write("It is used for a testing purpose!\n")
            fp2.write(os.path.abspath(file_name))
            fp2.write("\n")
            fp.close()
            self.file_list.append(os.path.abspath(file_name))
        fp2.close()
   
    def test_count_totoal_words(self):
        countedWords = self.wc.process_input_file("test_path.txt")
        #print (countedWords)
        self.assertEqual(len(countedWords), len(self.word_dict_counts_total), FAILURE)

    def test_count_words_single_file_2(self):
        countedWords = self.wc.count_words("2.txt")
        self.assertEqual(len(countedWords), 15, FAILURE)

    def test_search_word_totoal_count(self):
        countedWords = self.wc.process_input_file("test_path.txt")
        table = self.wc.search_word("file")
        self.assertEqual(countedWords['file']['total_count'], self.word_dict_counts_total["file"], FAILURE)

    def test_search_word_totoal_count_individual_file(self):
        countedWords = self.wc.count_words("2.txt")
        self.assertEqual(countedWords['file']['total_count'], self.word_dict_counts["file"], FAILURE)

    def test_invalid_search_word(self):
        countedWords = self.wc.process_input_file("test_path.txt")
        table = self.wc.search_word("invalid_word")
        self.assertFalse("invalid_word" in countedWords)

    def test_list_words(self):
        countedWords = self.wc.process_input_file("test_path.txt")
        for k,v in self.word_dict_counts_total.items():
            self.assertEqual(countedWords[k]['total_count'],v,FAILURE)

    def test_search_words_count_across_files(self):
        countedWords = self.wc.process_input_file("test_path.txt")
        word_info = countedWords["for"]
        for i in range(len(self.file_list)):
            self.assertEqual(word_info[self.file_list[i]],self.word_dict_counts["for"],FAILURE)

    def tearDown(self):
        for i in range(len(self.file_list)):
            os.remove(self.file_list[i])
        os.remove("test_path.txt")


if __name__ == '__main__':
    unittest.main()
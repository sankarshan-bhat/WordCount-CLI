WordCount README
==================

Program:
	The program takes the input file and counts the number of words across all the files mentioned in the input.

Running a program:
-------------------------
1. Run using standalone application created

1. Untar the submission.tgz file to current directory and change directory to submission(cd submission).

Windows:
-------------
Copy the dist directory to current directory
1. open cmd
2. cd executables\windows
3. type -> dist\word_count\word_count.exe
3. You will be able to see an interactive menu which list the operation supported.

first load the input file using "-c input_file" -> this will ingest the file into the system and allows you to perform the below operation.

Linux:
---------
I have created the standalone version of the program using nutika library. "python3 -m nuitka --follow-imports --standalone word_count.py"

1. copy the  word_count.dist directory to current directory 
2. open terminal
3. type cd executables/linux
4. type -> word_count.dist/word_count
5. You will be able to see an interactive menu which list the operation supported.


Operation Supported:
-----------------------------------
1. Load the file:
       which loads the input file (which contains absolute path to the text documents) to the system.
Usage : -c input_file_name
Ex: -c path.txt

2. list all words -> Dsiplays all the words found the input files and corresponding count of them across all the files.

Usage: -l
Ex: -l 
+---------------+--------------------------------------+
|      Word     | Total Number of occurence(All files) |
+---------------+--------------------------------------+
|   wellformed  |                  6                   |
|    english    |                  6                   |
|   sentences   |                  3                   |
|     words     |                  12                  |
|      are      |                  12                  |
|   displayed   |                  6                   |
|     using     |                  6                   |
|      some     |                  6                   |
|    context    |                  6                   |
|      but      |                  6                   |
|     these     |                  6                   |
|      dont     |                  6                   |
|      take     |                  6                   |
|       it      |                  6                   |
|       to      |                  12                  |
| consideration |                  6                   |
|       of      |                  6                   |
|      thr      |                  6                   |
|     names     |                  6                   |
|      and      |                  6                   |
|       we      |                  6                   |
|      need     |                  6                   |
|    survive    |                  6                   |
|       is      |                  2                   |
|       d       |                  2                   |
+---------------+--------------------------------------+

3. Search word:
	given a word (from the list of words) it displays which files the word came from how many times the word showed up in each file and total count across all the files.
Usage: -s "word"
Ex: $: -s english

 Occurence in each file:
+---------------+-------+
|    FileName   | Count |
+---------------+-------+
| ./files/2.txt |   2   |
| ./files/3.txt |   2   |
| ./files/1.txt |   2   |
+---------------+-------+
-------------------------
Total occurence:     6
-------------------------


4. Top K (Most frequent) words
	It displays the top "K" words which is most frequently found across all the files and thier corresponding count.

Usage: -t "number"

Ex:$: -t 10
+------------+--------------------------------------+
|    Word    | Total Number of occurence(All files) |
+------------+--------------------------------------+
|   words    |                  12                  |
|    are     |                  12                  |
|     to     |                  12                  |
| wellformed |                  6                   |
|  english   |                  6                   |
| displayed  |                  6                   |
|   using    |                  6                   |
|    some    |                  6                   |
|  context   |                  6                   |
|    but     |                  6                   |
+------------+--------------------------------------+


2. To run the program without the standalone binary, It requires below dependenices.
 1. python3.6
 2. python ptable library (pip3 install ptable)

 please install both and run as "python3 word_count.py" and you will see the same Input menu as displayed above.

Running the Unit test cases:
----------------------------
test.py contains all the Unit test cases.

1. Linux (Standalone)
------------------------
1. copy the  test.dist directory to current directory
2. open terminal
3. type -> cd executables/linux
4. type -> test.dist/test
5. You will see the test ran successfully.


2. Windows (Standalone):
-------------------
Copy the dist directory to current directory
1. open cmd
2. cd executables\windows
3. type -> dist\test\test.exe
4. You will see the test ran successfully.


3. To run the tests without the standalone binary, It requires below dependenices.
 1. python3.6
 2. python ptable library (pip3 install ptable)

 please install both and run as "python3 test.py" and you will see the test ran successfully.


Note: program assumes input_file will be a text documents(.txt) with "UTF-8" encoding.


Input Data:
----------------
· Input data used to test the program is in  "\source_code\test_files" directory.
I have created a around 1350 text files and thier absolute path is mentioned in path.txt which is used to test the program.



Requiremen.txt lists the required depenecies to run the program without the standalone executables which is captured in run.sh

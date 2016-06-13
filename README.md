# plagiarism-checker-in-python
This is a plagiarism checker in python using the ngram algorithm.
How does it work?
You can input the data from files in your desktop and the program will give you a cosine value which is a similarity parameter unit. More the cosine, higher is the similarity, more the plagiarism. Depending on the number of ngrams this value is calculated. Hence, lesser the value of ngrams, more accurate will be your result.

Libraries required:
1. nltk
2. re
3. math
4. collections


HOW TO GET LIBRARIES ON LINUX

	* Get easy_install

sudo apt-get install python-setuptools


	* Install PIP

sudo easy_install pip

	1. Install NLTK: run sudo pip install -U nltk

Test installation: run python then type import nltk

2. Install RE: run sudo pip install -U re
3.sudo pip install -U math
4.sudo pip install -U collections


HOW TO GET LIBRARIES ON WINDOWS:
These steps assume you already have python installed and that python is in your windows environment variables.
Download setup-tools according to your python version. (That is python 2.7 in most cases)
Run the .exe file. The installer will automatically find your python installation location from the registry and install easy_install to the Scripts directory where your python installation is located.
Once the installer has run, add easy_install to the windows environment variables path.

	* Open a command window
	* Run the following command:

easy_install pip


pip install PIL

pip install nltk

pip install re

pip install math

pip install collections
ABSTRACT:

You have two files with a lot of data individually and you want to calculate the similarity ratio. You input the paths of the two files in the code itself and set the value of ngrams. You can set it to any desired number. Ngrams basically splits your sentence into words. If you set the value as 3 (As in the code), ngrams algorithm will split every sentence into 3 words. So obviously, lesser the number of n, more will be the accuracy as the chances of the chunks to be similar reduces. Convert the text into lower case in case the code mistakes it to be a different. Cosine value is calculated as per the vector intersection. You assign "1" if that particular ngram is present and "0" if that ngram is absent. For each sentence, you calculate the vector. Multiply the vectors which gives you the intersection. If there's nothing common, return 0. Since the ngrams return the answer in tuples which is immutable and the vector function takes input as list. So, first I converted the ngrams by joining them into strings and appending them in a list.Using "findall" function returns all non-overlapping matches of pattern in string, as a list of strings. Cosine value thus gives you the result as a similarity parameter between the given two text files.

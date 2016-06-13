# plagiarism-detector-in-python
I made a plagiarism detector in python using the ngram algorithm.
You can input the data from files in your desktop and the program will give you a cosine value which is a similarity parameter unit. 
More the cosine, higher is the similarity, more the plagiarism. Depending on the number of ngrams this value is calculated. 
Hence, more the value of ngrams, more accurate will be your result. 

So, basically. You have two files with a lot of data individually and you want to calculate the similarity ratio. You input
the paths of the two files in the code itself and set the value of ngrams. You can set it to any desired number. Ngrams basically splits your sentence into words. If you set the value as 3 (As in the code), ngrams algorithm will split every sentence into 3 words. So obviously, lesser the number of n, more will be the accuracy as the chances of the chunks to be similar reduces. Convert the text into lower case in case the code mistakes it to be a different. 
Cosine value is calculated as per the vector intersection. You assign "1" if that particular ngram is present and "0" if that ngram is absent. For each sentence, you calculate the vector. Multiply the vectors which gives you the intersection. If there's nothing common, return 0. 
Since the ngrams return the answer in tuples which is immutable and the vector function takes input as list. So, first I converted the ngrams by joining them into strings and appending them in a list.Using "findall" function returns all non-overlapping matches of pattern in string, as a list of strings.
Cosine value thus gives you the result as a similarity parameter between the given two text files.

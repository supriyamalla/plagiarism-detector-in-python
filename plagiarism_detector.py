import nltk
from nltk.util import ngrams
import re, math
from collections import Counter

with open('C:\Users\welcome\Desktop\est1.txt', 'r') as myfile1:
    text1=myfile1.read().replace('\n', '')
with open('C:\Users\welcome\Desktop\est2.txt', 'r') as myfile2:
    text2=myfile2.read().replace('\n', '')

n = 3
text1= ngrams(text1.lower().split(), n)
text2 = ngrams(text2.lower().split(), n)
list1 = []
list2 = []
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator
    
def text_to_vector(list):
     words = WORD.findall(list)
     return Counter(words)

for grams in text1:
    #print(grams)
    str1=''.join(grams)
    list1.append(str1)
    final1 = ', '.join(list1)

for grams in text2:
    #print(grams)
    str2 =''.join(grams) 
    list2.append(str2)
    final2 = ', '.join(list2)
print list1
print list2
print final1
print final2

vector1 = text_to_vector(final1)
vector2 = text_to_vector(final2)
cosine = get_cosine(vector1, vector2)

print 'Cosine:', cosine

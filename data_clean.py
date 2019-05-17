import pandas as pd
import numpy as np
import nltk, re

nltk.download()
from nltk.corpus import stopwords

train = pd.read_csv('train_full.csv')
len_tr = len(train["id"])
test = pd.read_csv('test.csv')
len_ts = len(test["id"])

def comment_cleaning(comment):
	letters = re.sub("[^a-zA-Z]"," ", comment)		#remove non-letter words
	words = letters.lower().split()                         #split words    
	stops = set(stopwords.words("english"))			
	meaningful_words = [w for w in words if not w in stops]	#remove stopwords
	return( " ".join( meaningful_words ))			#return cleaned comment


#def main():
clean_train = []
i = 0
for i in xrange( 0, len_tr ):
	clean_train.append( comment_cleaning(train["comment_text"][i]))

clean_tr = pd.DataFrame(clean_train, columns=["comment_text"])

clean_test = []
i = 0 
for i in xrange( 0, len_ts ):
	clean_test.append( comment_cleaning(test["comment_text"][i]))

clean_ts = pd.DataFrame(clean_test, columns=["comment_text"])

train_new = train.drop(columns=["comment_text"])
train_new = pd.concat([train_new,clean_tr],axis=1)
test_new = test.drop(columns=["comment_text"])
test_new = pd.concat([test_new,clean_ts],axis=1)

train_new.to_csv("train_full_new.csv",index=False)
test_new.to_csv("test_new.csv",index=False)

#if __name__ == '__main__':
#main()




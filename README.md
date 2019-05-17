# Toxic-classification-unsup
Unsupervised classification of toxic comments.
## Problem Statement: 
To classify textual comments as ‘toxic’ or ‘non-toxic’, and distinguish between categories of toxicity in comments
## Dataset: 
The dataset here is from the Wikipedia comments corpus dataset, which was labeled by human raters for toxicity. The data was cleaned extensively. Comments were split into words, all non-letter words and stopwords were removed, and the cleaned comments, containing only the key words, were stored in lowercase. Lastly, it was spliced to create sub-datasets with balanced data points, i.e. number of positive and negative examples very close. For data cleaning (removal of stopwords, etc) and tokenization, we use NLTK (Natural Language Toolkit) for Python.
For reference, see: data_clean.py, ohe.py
## Proposed approach (as implemented in cluster'.ipynb)
Words or comments with similar toxicity would occur close to each other in the feature space, and would therefore be part of the same cluster.
Our novel approach then uses unsupervised learning to create clusters of semantically proximate training and test data vectors, These would be of similar meaning and toxicity value. A column containing cluster assignments is then appended to the training and test dataset. 
Clustering algorithm used is K-Means clustering.
### Method 1: 
We use a simple prediction strategy based on our assumption. Within each cluster, all test data points were assigned the most frequently occurring label value within that cluster.
### Method 2: 
We attempt to refine prediction algorithm further by using distance weights to gauge likelihood of a label. We use Euclidean distance of training vectors within a cluster from the test vector input, to determine most likely label value of that test vector.





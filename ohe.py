import pandas as pd
import numpy as np
train = pd.read_csv('train.csv')
print(train.info())

train_labels = train.drop(columns=['id','comment_text'])
print(train_labels)
num_rows = len(train['id'])

label_names = list(train_labels)
print('\n\n')
print( label_names )
num_cols = len(label_names)
print(num_rows)
print('\n\n')

arr = []
for i in range(0,num_rows):
	arr.append(1)

for i in range(0,num_rows):
	for col in label_names:
		if(train_labels.iloc[i][col] == 1):
			arr[i] = 0

print(arr)
clean = pd.DataFrame(data={'non-toxic':arr})
final_train = pd.concat([train,clean], axis=1)
print(final_train)
final_train.to_csv('train_full.csv', index=False)

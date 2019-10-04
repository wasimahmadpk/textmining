import pandas as pd 

# read train data

train_data = pd.read_csv(r'F:\AppliedAI\NLPpro\textmining\datasets\train.tsv', sep='\t')

print(train_data.head(5))
print(train_data.info())
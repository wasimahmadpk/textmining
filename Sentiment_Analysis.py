import pandas as pd 
import matplotlib.pyplot as plt

# read train data

train_data = pd.read_csv(r'F:\AppliedAI\NLPpro\textmining\datasets\train.tsv', sep='\t')

print(train_data.head(5))
print(train_data.info())

print(train_data.Sentiment.value_counts())

Sentiment_count = train_data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show()
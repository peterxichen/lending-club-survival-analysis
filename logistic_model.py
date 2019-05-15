import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import SparsePCA, PCA
from sklearn.model_selection import KFold


DATA_PATH = "arct-2017-1-last-updated-2019-03-31-as-of-2019-04-27.csv"
df = pd.read_csv(DATA_PATH)
print(df.columns.values)

prepay = ['Paid Off']
df['Prepaid'] = df.apply(lambda r: 1 if r['Loan Status'] in prepay else 0, axis=1)

failure = ['Charged Off', 'Sold - Debt Sale', 'Defaulted' ]
df['Default'] = df.apply(lambda r: 1 if r['Loan Status'] in failure else 0, axis=1)

#df = df.dropna()
df = df[['Interest Rate', 'Pre-Loan DTI', 'Revolving Utilization', 'Number of Trade Lines Opened (Last 12 Months)',
        'Number of Inquiries (Last 6 Months)', 'Original FICO', 'Original Loan Balance', 'Annual Income',
        'Total Revolving Balance', 'Months Since Most Recent DQ', 'Term', 'Employment Length', 'Prepaid', 'Default']].dropna()
X = df[['Interest Rate', 'Pre-Loan DTI', 'Revolving Utilization', 'Number of Trade Lines Opened (Last 12 Months)',
        'Number of Inquiries (Last 6 Months)', 'Original FICO', 'Original Loan Balance', 'Annual Income',
        'Total Revolving Balance', 'Months Since Most Recent DQ', 'Term', 'Employment Length']]

y = df['Prepaid']
model = LogisticRegression(C=1)
print(accuracy_score(model.fit(X,y).predict(X),y))
print(model.coef_)

y = df['Default']
model = LogisticRegression(C=1)
print(accuracy_score(model.fit(X,y).predict(X),y))
print(model.coef_)


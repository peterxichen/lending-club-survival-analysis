import pandas as pd
import numpy as np
import lifelines
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pickle

# dv01 data
df= pd.read_csv('input.csv')
# target = ['Charged Off', 'Sold - Debt Sale', 'Defaulted' ] # default
target = ['Paid Off'] #prepay

# columns to keep
columns_to_keep = ['Original Loan Balance', 'Loan Status', 'Term', 'Grade', 'Interest Rate',
                   'Annual Income', 'Pre-Loan DTI', 'Original FICO', 'Employment Length',
                   'Loan Purpose', 'Housing Status', 'Number of Inquiries (Last 6 Months)',
                   'Months Since Most Recent DQ', 'Number of Trade Lines Opened (Last 12 Months)',
                   'Total Revolving Balance', 'Revolving Utilization',
                   'Charge Off Date', 'Funded Date', 'Loan Maturity Date', 'Loan Paid In Full Date'
                   ]
df = df[ columns_to_keep]
df['Loan Status'] = df.apply(lambda r: 1 if r['Loan Status'] in target else 0, axis=1)

# change date variables
date_vars = ['Charge Off Date', 'Funded Date', 'Loan Maturity Date', 'Loan Paid In Full Date']
for var in date_vars:
    df[var] = pd.to_datetime(df[var])

# calculate duration (matruity or charge off date) 
def time_between(r):
    if r.isnull()['Loan Paid In Full Date']:
        return r['Loan Maturity Date'] - r['Funded Date']
    else:
        return r['Loan Paid In Full Date'] - r['Funded Date']
    #if r.isnull()['Charge Off Date']:
    #    return r['Loan Maturity Date'] - r['Funded Date']
    #else:
    #    return r['Charge Off Date'] - r['Funded Date']
T = df.apply(lambda r: time_between(r), axis=1).dt.days
E = df['Loan Status']

# survival analysis
cph = lifelines.CoxPHFitter()
X = df
X['T'] = T

# One Hot encode the categorical features
cat_vars = ['Grade', 'Loan Purpose', 'Housing Status']
for var in cat_vars:
    X = pd.concat((X, pd.get_dummies(X[var])), 1)
    X = X.drop(var, axis=1)
    
# remove unused datetime features
X = X.drop(['Charge Off Date', 'Funded Date', 'Loan Maturity Date', 'Loan Paid In Full Date'], axis=1)

# for simplicity, drop the null rows
X = X.dropna()
X = X.reset_index(drop=True)

# check correlations among features
corr = X.corr()
corr.loc[:,:] = np.tril(corr, k=-1)
corr = corr.stack()

print('Large Correlations:')
print(corr[(corr > 0.55) | (corr < -0.55)])

var = X.var()
print('Small Variance')
print(var[var == 0.0])
print(X.columns)

# drop features with small variance + remove one column of each variable to ensure there is no multicollinearity
X = X.drop(['Other', 'LC-F', 'Rent'], axis=1)

# visualize
cph.fit(X, duration_col='T', event_col='Loan Status')
cph.print_summary()
cph.plot()

X = df
X['T'] = T
# remove insignificatant variables + interest rate
drop_vars = ['Interest Rate', 'Grade', 'Loan Purpose', 'Housing Status', 'Charge Off Date', 'Funded Date', 'Loan Maturity Date', 'Loan Paid In Full Date']

for var in drop_vars:
    X = X.drop(var, axis=1)
    
# For simplicity, drop the null rows
X = X.dropna()
X = X.reset_index(drop=True)

cph.fit(X, duration_col='T', event_col='Loan Status')
cph.print_summary()
print(X.columns)
cph.plot()

# normalize
temp = X[['Original Loan Balance', 'Term', 'Annual Income',
       'Pre-Loan DTI', 'Original FICO', 'Employment Length',
       'Number of Inquiries (Last 6 Months)', 'Months Since Most Recent DQ',
       'Number of Trade Lines Opened (Last 12 Months)',
       'Total Revolving Balance', 'Revolving Utilization']]
min_max_scaler = preprocessing.MinMaxScaler()
temp_scaled = min_max_scaler.fit_transform(temp)
X_imputed = pd.DataFrame(temp_scaled)
X_imputed['T'] = X['T']
X_imputed['Loan Status']=X['Loan Status']
X_imputed = X_imputed.rename(index=str, columns={0:'Original Loan Balance', 1:'Term', 2:'Annual Income',
       3:'Pre-Loan DTI', 4:'Original FICO', 5:'Employment Length',
       6:'Number of Inquiries (Last 6 Months)', 7:'Months Since Most Recent DQ',
       8:'Number of Trade Lines Opened (Last 12 Months)',
       9:'Total Revolving Balance', 10:'Revolving Utilization', 'T':'T','Loan Status':'Loan Status'})
X = X_imputed
cph.fit(X, duration_col='T', event_col='Loan Status')
cph.print_summary()

cph.plot()

# extended dataset
df = pickle.load(open("dv01extended.pkl","rb"))
# columns to keep (adding average current balance
columns_to_keep = ['Original Loan Balance', 'Loan Status', 'Term', 'Grade', 'Interest Rate',
                   'Annual Income', 'Pre-Loan DTI', 'Original FICO', 'Employment Length',
                   'Loan Purpose', 'Housing Status', 'Number of Inquiries (Last 6 Months)',
                   'Months Since Most Recent DQ', 'Number of Trade Lines Opened (Last 12 Months)',
                   'Total Revolving Balance', 'Revolving Utilization',
                   'Charge Off Date', 'Funded Date', 'Loan Maturity Date',
                   'acc_now_delinq','acc_open_past_24mths','avg_cur_bal','bc_open_to_buy',
                   'bc_util','chargeoff_within_12_mths','collections_12_mths_ex_med',
                   'mo_sin_old_il_acct','mo_sin_old_rev_tl_op','mo_sin_rcnt_rev_tl_op',
                   'mo_sin_rcnt_tl','mort_acc','num_accts_ever_120_pd','num_actv_bc_tl',
                   'num_actv_rev_tl','num_bc_sats','num_bc_tl','num_il_tl','num_op_rev_tl',
                   'num_rev_accts','num_rev_tl_bal_gt_0','num_sats','num_tl_120dpd_2m',
                   'num_tl_30dpd','num_tl_90g_dpd_24m','open_acc','pct_tl_nvr_dlq',
                   'percent_bc_gt_75','pub_rec','pub_rec_bankruptcies','tax_liens',
                   'tot_coll_amt','tot_cur_bal','tot_hi_cred_lim','total_acc',
                   'total_bal_ex_mort','total_bc_limit','total_il_high_credit_limit',
                   'total_rev_hi_lim']
df = df[ columns_to_keep]
df['Loan Status'] = df.apply(lambda r: 1 if r['Loan Status'] in target else 0, axis=1)

# change date variables
date_vars = ['Charge Off Date', 'Funded Date', 'Loan Maturity Date']
for var in date_vars:
    df[var] = pd.to_datetime(df[var])

# calculate duration (matruity or charge off date) 
def time_between(r):
    if r.isnull()['Charge Off Date']:
        return r['Loan Maturity Date'] - r['Funded Date']
    else:
        return r['Charge Off Date'] - r['Funded Date']
T = df.apply(lambda r: time_between(r), axis=1).dt.days
E = df['Loan Status']

# survival analysis
cph = lifelines.CoxPHFitter()
X = df
X['T'] = T

# One Hot encode the categorical features
cat_vars = ['Grade', 'Loan Purpose', 'Housing Status']
for var in cat_vars:
    X = pd.concat((X, pd.get_dummies(X[var])), 1)
    X = X.drop(var, axis=1)
    
# remove unused datetime features
X = X.drop(['Charge Off Date', 'Funded Date', 'Loan Maturity Date'], axis=1)

# for simplicity, drop the null rows
X = X.dropna()
X = X.reset_index(drop=True)

X = X.convert_objects(convert_numeric=True)
# check correlations among features
corr = X.corr()
corr.loc[:,:] = np.tril(corr, k=-1)
corr = corr.stack()

print('Large Correlations:')
print(corr[(corr > 0.55) | (corr < -0.55)])

var = X.var()
print('Small Variance')
print(var[var == 0.0])
print(X.columns)

# drop features with small variance + remove one column of each variable to ensure there is no multicollinearity
X = X.drop(['Other', 'LC-F', 'Rent'], axis=1)
X = X.dropna()
X = X.reset_index(drop=True)

# visualize
cph.fit(X, duration_col='T', event_col='Loan Status')
cph.print_summary()
cph.plot()

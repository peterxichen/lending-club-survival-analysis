import numpy as np
import pandas as pd
import pickle
from datetime import datetime

# import downloaded Lending Club data
"""
df1 = pd.read_csv("LoanStats_2016Q1.csv")
df2 = pd.read_csv("LoanStats_2016Q2.csv")
df3 = pd.read_csv("LoanStats_2016Q3.csv")
df4 = pd.read_csv("LoanStats_2016Q4.csv")
df5 = pd.read_csv("LoanStats_2017Q1.csv")
df6 = pd.read_csv("LoanStats_2017Q2.csv")
df7 = pd.read_csv("LoanStats_2017Q3.csv")
df8 = pd.read_csv("LoanStats_2017Q4.csv")
df9 = pd.read_csv("LoanStats_2018Q1.csv")
df10 = pd.read_csv("LoanStats_2018Q2.csv")
df11 = pd.read_csv("LoanStats_2018Q3.csv")
df12 = pd.read_csv("LoanStats_2018Q4.csv")
df13 = pd.read_csv("LoanStats_2015.csv")
df14 = pd.read_csv("LoanStats_2014.csv")
df15 = pd.read_csv("LoanStats_201213.csv")
df = pd.concat([df1, df2, df3, df4, df5, df6,
                     df7, df8, df9, df10, df11,
                     df12, df13, df14, df15], axis=0, ignore_index=True)
df.to_pickle("lendingclub.pkl")
"""

# import compiled lending club data
lending_club_df = pickle.load(open("lendingclub.pkl","rb"))
print(list(lending_club_df.columns.values))

lending_club_df['issue_d'] = pd.to_datetime(lending_club_df['issue_d'], format='%b-%y')

# dv01 data
df = pd.read_csv("arct-2017-1-last-updated-2019-03-31-as-of-2019-04-27.csv")
print(list(df.columns.values))

# additional fields scraped from lending club
df['id']=''
df['member_id']=''
df['loan_amnt']=''
df['funded_amnt']=''
df['funded_amnt_inv']=''
df['term']=''
df['int_rate']=''
df['installment']=''
df['grade']=''
df['sub_grade']=''
df['emp_title']=''
df['emp_length']=''
df['home_ownership']=''
df['annual_inc']=''
df['verification_status']=''
df['issue_d']=''
df['loan_status']=''
df['pymnt_plan']=''
df['url']=''
df['desc']=''
df['purpose']=''
df['title']=''
df['zip_code']=''
df['addr_state']=''
df['dti']=''
df['delinq_2yrs']=''
df['earliest_cr_line']=''
df['inq_last_6mths']=''
df['mths_since_last_delinq']=''
df['mths_since_last_record']=''
df['open_acc']=''
df['pub_rec']=''
df['revol_bal']=''
df['revol_util']=''
df['total_acc']=''
df['initial_list_status']=''
df['out_prncp']=''
df['out_prncp_inv']=''
df['total_pymnt']=''
df['total_pymnt_inv']=''
df['total_rec_prncp']=''
df['total_rec_int']=''
df['total_rec_late_fee']=''
df['recoveries']=''
df['collection_recovery_fee']=''
df['last_pymnt_d']=''
df['last_pymnt_amnt']=''
df['next_pymnt_d']=''
df['last_credit_pull_d']=''
df['collections_12_mths_ex_med']=''
df['mths_since_last_major_derog']=''
df['policy_code']=''
df['application_type']=''
df['annual_inc_joint']=''
df['dti_joint']=''
df['verification_status_joint']=''
df['acc_now_delinq']=''
df['tot_coll_amt']=''
df['tot_cur_bal']=''
df['open_acc_6m']=''
df['open_act_il']=''
df['open_il_12m']=''
df['open_il_24m']=''
df['mths_since_rcnt_il']=''
df['total_bal_il']=''
df['il_util']=''
df['open_rv_12m']=''
df['open_rv_24m']=''
df['max_bal_bc']=''
df['all_util']=''
df['total_rev_hi_lim']=''
df['inq_fi']=''
df['total_cu_tl']=''
df['inq_last_12m']=''
df['acc_open_past_24mths']=''
df['avg_cur_bal']=''
df['bc_open_to_buy']=''
df['bc_util']=''
df['chargeoff_within_12_mths']=''
df['delinq_amnt']=''
df['mo_sin_old_il_acct']=''
df['mo_sin_old_rev_tl_op']=''
df['mo_sin_rcnt_rev_tl_op']=''
df['mo_sin_rcnt_tl']=''
df['mort_acc']=''
df['mths_since_recent_bc']=''
df['mths_since_recent_bc_dlq']=''
df['mths_since_recent_inq']=''
df['mths_since_recent_revol_delinq']=''
df['num_accts_ever_120_pd']=''
df['num_actv_bc_tl']=''
df['num_actv_rev_tl']=''
df['num_bc_sats']=''
df['num_bc_tl']=''
df['num_il_tl']=''
df['num_op_rev_tl']=''
df['num_rev_accts']=''
df['num_rev_tl_bal_gt_0']=''
df['num_sats']=''
df['num_tl_120dpd_2m']=''
df['num_tl_30dpd']=''
df['num_tl_90g_dpd_24m']=''
df['num_tl_op_past_12m']=''
df['pct_tl_nvr_dlq']=''
df['percent_bc_gt_75']=''
df['pub_rec_bankruptcies']=''
df['tax_liens']=''
df['tot_hi_cred_lim']=''
df['total_bal_ex_mort']=''
df['total_bc_limit']=''
df['total_il_high_credit_limit']=''
df['revol_bal_joint']=''
df['sec_app_earliest_cr_line']=''
df['sec_app_inq_last_6mths']=''
df['sec_app_mort_acc']=''
df['sec_app_open_acc']=''
df['sec_app_revol_util']=''
df['sec_app_open_act_il']=''
df['sec_app_num_rev_accts']=''
df['sec_app_chargeoff_within_12_mths']=''
df['sec_app_collections_12_mths_ex_med']=''
df['sec_app_mths_since_last_major_derog']=''
df['hardship_flag']=''
df['hardship_type']=''
df['hardship_reason']=''
df['hardship_status']=''
df['deferral_term']=''
df['hardship_amount']=''
df['hardship_start_date']=''
df['hardship_end_date']=''
df['payment_plan_start_date']=''
df['hardship_length']=''
df['hardship_dpd']=''
df['hardship_loan_status']=''
df['orig_projected_additional_accrued_interest']=''
df['hardship_payoff_balance_amount']=''
df['hardship_last_payment_amount']=''
df['debt_settlement_flag']=''
df['debt_settlement_flag_date']=''
df['settlement_status']=''
df['settlement_date']=''
df['settlement_amount']=''
df['settlement_percentage']=''
df['settlement_term']=''


# cross reference by income, state, loan amount, dti, issue date
for index, row in df.iterrows():
     this = lending_club_df[(lending_club_df['annual_inc'] == row['Annual Income'])&
                           (lending_club_df['addr_state'] == row['State'])&
                           (lending_club_df['funded_amnt'] == row['Original Loan Balance'])&
                           (lending_club_df['dti'] < 100*row['Pre-Loan DTI']+.01)&
                           (lending_club_df['dti'] > 100*row['Pre-Loan DTI']-.01)&
                           (lending_club_df['issue_d'] == datetime(datetime.strptime(row['Funded Date'], '%Y-%m-%d').year,
                                                                         datetime.strptime(row['Funded Date'], '%Y-%m-%d').month, 1))]
     
     if (this.shape[0] != 1):
          print('Failed to query row ', index)
     else:
          df.set_value(index, 'id', this['id'].values[0])
          df.set_value(index, 'member_id', this['member_id'].values[0])
          df.set_value(index, 'loan_amnt', this['loan_amnt'].values[0])
          df.set_value(index, 'funded_amnt', this['funded_amnt'].values[0])
          df.set_value(index, 'funded_amnt_inv', this['funded_amnt_inv'].values[0])
          df.set_value(index, 'term', this['term'].values[0])
          df.set_value(index, 'int_rate', this['int_rate'].values[0])
          df.set_value(index, 'installment', this['installment'].values[0])
          df.set_value(index, 'grade', this['grade'].values[0])
          df.set_value(index, 'sub_grade', this['sub_grade'].values[0])
          df.set_value(index, 'emp_title', this['emp_title'].values[0])
          df.set_value(index, 'emp_length', this['emp_length'].values[0])
          df.set_value(index, 'home_ownership', this['home_ownership'].values[0])
          df.set_value(index, 'annual_inc', this['annual_inc'].values[0])
          df.set_value(index, 'verification_status', this['verification_status'].values[0])
          df.set_value(index, 'issue_d', this['issue_d'].values[0])
          df.set_value(index, 'loan_status', this['loan_status'].values[0])
          df.set_value(index, 'pymnt_plan', this['pymnt_plan'].values[0])
          df.set_value(index, 'url', this['url'].values[0])
          df.set_value(index, 'desc', this['desc'].values[0])
          df.set_value(index, 'purpose', this['purpose'].values[0])
          df.set_value(index, 'title', this['title'].values[0])
          df.set_value(index, 'zip_code', this['zip_code'].values[0])
          df.set_value(index, 'addr_state', this['addr_state'].values[0])
          df.set_value(index, 'dti', this['dti'].values[0])
          df.set_value(index, 'delinq_2yrs', this['delinq_2yrs'].values[0])
          df.set_value(index, 'earliest_cr_line', this['earliest_cr_line'].values[0])
          df.set_value(index, 'inq_last_6mths', this['inq_last_6mths'].values[0])
          df.set_value(index, 'mths_since_last_delinq', this['mths_since_last_delinq'].values[0])
          df.set_value(index, 'mths_since_last_record', this['mths_since_last_record'].values[0])
          df.set_value(index, 'open_acc', this['open_acc'].values[0])
          df.set_value(index, 'pub_rec', this['pub_rec'].values[0])
          df.set_value(index, 'revol_bal', this['revol_bal'].values[0])
          df.set_value(index, 'revol_util', this['revol_util'].values[0])
          df.set_value(index, 'total_acc', this['total_acc'].values[0])
          df.set_value(index, 'initial_list_status', this['initial_list_status'].values[0])
          df.set_value(index, 'out_prncp', this['out_prncp'].values[0])
          df.set_value(index, 'out_prncp_inv', this['out_prncp_inv'].values[0])
          df.set_value(index, 'total_pymnt', this['total_pymnt'].values[0])
          df.set_value(index, 'total_pymnt_inv', this['total_pymnt_inv'].values[0])
          df.set_value(index, 'total_rec_prncp', this['total_rec_prncp'].values[0])
          df.set_value(index, 'total_rec_int', this['total_rec_int'].values[0])
          df.set_value(index, 'total_rec_late_fee', this['total_rec_late_fee'].values[0])
          df.set_value(index, 'recoveries', this['recoveries'].values[0])
          df.set_value(index, 'collection_recovery_fee', this['collection_recovery_fee'].values[0])
          df.set_value(index, 'last_pymnt_d', this['last_pymnt_d'].values[0])
          df.set_value(index, 'last_pymnt_amnt', this['last_pymnt_amnt'].values[0])
          df.set_value(index, 'next_pymnt_d', this['next_pymnt_d'].values[0])
          df.set_value(index, 'last_credit_pull_d', this['last_credit_pull_d'].values[0])
          df.set_value(index, 'collections_12_mths_ex_med', this['collections_12_mths_ex_med'].values[0])
          df.set_value(index, 'mths_since_last_major_derog', this['mths_since_last_major_derog'].values[0])
          df.set_value(index, 'policy_code', this['policy_code'].values[0])
          df.set_value(index, 'application_type', this['application_type'].values[0])
          df.set_value(index, 'annual_inc_joint', this['annual_inc_joint'].values[0])
          df.set_value(index, 'dti_joint', this['dti_joint'].values[0])
          df.set_value(index, 'verification_status_joint', this['verification_status_joint'].values[0])
          df.set_value(index, 'acc_now_delinq', this['acc_now_delinq'].values[0])
          df.set_value(index, 'tot_coll_amt', this['tot_coll_amt'].values[0])
          df.set_value(index, 'tot_cur_bal', this['tot_cur_bal'].values[0])
          df.set_value(index, 'open_acc_6m', this['open_acc_6m'].values[0])
          df.set_value(index, 'open_act_il', this['open_act_il'].values[0])
          df.set_value(index, 'open_il_12m', this['open_il_12m'].values[0])
          df.set_value(index, 'open_il_24m', this['open_il_24m'].values[0])
          df.set_value(index, 'mths_since_rcnt_il', this['mths_since_rcnt_il'].values[0])
          df.set_value(index, 'total_bal_il', this['total_bal_il'].values[0])
          df.set_value(index, 'il_util', this['il_util'].values[0])
          df.set_value(index, 'open_rv_12m', this['open_rv_12m'].values[0])
          df.set_value(index, 'open_rv_24m', this['open_rv_24m'].values[0])
          df.set_value(index, 'max_bal_bc', this['max_bal_bc'].values[0])
          df.set_value(index, 'all_util', this['all_util'].values[0])
          df.set_value(index, 'total_rev_hi_lim', this['total_rev_hi_lim'].values[0])
          df.set_value(index, 'inq_fi', this['inq_fi'].values[0])
          df.set_value(index, 'total_cu_tl', this['total_cu_tl'].values[0])
          df.set_value(index, 'inq_last_12m', this['inq_last_12m'].values[0])
          df.set_value(index, 'acc_open_past_24mths', this['acc_open_past_24mths'].values[0])
          df.set_value(index, 'avg_cur_bal', this['avg_cur_bal'].values[0])
          df.set_value(index, 'bc_open_to_buy', this['bc_open_to_buy'].values[0])
          df.set_value(index, 'bc_util', this['bc_util'].values[0])
          df.set_value(index, 'chargeoff_within_12_mths', this['chargeoff_within_12_mths'].values[0])
          df.set_value(index, 'delinq_amnt', this['delinq_amnt'].values[0])
          df.set_value(index, 'mo_sin_old_il_acct', this['mo_sin_old_il_acct'].values[0])
          df.set_value(index, 'mo_sin_old_rev_tl_op', this['mo_sin_old_rev_tl_op'].values[0])
          df.set_value(index, 'mo_sin_rcnt_rev_tl_op', this['mo_sin_rcnt_rev_tl_op'].values[0])
          df.set_value(index, 'mo_sin_rcnt_tl', this['mo_sin_rcnt_tl'].values[0])
          df.set_value(index, 'mort_acc', this['mort_acc'].values[0])
          df.set_value(index, 'mths_since_recent_bc', this['mths_since_recent_bc'].values[0])
          df.set_value(index, 'mths_since_recent_bc_dlq', this['mths_since_recent_bc_dlq'].values[0])
          df.set_value(index, 'mths_since_recent_inq', this['mths_since_recent_inq'].values[0])
          df.set_value(index, 'mths_since_recent_revol_delinq', this['mths_since_recent_revol_delinq'].values[0])
          df.set_value(index, 'num_accts_ever_120_pd', this['num_accts_ever_120_pd'].values[0])
          df.set_value(index, 'num_actv_bc_tl', this['num_actv_bc_tl'].values[0])
          df.set_value(index, 'num_actv_rev_tl', this['num_actv_rev_tl'].values[0])
          df.set_value(index, 'num_bc_sats', this['num_bc_sats'].values[0])
          df.set_value(index, 'num_bc_tl', this['num_bc_tl'].values[0])
          df.set_value(index, 'num_il_tl', this['num_il_tl'].values[0])
          df.set_value(index, 'num_op_rev_tl', this['num_op_rev_tl'].values[0])
          df.set_value(index, 'num_rev_accts', this['num_rev_accts'].values[0])
          df.set_value(index, 'num_rev_tl_bal_gt_0', this['num_rev_tl_bal_gt_0'].values[0])
          df.set_value(index, 'num_sats', this['num_sats'].values[0])
          df.set_value(index, 'num_tl_120dpd_2m', this['num_tl_120dpd_2m'].values[0])
          df.set_value(index, 'num_tl_30dpd', this['num_tl_30dpd'].values[0])
          df.set_value(index, 'num_tl_90g_dpd_24m', this['num_tl_90g_dpd_24m'].values[0])
          df.set_value(index, 'num_tl_op_past_12m', this['num_tl_op_past_12m'].values[0])
          df.set_value(index, 'pct_tl_nvr_dlq', this['pct_tl_nvr_dlq'].values[0])
          df.set_value(index, 'percent_bc_gt_75', this['percent_bc_gt_75'].values[0])
          df.set_value(index, 'pub_rec_bankruptcies', this['pub_rec_bankruptcies'].values[0])
          df.set_value(index, 'tax_liens', this['tax_liens'].values[0])
          df.set_value(index, 'tot_hi_cred_lim', this['tot_hi_cred_lim'].values[0])
          df.set_value(index, 'total_bal_ex_mort', this['total_bal_ex_mort'].values[0])
          df.set_value(index, 'total_bc_limit', this['total_bc_limit'].values[0])
          df.set_value(index, 'total_il_high_credit_limit', this['total_il_high_credit_limit'].values[0])
          df.set_value(index, 'revol_bal_joint', this['revol_bal_joint'].values[0])
          df.set_value(index, 'sec_app_earliest_cr_line', this['sec_app_earliest_cr_line'].values[0])
          df.set_value(index, 'sec_app_inq_last_6mths', this['sec_app_inq_last_6mths'].values[0])
          df.set_value(index, 'sec_app_mort_acc', this['sec_app_mort_acc'].values[0])
          df.set_value(index, 'sec_app_open_acc', this['sec_app_open_acc'].values[0])
          df.set_value(index, 'sec_app_revol_util', this['sec_app_revol_util'].values[0])
          df.set_value(index, 'sec_app_open_act_il', this['sec_app_open_act_il'].values[0])
          df.set_value(index, 'sec_app_num_rev_accts', this['sec_app_num_rev_accts'].values[0])
          df.set_value(index, 'sec_app_chargeoff_within_12_mths', this['sec_app_chargeoff_within_12_mths'].values[0])
          df.set_value(index, 'sec_app_collections_12_mths_ex_med', this['sec_app_collections_12_mths_ex_med'].values[0])
          df.set_value(index, 'sec_app_mths_since_last_major_derog', this['sec_app_mths_since_last_major_derog'].values[0])
          df.set_value(index, 'hardship_flag', this['hardship_flag'].values[0])
          df.set_value(index, 'hardship_type', this['hardship_type'].values[0])
          df.set_value(index, 'hardship_reason', this['hardship_reason'].values[0])
          df.set_value(index, 'hardship_status', this['hardship_status'].values[0])
          df.set_value(index, 'deferral_term', this['deferral_term'].values[0])
          df.set_value(index, 'hardship_amount', this['hardship_amount'].values[0])
          df.set_value(index, 'hardship_start_date', this['hardship_start_date'].values[0])
          df.set_value(index, 'hardship_end_date', this['hardship_end_date'].values[0])
          df.set_value(index, 'payment_plan_start_date', this['payment_plan_start_date'].values[0])
          df.set_value(index, 'hardship_length', this['hardship_length'].values[0])
          df.set_value(index, 'hardship_dpd', this['hardship_dpd'].values[0])
          df.set_value(index, 'hardship_loan_status', this['hardship_loan_status'].values[0])
          df.set_value(index, 'orig_projected_additional_accrued_interest', this['orig_projected_additional_accrued_interest'].values[0])
          df.set_value(index, 'hardship_payoff_balance_amount', this['hardship_payoff_balance_amount'].values[0])
          df.set_value(index, 'hardship_last_payment_amount', this['hardship_last_payment_amount'].values[0])
          df.set_value(index, 'debt_settlement_flag', this['debt_settlement_flag'].values[0])
          df.set_value(index, 'debt_settlement_flag_date', this['debt_settlement_flag_date'].values[0])
          df.set_value(index, 'settlement_status', this['settlement_status'].values[0])
          df.set_value(index, 'settlement_date', this['settlement_date'].values[0])
          df.set_value(index, 'settlement_amount', this['settlement_amount'].values[0])
          df.set_value(index, 'settlement_percentage', this['settlement_percentage'].values[0])
          df.set_value(index, 'settlement_term', this['settlement_term'].values[0])
df.to_pickle("dv01extended.pkl")

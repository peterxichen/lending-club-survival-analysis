# LendingClubHazards
Modeling default versus prepayment risk via logistic regression and Cox proportional hazards.

Abstract
----------------------------------------------

The main focus of our study is examining the difference in statistical modeling approaches when predicting
for loan default versus prepayment as well as the interpretation of the features used to inform these models.
A loan default is the failure to repay a loan by the borrower according to agreed upon terms. A loan
prepayment is the early payment of a loan by the borrower, typically as a result of lower interest rates
allowing for favorable refinancing. Prepayment reflects a borrower's financial capacity to pay off a loan or
ability to refinance it at a more attractive level. On the other hand, default represents lack of capacity (or
willingness/wherewithal) to pay. Using dv01 labels of loan status, we assume defaulted loans to be indicated
as 'Charged Off' and 'Sold - Debt Sale', and prepaid loans to be indicated as 'Paid Off' in their loan statuses.
In theory, we would expect borrowers that prepay to be have high debt servicing capacity/be good
borrowers in order to be able to prepay. For instance, we would expect this group to thus have higher
incomes, and a lower Debt to Income Ratio. On the other hand, borrowers that default will be likely to
have lower incomes, and higher Debt to Income Ratios. Some variables may have less explainability due
to correlated externalities. For example, it is unclear whether groups that prepay will have lower or higher
credit inquiries than the average borrower, because although having a large number of inquires is a sign of
someone with low credit/who was rejected multiple times, borrowers who shop around (and thus are likely
to prepay if they find a better deal) will also tend to have a higher number of inquiries.
We study these factors, first using a simple binary classification framework using the logistic regression
Model, and then using a hazard rate approach via the cox-proportional hazards model.

Authors
----------------------------------------------

- Peter Chen
- Sarang Gupta
- Ally Bouchard

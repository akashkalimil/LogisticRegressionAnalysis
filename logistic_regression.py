import pandas as pd
import statsmodels.api as sm
import math as math
import random



data=pd.read_csv("loansData_clean.csv")


data["IR_TF"]=(data["Interest.Rate"]<.12)
data["Intercept"]=1.0


ind_vars=["Amount.Requested","FICO.Range","Intercept"]

logit = sm.Logit(data['IR_TF'], data[ind_vars])
result = logit.fit()
coeff = result.params
print(coeff)

fscore =raw_input("FICO Score : ")
lamount =raw_input("Loan Amount: ")


print ""


def logistic_function(fscore,lamount,coeff):
	#function p(x)= 1/ (1 + e^(intercept + a1 * x1 -a2 *x2))
	p = 1 / ( 1+ math.e**( float(coeff[2])  + float(coeff[0]) * float(lamount) + float(coeff[1]) * float(fscore) ) )
	return p        

def pred(p):
	r = random.randint(1,10)
	print r
	if (r <= p*10 ):
		print "Loan Approved"
	else:
		print "Loan Denied"

prediction = logistic_function(fscore,lamount,coeff)
print "p value: ",prediction
print "Prediction: ",pred(prediction)
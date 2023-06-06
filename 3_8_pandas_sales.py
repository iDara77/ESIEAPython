import pandas as pd
import matplotlib.pyplot as plt
import os

CWD = os.path.dirname(os.path.realpath(__file__))

calls = pd.read_csv(CWD+"/sales_calls.csv")
revenue = pd.read_csv(CWD+"/sales_revenue.csv")
calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls

byMember = calls_revenue[['Team member', 'Month', 'Amount']].groupby(['Team member']).sum()
byMemberMonth = calls_revenue[['Team member', 'Month', 'Calls']].groupby(['Team member','Month']).sum()

byMonth = calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum()
byMonth['Call_Amount'] = byMonth.Amount/byMonth.Calls
byMonth['Call_Amount_Median'] = calls_revenue[['Month', 'Call_Amount']].groupby(['Month']).median()

print()
plt.figure(1)
plt.subplot(221)
plt.bar(byMember.index.values, byMember.Amount)
plt.subplot(222)
plt.plot(byMonth.Calls,'bo')
plt.plot(byMonth.Call_Amount, 'g^')
plt.plot(byMonth.Call_Amount_Median, 'r--')
# plt.figure(2)
plt.subplot(223)
plt.axis([0,5,0,150])
plt.plot(calls_revenue[calls_revenue["Team member"] == "Ali"].groupby('Month').sum().Calls,'bo')
plt.plot(calls_revenue[calls_revenue["Team member"] == "Ana"].groupby('Month').sum().Calls,'g^')
plt.plot(calls_revenue[calls_revenue["Team member"] == "Jorge"].groupby('Month').sum().Calls,'rs')
plt.show()




# print(calls_revenue)
# print(calls_revenue[calls_revenue.Month == 1])
# print(calls_revenue[calls_revenue.Calls>100])
# print(calls_revenue[calls_revenue.Amount/calls_revenue.Calls>500])
# calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls
# print(calls_revenue)
# print(calls_revenue.Calls.sum())
# print(calls_revenue.Calls.mean())
# print(calls_revenue.Calls.median())
# print(calls_revenue.Calls.max())
# print(calls_revenue.Calls.min())
# print(calls_revenue.Call_Amount.median())
# print(calls_revenue[calls_revenue.Call_Amount >= calls_revenue.Call_Amount.median()])
# print(calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum())
# print(calls_revenue[['Territory', 'Calls', 'Amount']].groupby(['Territory']).sum())

# byTerritory = calls_revenue[['Territory', 'Calls', 'Amount']].groupby(['Territory']).sum()
# byMonth = calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum()
# plt.plot(byTerritory.Calls,'ro')
# plt.plot(byMonth.Calls, 'g^')
# plt.ylabel("Somme des appels")
# plt.show()
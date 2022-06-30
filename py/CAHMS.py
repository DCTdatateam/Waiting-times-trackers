#importing the libraries needed
import pandas as pd

#identifying the source data
#https://www.opendata.nhs.scot/dataset/child-and-adolescent-mental-health-waiting-times
patientsseen = pd.read_csv("https://www.opendata.nhs.scot/dataset/f9bab568-501e-49d3-a0a4-0b9a7578b0de/resource/7a2fe10d-1339-41c1-a2f2-a469644fd619/download/camhs-adjusted-patients-seen.csv")
patientswaiting = pd.read_csv("https://www.opendata.nhs.scot/dataset/f9bab568-501e-49d3-a0a4-0b9a7578b0de/resource/d43cae98-a620-4f24-a02f-a6451c297478/download/camhs-adjusted-patients-waiting.csv")
referrals = pd.read_csv("https://www.opendata.nhs.scot/dataset/f9bab568-501e-49d3-a0a4-0b9a7578b0de/resource/d31d8e7c-fbcb-4e4b-a6a1-3b9c4f3b14a0/download/camhs-referrals.csv")
HBcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#changing the max column output because there's quite a lot of columns in the original merges
pd.set_option('display.max_columns', 100)

#merging datasets
merge1= pd.merge(patientsseen, patientswaiting, how='outer')
merge2= pd.merge(merge1, referrals, how='outer')

#final merge, CAHMSdata is the sheet with the final merge
CAHMSdata= pd.merge(merge2, HBcodes, how='outer')

#deleting columns that aren't necessary for the visualisation (aka they're empty)
#Overwrites previous CAHMS data
CAHMSdata1= CAHMSdata.drop(columns=['TotalPatientsSeenQF', 'NumberOfPatientsSeen0To18WeeksQF', 'NumberOfPatientsSeen19To35WeeksQF', 'NumberOfPatientsSeen36To52WeeksQF', 'NumberOfPatientsSeenOver52WeeksQF', 'MedianWeeksPatientsSeenQF', '90thPercentileWeeksPatientsSeenQF', 'TotalPatientsWaitingQF', 'NumberOfPatientsWaiting0To18WeeksQF', 'NumberOfPatientsWaiting19To35WeeksQF', 'NumberOfPatientsWaiting36To52WeeksQF', 'NumberOfPatientsWaitingOver52WeeksQF', 'ReferralsAcceptedQF', 'ReferralsReceivedQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])

#sorting the month column into a date format that is flourish compatible for the data visualisation
from datetime import datetime
CAHMSdata1['Month'] = pd.to_datetime(CAHMSdata1['Month'], format='%Y%m').dt.strftime('%d/%m/%y')

#renaming columns for flourish visualisation
CAHMSdata2 = CAHMSdata1.rename(columns={'TotalPatientsSeen': 'Total patients seen', 'NumberOfPatientsSeen0To18Weeks': 'Number of patients seen in 0 to 18 weeks','NumberOfPatientsSeen19To35Weeks': 'Number of patients seen in 19 to 35 weeks', 'NumberOfPatientsSeen36To52Weeks': 'Number of patients seen in 36 to 52 weeks', 'NumberOfPatientsSeenOver52Weeks': 'Number of patients seen in over 52 weeks', 'MedianWeeksPatientsSeen': 'Median number of weeks patients seen in', 'TotalPatientsWaiting': 'Total number of patients waiting', 'NumberOfPatientsWaiting0To18Weeks': 'Number of patients waiting from 0 to 18 weeks', 'NumberOfPatientsWaiting19To35Weeks': 'Number of patients waiting between 19 and 35 weeks', 'NumberOfPatientsWaiting36To52Weeks': 'Number of patients waiting between 36 and 52 weeks', 'NumberOfPatientsWaitingOver52Weeks': 'Number of patients waiting more than 52 weeks', 'ReferralsAccepted': 'Number of referrals accepted', 'ReferralsReceived': 'Number of referrals received', 'HBName': 'Health board'}, inplace=True)

#making new datasets for charts
PatientsSeenFinal= CAHMSdata1.drop(columns=['Number of patients waiting from 0 to 18 weeks', 'Number of patients waiting between 19 and 35 weeks', 'Number of patients waiting between 36 and 52 weeks', 'Number of patients waiting more than 52 weeks', 'Number of referrals accepted','Number of referrals received' ])
PatientsWaitingFinal= CAHMSdata1.drop(columns=['Total patients seen', 'Number of patients seen in 0 to 18 weeks', 'Number of patients seen in 19 to 35 weeks', 'Number of patients seen in 36 to 52 weeks', 'Number of patients seen in over 52 weeks', 'Median number of weeks patients seen in', '90thPercentileWeeksPatientsSeen', 'Number of referrals accepted','Number of referrals received' ])
ReferralsFinal= CAHMSdata1.drop(columns=['Total patients seen', 'Number of patients waiting between 19 and 35 weeks', 'Number of patients seen in 0 to 18 weeks', 'Number of patients seen in 19 to 35 weeks', 'Number of patients seen in 36 to 52 weeks', 'Number of patients seen in over 52 weeks', 'Median number of weeks patients seen in', '90thPercentileWeeksPatientsSeen', 'Number of patients waiting from 0 to 18 weeks', 'Number of patients waiting between 19 and 35 weeks', 'Number of patients waiting between 36 and 52 weeks', 'Number of patients waiting more than 52 weeks'])

Seenmerged= PatientsSeenFinal['Number of patients seen in 19 to 35 weeks']+PatientsSeenFinal['Number of patients seen in 36 to 52 weeks']+PatientsSeenFinal['Number of patients seen in over 52 weeks']
PatientsSeenFinal['Number of patients seen in over 18 weeks'] = Seenmerged

Waitingmerged= PatientsWaitingFinal['Number of patients waiting between 19 and 35 weeks']+PatientsWaitingFinal['Number of patients waiting between 36 and 52 weeks']+PatientsWaitingFinal['Number of patients waiting more than 52 weeks']
PatientsWaitingFinal['Number of patients waiting over 18 weeks'] = Waitingmerged


#saving the final merged dataset with all the improvements as a csv - there's three because there's three different charts linked to this -decided after coding!
PatientsSeenFinal.to_csv(r'data/PatientsSeenFinal.csv')
PatientsWaitingFinal.to_csv(r'data/PatientsWaitingFinal.csv')
ReferralsFinal.to_csv(r'data/ReferralsFinal.csv')

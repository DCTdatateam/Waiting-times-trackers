#importing libraries needed
import pandas as pd

#identifying the source data
#source - https://www.opendata.nhs.scot/dataset/ivf-waiting-times-in-scotland
IVFwaitingtimes = pd.read_csv("https://www.opendata.nhs.scot/dataset/dd6bf01f-ff9c-4aaa-801b-75d1a933ecb1/resource/2cf6c335-dc7c-4773-b317-cf72293917c4/download/waiting-by-ivf-centre-month.csv")
HBcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")
IVFwaitingtimesbyreferringboard = pd.read_csv("https://www.opendata.nhs.scot/dataset/dd6bf01f-ff9c-4aaa-801b-75d1a933ecb1/resource/c9f6ee36-0cda-410a-95a5-3d6677b651b2/download/waiting-by-referring-board-month.csv")
IVFreferrals = pd.read_csv("https://www.opendata.nhs.scot/dataset/dd6bf01f-ff9c-4aaa-801b-75d1a933ecb1/resource/a4c56e8e-5dbd-481b-8cee-808d06f2bf18/download/referrals-by-ivf-centre-quarter.csv")
IVFreferralsbyboard= pd.read_csv("https://www.opendata.nhs.scot/dataset/dd6bf01f-ff9c-4aaa-801b-75d1a933ecb1/resource/dc378b1b-34c7-43a5-a05f-a478f73f48bd/download/referrals-by-referring-board-quarter.csv")

#merge
merge1= pd.merge(IVFwaitingtimesbyreferringboard, HBcodes, left_on='HBR', right_on='HB')
merge2= pd.merge(IVFreferralsbyboard, HBcodes, left_on='HBR', right_on='HB')

#removing unneeded columns from the dataset
IVF= IVFwaitingtimes.drop(columns=['PatientsWaitingQF', 'NumberWaitingZeroTo13WeeksQF', 'NumberWaiting14To26WeeksQF', 'NumberWaiting27To39WeeksQF', 'NumberWaiting40To52WeeksQF', 'NumberWaitingOver52WeeksQF', 'NumberWaitingWithin52WeeksQF', 'NumberWaitingZeroTo13WeeksPcQF', 'NumberWaiting14To26WeeksPcQF', 'NumberWaiting27To39WeeksPcQF', 'NumberWaiting40To52WeeksPcQF', 'NumberWaitingOver52WeeksPcQF', 'NumberWaitingWithin52WeeksPcQF'])
IVFboard = merge1.drop(columns=['HBRQF','PatientsWaitingQF', 'NumberWaitingZeroTo13WeeksQF', 'NumberWaiting14To26WeeksQF', 'NumberWaiting27To39WeeksQF', 'NumberWaiting40To52WeeksQF', 'NumberWaitingOver52WeeksQF', 'NumberWaitingWithin52WeeksQF', 'NumberWaitingZeroTo13WeeksPcQF', 'NumberWaiting14To26WeeksPcQF', 'NumberWaiting27To39WeeksPcQF', 'NumberWaiting40To52WeeksPcQF', 'NumberWaitingOver52WeeksPcQF', 'NumberWaitingWithin52WeeksPcQF'])

#changing the time in dataset to something flourish will recognise
from datetime import datetime
IVF['Month'] = pd.to_datetime(IVF['Month'], format='%Y%m').dt.strftime('%d/%m/%y')
IVFboard['Month'] = pd.to_datetime(IVFboard['Month'], format='%Y%m').dt.strftime('%d/%m/%y')


#renaming columns for flourish visualisation
IVF2 = IVF.rename(columns={'IVFCentre': 'IVF centre', 'PatientsWaiting': 'Patients waiting', 'NumberWaitingZeroTo13Weeks': 'Number of patients waiting 0 to 13 weeks','NumberWaiting14To26Weeks': 'Number of patients waiting 14 to 26 weeks', 'NumberWaiting27To39Weeks': 'Number of patients waiting 27 to 39 weeks', 'NumberWaiting40To52Weeks': 'Number of patients waiting 40 to 52 weeks', 'NumberWaitingOver52Weeks': 'Number waiting over 52 weeks', 'MedianWeeksPatientsSeen': 'Median number of weeks patients seen in', 'TotalPatientsWaiting': 'Total number of patients waiting', 'NumberOfPatientsWaiting0To18Weeks': 'Number of patients waiting from 0 to 18 weeks', 'NumberOfPatientsWaiting19To35Weeks': 'Number of patients waiting between 19 and 35 weeks', 'NumberOfPatientsWaiting36To52Weeks': 'Number of patients waiting between 36 and 52 weeks', 'NumberOfPatientsWaitingOver52Weeks': 'Number of patients waiting more than 52 weeks', 'NumberWaitingWithin52Weeks': 'Number waiting within 52 weeks', 'NumberWaitingZeroTo13WeeksPc': 'Percentage of people waiting 0 to 13 weeks', 'NumberWaiting14To26WeeksPc': 'Percentage of people waiting 14 to 26 weeks', 'NumberWaiting27To39WeeksPc': 'Percentage of people waiting 27 to 39 weeks', 'NumberWaiting40To52WeeksPc': 'Percentage of people waiting 40 to 52 weeks', 'NumberWaitingOver52WeeksPc': 'Percentage of people waiting over 52 weeks', 'NumberWaitingWithin52WeeksPc': 'Percentage of people waiting within 52 weeks', 'NumberWaitingWithin52WeeksPc': 'Percentage waiting within 52 weeks'}, inplace=True)
IVFboard2 = IVFboard.rename(columns={'PatientsWaiting': 'Patients waiting', 'NumberWaitingZeroTo13Weeks': 'Number waiting between 0 and 13 weeks', 'NumberWaiting14To26Weeks': 'Number of people waiting betweeen 14 and 26 weeks', 'NumberWaiting27To39Weeks': 'Number waiting between 27 and 39 weeks', 'NumberWaiting40To52Weeks': 'Number waiting 40 to 52 weeks', 'NumberWaitingOver52Weeks': 'Number waiting more than 52 weeks', 'NumberWaitingWithin52Weeks': 'Number waiting within 52 weeks', 'NumberWaitingZeroTo13WeeksPc': 'Percentage waiting between 0 and 13 weeks', 'NumberWaiting14To26WeeksPc': 'Percentage waiting 14 to 26 weeks', 'NumberWaiting27To39WeeksPc': 'Percentage waiting 27 to 39 weeks', 'NumberWaiting40To52WeeksPc': 'Percentage waiting 40 to 52 weeks', 'NumberWaitingOver52WeeksPc': 'Percentage waiting over 52 weeks', 'NumberWaitingWithin52WeeksPc': 'Percentage waiting within 52 weeks'}, inplace=True)
IVFreferrals1= IVFreferrals.rename(columns={'IVFCentre': 'IVF centre', 'NumberOfReferrals': 'Number of referrals'})
IVFreferralsbyboard1= merge2.rename(columns={'HBName': 'Health board', 'NumberOfReferrals': 'Number of referrals'})

#saving dataset to csv
IVF.to_csv(r'data/IVF.csv')
IVFboard.to_csv(r'data/IVFbyboard.csv')
IVFreferrals1.to_csv(r'data/IVFreferrals.csv')
IVFreferralsbyboard1.to_csv(r'data/IVFreferralsbyboard.csv')

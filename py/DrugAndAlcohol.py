#importing the libraries needed
import pandas as pd

#identifying the source data
#source: https://www.opendata.nhs.scot/dataset/drug-and-alcohol-treatment-waiting-times
waitbynhsboard= pd.read_csv("https://www.opendata.nhs.scot/dataset/31597116-4a57-4c6c-a250-3ae8baa36864/resource/ca67ac5b-085c-412c-947d-2a1fa2ec646b/download/20220405-all-quarters-ongoing-hb.csv")
waitbyAandD= pd.read_csv("https://www.opendata.nhs.scot/dataset/31597116-4a57-4c6c-a250-3ae8baa36864/resource/691d7aea-86ea-40ea-8d8e-5afe6bbed25c/download/20220405-all-quarters-ongoing-adp.csv")
waitbyprison= pd.read_csv("https://www.opendata.nhs.scot/dataset/31597116-4a57-4c6c-a250-3ae8baa36864/resource/a5595172-90d7-4c3b-934f-b5dd0effd38d/download/20220405-all-quarters-ongoing-prisons.csv")
HBnames= pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#changing the max column output
pd.set_option('display.max_columns', 100)

#merging datasets
merge1= pd.merge(waitbynhsboard, waitbyAandD, how='outer')
merge2= pd.merge(merge1, waitbyprison, how='outer')

merge3= pd.merge(waitbynhsboard, HBnames, left_on='HBT', right_on='HB')
merge4= pd.merge(waitbyAandD, HBnames, left_on='HBT', right_on='HB')
merge5= pd.merge(waitbyprison, HBnames, left_on='HBT', right_on='HB')

#creating a new column to merge 
ADPmerged= merge4['PercentWaitOver3WeeksAndUpTo4Weeks']+merge4['PercentWaitOver4WeeksAndUpTo5Weeks']+merge4['PercentWaitOver5WeeksAndUpTo6Weeks']+merge4['PercentWaitOver6WeeksAndUpTo8Weeks']+ merge4['PercentWaitOver8WeeksAndUpTo12Weeks']+merge4['PercentWaitOver12WeeksAndUpTo16Weeks']+merge4['PercentWaitOver16WeeksAndUpTo20Weeks']+merge4['PercentWaitOver20Weeks']
merge4['Percent wait over 3 weeks'] = ADPmerged

ADPmerged1= merge4['PercentWaitUpTo1Week']+merge4['PercentWaitOver1WeekAndUpTo2Weeks']+merge4['PercentWaitOver2WeeksAndUpTo3Weeks']
merge4['Percent wait within 3 week target'] = ADPmerged1

NHSmerged = merge3['PercentWaitOver3WeeksAndUpTo4Weeks']+merge3['PercentWaitOver4WeeksAndUpTo5Weeks']+merge3['PercentWaitOver5WeeksAndUpTo6Weeks']+merge3['PercentWaitOver6WeeksAndUpTo8Weeks']+ merge3['PercentWaitOver8WeeksAndUpTo12Weeks']+merge3['PercentWaitOver12WeeksAndUpTo16Weeks']+merge3['PercentWaitOver16WeeksAndUpTo20Weeks']+merge3['PercentWaitOver20Weeks']
merge3['Percent wait over 3 weeks'] = NHSmerged

NHSmerged1= merge3['PercentWaitUpTo1Week']+merge3['PercentWaitOver1WeekAndUpTo2Weeks']+merge3['PercentWaitOver2WeeksAndUpTo3Weeks']
merge3['Percent wait within 3 week target'] = NHSmerged1


Prisonsmerged = merge5['PercentWaitOver3WeeksAndUpTo4Weeks']+merge5['PercentWaitOver4WeeksAndUpTo5Weeks']+merge5['PercentWaitOver5WeeksAndUpTo6Weeks']+merge5['PercentWaitOver6WeeksAndUpTo8Weeks']+ merge5['PercentWaitOver8WeeksAndUpTo12Weeks']+merge5['PercentWaitOver12WeeksAndUpTo16Weeks']+merge5['PercentWaitOver16WeeksAndUpTo20Weeks']+merge5['PercentWaitOver20Weeks']
merge5['Percent wait over 3 weeks'] = Prisonsmerged

Prisonsmerged1= merge5['PercentWaitUpTo1Week']+merge5['PercentWaitOver1WeekAndUpTo2Weeks']+merge5['PercentWaitOver2WeeksAndUpTo3Weeks']
merge5['Percent wait within 3 week target'] = Prisonsmerged1

#dropping values from the ADP columns for both ADP and prisons csv- All ADP selection as not needed for chart
merge4= merge4[merge4.ADP !='Ayrshire & Arran  - All ADPs']
merge4= merge4[merge4.ADP !='Borders  - All ADPs']
merge4= merge4[merge4.ADP !='Dumfries & Galloway  - All ADPs']
merge4= merge4[merge4.ADP !='Fife  - All ADPs']
merge4= merge4[merge4.ADP !='Forth Valley  - All ADPs']
merge4= merge4[merge4.ADP !='Grampian  - All ADPs']
merge4= merge4[merge4.ADP !='Greater Glasgow & Clyde  - All ADPs']
merge4= merge4[merge4.ADP !='Highland  - All ADPs']
merge4= merge4[merge4.ADP !='Lanarkshire  - All ADPs']
merge4= merge4[merge4.ADP !='Lothian  - All ADPs']
merge4= merge4[merge4.ADP !='Orkney  - All ADPs']
merge4= merge4[merge4.ADP !='Tayside  - All ADPs']
merge4= merge4[merge4.ADP !='Western Isles  - All ADPs']

merge5= merge5[merge5.ADP !='Ayrshire & Arran  - All ADPs']
merge5= merge5[merge5.ADP !='Borders  - All ADPs']
merge5= merge5[merge5.ADP !='Dumfries & Galloway  - All ADPs']
merge5= merge5[merge5.ADP !='Fife  - All ADPs']
merge5= merge5[merge5.ADP !='Forth Valley  - All ADPs']
merge5= merge5[merge5.ADP !='Grampian  - All ADPs']
merge5= merge5[merge5.ADP !='Greater Glasgow & Clyde  - All ADPs']
merge5= merge5[merge5.ADP !='Highland  - All ADPs']
merge5= merge5[merge5.ADP !='Lanarkshire  - All ADPs']
merge5= merge5[merge5.ADP !='Lothian  - All ADPs']
merge5= merge5[merge5.ADP !='Orkney  - All ADPs']
merge5= merge5[merge5.ADP !='Tayside  - All ADPs']
merge5= merge5[merge5.ADP !='Western Isles  - All ADPs']

#renaming columns for flourish popups
merge4= merge4.rename(columns={'TotalNumberOfReferrals': 'Total number of referrals', 'SubstanceType': 'Substance type', 'TotalNumberOfReferrals': 'Total number of referrals', 'PercentWaitUpTo1Week': 'Percent waiting up to a week', 'PercentWaitOver1WeekAndUpTo2Weeks': 'Percent waiting between 1 and 2 weeks', 'PercentWaitOver2WeeksAndUpTo3Weeks': 'Percent waiting between 2 and 3 weeks', 'PercentWaitOver3WeeksAndUpTo4Weeks': 'Percent waiting between 3 and 4 weeks', 'PercentWaitOver4WeeksAndUpTo5Weeks': 'Percent waiting between 4 and 5 weeks', 'PercentWaitOver5WeeksAndUpTo6Weeks': 'Percent waiting between 5 and 6 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver8WeeksAndUpTo12Weeks': 'Percent waiting between 8 and 12 weeks', 'PercentWaitOver12WeeksAndUpTo16Weeks': 'Percent waiting between 12 and 16 weeks', 'PercentWaitOver16WeeksAndUpTo20Weeks': 'Percent waiting between 16 and 20 weeks', 'PercentWaitOver20Weeks': 'Percent waiting over 20 weeks', 'HBName': 'Health board'})
merge3= merge3.rename(columns={'TotalNumberOfReferrals': 'Total number of referrals', 'SubstanceType': 'Substance type', 'TotalNumberOfReferrals': 'Total number of referrals', 'PercentWaitUpTo1Week': 'Percent waiting up to a week', 'PercentWaitOver1WeekAndUpTo2Weeks': 'Percent waiting between 1 and 2 weeks', 'PercentWaitOver2WeeksAndUpTo3Weeks': 'Percent waiting between 2 and 3 weeks', 'PercentWaitOver3WeeksAndUpTo4Weeks': 'Percent waiting between 3 and 4 weeks', 'PercentWaitOver4WeeksAndUpTo5Weeks': 'Percent waiting between 4 and 5 weeks', 'PercentWaitOver5WeeksAndUpTo6Weeks': 'Percent waiting between 5 and 6 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver8WeeksAndUpTo12Weeks': 'Percent waiting between 8 and 12 weeks', 'PercentWaitOver12WeeksAndUpTo16Weeks': 'Percent waiting between 12 and 16 weeks', 'PercentWaitOver16WeeksAndUpTo20Weeks': 'Percent waiting between 16 and 20 weeks', 'PercentWaitOver20Weeks': 'Percent waiting over 20 weeks', 'HBName': 'Health board'})
merge5= merge5.rename(columns={'TotalNumberOfReferrals': 'Total number of referrals', 'SubstanceType': 'Substance type', 'TotalNumberOfReferrals': 'Total number of referrals', 'PercentWaitUpTo1Week': 'Percent waiting up to a week', 'PercentWaitOver1WeekAndUpTo2Weeks': 'Percent waiting between 1 and 2 weeks', 'PercentWaitOver2WeeksAndUpTo3Weeks': 'Percent waiting between 2 and 3 weeks', 'PercentWaitOver3WeeksAndUpTo4Weeks': 'Percent waiting between 3 and 4 weeks', 'PercentWaitOver4WeeksAndUpTo5Weeks': 'Percent waiting between 4 and 5 weeks', 'PercentWaitOver5WeeksAndUpTo6Weeks': 'Percent waiting between 5 and 6 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver6WeeksAndUpTo8Weeks': 'Percent waiting between 6 and 8 weeks', 'PercentWaitOver8WeeksAndUpTo12Weeks': 'Percent waiting between 8 and 12 weeks', 'PercentWaitOver12WeeksAndUpTo16Weeks': 'Percent waiting between 12 and 16 weeks', 'PercentWaitOver16WeeksAndUpTo20Weeks': 'Percent waiting between 16 and 20 weeks', 'PercentWaitOver20Weeks': 'Percent waiting over 20 weeks', 'HBName': 'Health board'})


#saving the final dataset as a csv
merge2.to_csv(r'data/DandAtreatment.csv')
merge3.to_csv(r'data/DandANHS.csv')
merge4.to_csv(r'data/DandAADP.csv')
merge5.to_csv(r'data/DandAPrison.csv')

#importing the libraries needed
import pandas as pd

#identifying the source data
#source: https://www.opendata.nhs.scot/dataset/drug-and-alcohol-treatment-waiting-times
ongoingwaits= pd.read_csv("https://www.opendata.nhs.scot/dataset/2e085b14-3640-4c6a-aab3-b04476d60718/resource/abf54d64-88de-47d8-9c31-49a959abc164/download/ongoingwaits-30-06-2022.csv")

#renaming columns
ongoingwaits2= ongoingwaits.rename(columns={'HBName': 'Health board', 'ADPName': 'ADP', 'ServiceType': 'Service type', 'SubstanceType': 'Substance type', 'LDP_standard_waited_3_weeks_or_less': 'Percent waiting within 3 weeks', 'LDP_standard_waited_more_than_3_weeks': 'Percent waiting over 3 weeks', 'Median_length_of_wait': 'Median length of wait'})

#dropping unneeded columns
ongoingwaits3= ongoingwaits2.drop(columns=['HBQF', 'HBNameQF', 'ADPNameQF', 'SubstanceTypeQF', 'ServiceTypeQF'])

#filtering to remove percentage
ongoingwaits3= ongoingwaits3[ongoingwaits3['Measure']=='Number']

#dropping some values from ADP column
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Ayrshire & Arran ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Borders ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Dumfries & Galloway ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Fife ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Forth Valley ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Grampian ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Greater Glasgow & Clyde ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Highland ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Lanarkshire ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Lothian ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Orkney ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Shetland ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Tayside ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Western Isles ADPs']
ongoingwaits3= ongoingwaits3[ongoingwaits3.ADP !='All NHS Scotland ADPs']




#filtering so code can be used for different graphs
ongoingwaits_allservices= ongoingwaits3[ongoingwaits3['Service type']=='All services']
ongoingwaits_communityservices= ongoingwaits3[ongoingwaits3['Service type']=='Community-based service']
ongoingwaits_prisonservices= ongoingwaits3[ongoingwaits3['Service type']=='Prison-based service']

#saving the final dataset as a csv
ongoingwaits2.to_csv(r'data/DandA_Ongoingwaits.csv')
ongoingwaits_allservices.to_csv(r'data/DandA_allservices.csv')
ongoingwaits_communityservices.to_csv(r'data/DandA_communityservices.csv')
ongoingwaits_prisonservices.to_csv(r'data/DandA_prisonservices.csv')

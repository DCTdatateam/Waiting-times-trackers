import pandas as pd

patientswaiting= pd.read_csv("https://www.opendata.nhs.scot/dataset/959f2341-ca34-428c-8abb-b925a18fc0c7/resource/eff86139-89de-4169-83d5-7b5cec2ed3e9/download/open_data_ahp_msk_waiting_december2021.csv")
HBcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")
patientsseen = pd.read_csv("https://www.opendata.nhs.scot/dataset/959f2341-ca34-428c-8abb-b925a18fc0c7/resource/6a403c6f-bff1-425e-918e-cd17a134227f/download/open_data_ahp_msk_seen_with_mats_december2021.csv")
HSCPcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/944765d7-d0d9-46a0-b377-abb3de51d08e/download/hscp16_hscp19.csv")

merge1= pd.merge(patientswaiting, HSCPcodes, how='outer')
#merge2= pd.merge(patientsseen, HBcodes, left_on='HBT', right_on='HB')

#merge1= merge1.drop(columns=['PatientsWaitingQF', 'NumberWaitingZeroToFourWeeksQF', 'NumberWaitingFiveToEightWeeksQF', 'NumberWaitingNineToTwelveWeeksQF', 'NumberWaitingThirteenToSixteenWeeksQF', 'NumberWaitingSixteenPlusWeeksQF', 'NumberWaitingFourPlusWeeksQF', 'NumberWaitingZeroToFourWeeksPcQF', 'NumberWaitingFiveToEightWeeksPcQF', 'NumberWaitingNineToTwelveWeeksPcQF', 'NumberWaitingThirteenToSixteenWeeksPcQF', 'NumberWaitingSixteenPlusWeeksPcQF', 'NumberWaitingFourPlusWeeksPcQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])
#merge2= merge2.drop(columns=['PatientsSeenQF', 'NumberWhoWaitedZeroToFourWeeksQF', 'NumberWhoWaitedFiveToEightWeeksQF', 'NumberWhoWaitedNineToTwelveWeeksQF', 'NumberWhoWaitedThirteenToSixteenWeeksQF', 'NumberWhoWaitedSixteenPlusWeeksQF', 'NumberWhoWaitedFourPlusWeeksQF', 'NumberWhoWaitedZeroToFourWeeksPcQF', 'NumberWhoWaitedFiveToEightWeeksPcQF', 'NumberWhoWaitedNineToTwelveWeeksPcQF', 'NumberWhoWaitedThirteenToSixteenWeeksPcQF', 'NumberWhoWaitedSixteenPlusWeeksPcQF', 'NumberWhoWaitedFourPlusWeeksPcQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])


Musculoskeletal= merge1.rename(columns={'PatientsWaiting': 'Number of patients waiting', 'NumberWhoWaitedZeroToFourWeeks': 'Number waiting 0 to 4 weeks', 'NumberWhoWaitedFiveToEightWeeks': 'Number waiting 5 to 8 weeks', 'NumberWhoWaitedNineToTwelveWeeks': 'Number waiting 9 to 12 weeks', 'NumberWhoWaitedThirteenToSixteenWeeks': 'Number waiting 13 to 16 weeks', 'NumberWhoWaitedSixteenPlusWeeks': 'Number waiting more than 16 weeks', 'NumberWhoWaitedFourPlusWeeks': 'Number waiting more than four weeks', 'NumberWhoWaitedZeroToFourWeeksPc': 'Percentage of people waiting between 0 and 4 weeks', 'NumberWhoWaitedFiveToEightWeeksPc': 'Percentage waiting between 5 and 8 weeks', 'NumberWhoWaitedNineToTwelveWeeksPc': 'Percentage waiting 9 to 12 weeks', 'NumberWhoWaitedThirteenToSixteenWeeksPc': 'Percentage waiting 13 to 16 weeks', 'NumberWhoWaitedSixteenPlusWeeksPc': 'Percentage waiting more than 16 weeks', 'NumberWhoWaitedFourPlusWeeksPc': 'Percentage waiting more than 4 weeks', 'HBName': 'Health board', 'HSCPName': 'Health and Social Care Partnership'})
#Musculoskeletal2= merge2.rename(columns={'PatientsSeen': 'Number of patients seen', 'NumberWhoWaitedZeroToFourWeeks': 'Number who waited 0 to 4 weeks', 'NumberWhoWaitedFiveToEightWeeks': 'Number who waited 5 to 8 weeks', 'NumberWhoWaitedNineToTwelveWeeks': 'Number who waited 9 to 12 weeks', 'NumberWhoWaitedThirteenToSixteenWeeks': 'Number who waited 13 to 16 weeks', 'NumberWhoWaitedSixteenPlusWeeks': 'Number who waited more than 16 weeks', 'NumberWhoWaitedFourPlusWeeks': 'Number who waited more than four weeks', 'NumberWhoWaitedZeroToFourWeeksPc': 'Percentage of people who waited between 0 and 4 weeks', 'NumberWhoWaitedFiveToEightWeeksPc': 'Percentage who waited between 5 and 8 weeks', 'NumberWhoWaitedNineToTwelveWeeksPc': 'Percentage who waited 9 to 12 weeks', 'NumberWhoWaitedThirteenToSixteenWeeksPc': 'Percentage who waited 13 to 16 weeks', 'NumberWhoWaitedSixteenPlusWeeksPc': 'Percentage who waited more than 16 weeks', 'NumberWhoWaitedFourPlusWeeksPc': 'Percentage who waited more than 4 weeks', 'HBName': 'Health board'})


#changing the time in dataset to something flourish will recognise
#from datetime import datetime
#Musculoskeletal['Month'] = pd.to_datetime(Musculoskeletal['Month'], format='%Y%m').dt.strftime('%d/%m/%y')

#filtering the dataset into different sections so it can be used in flourish
Musculoskeletal_chiro_podia= Musculoskeletal[Musculoskeletal['Specialty']=='Chiropody/Podiatry']
Musculoskeletal_occupationaltherapy= Musculoskeletal[Musculoskeletal['Specialty']=='Occupational Therapy']
Musculoskeletal_Orthotics= Musculoskeletal[Musculoskeletal['Specialty']=='Orthotics']
Musculoskeletal_Physiotherapy= Musculoskeletal[Musculoskeletal['Specialty']=='Physiotherapy']


#writing to csv
Musculoskeletal.to_csv(r'data/Musculoskeletal.csv')
#Musculoskeletal2.to_csv(r'data/Musculoskeletalseen.csv')

Musculoskeletal_chiro_podia.to_csv(r'data/Musculoskeletal_chiropody_podiatry.csv')
Musculoskeletal_occupationaltherapy.to_csv(r'data/Musculoskeletal_occupationaltherapy.csv')
Musculoskeletal_Orthotics.to_csv(r'data/Musculoskeletal_orthotics.csv')
Musculoskeletal_Physiotherapy.to_csv(r'data/Musculoskeletal_physiotherapy.csv')

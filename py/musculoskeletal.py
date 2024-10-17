import pandas as pd

patientswaiting= pd.read_csv("https://www.opendata.nhs.scot/dataset/959f2341-ca34-428c-8abb-b925a18fc0c7/resource/eff86139-89de-4169-83d5-7b5cec2ed3e9/download/open_data_ahp_msk_waiting_monthly_june2024.csv")
HBcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

merge1= pd.merge(patientswaiting, HBcodes, left_on='HBT', right_on='HB')

merge1= merge1.drop(columns=['PatientsWaitingQF', 'NumberWaitingZeroToFourWeeksQF', 'NumberWaitingFiveToEightWeeksQF', 'NumberWaitingNineToTwelveWeeksQF', 'NumberWaitingThirteenToSixteenWeeksQF', 'NumberWaitingSixteenPlusWeeksQF', 'NumberWaitingFourPlusWeeksQF', 'NumberWaitingZeroToFourWeeksPcQF', 'NumberWaitingFiveToEightWeeksPcQF', 'NumberWaitingNineToTwelveWeeksPcQF', 'NumberWaitingThirteenToSixteenWeeksPcQF', 'NumberWaitingSixteenPlusWeeksPcQF', 'NumberWaitingFourPlusWeeksPcQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])


Musculoskeletal= merge1.rename(columns={'PatientsWaiting': 'Number of patients waiting', 'NumberWaitingZeroToFourWeeks': 'Number waiting 0 to 4 weeks', 'NumberWaitingFiveToEightWeeks': 'Number waiting 5 to 8 weeks', 'NumberWaitingNineToTwelveWeeks': 'Number waiting 9 to 12 weeks', 'NumberWaitingThirteenToSixteenWeeks': 'Number waiting 13 to 16 weeks', 'NumberWaitingSixteenPlusWeeks': 'Number waiting more than 16 weeks', 'NumberWaitingFourPlusWeeks': 'Number waiting more than four weeks', 'NumberWaitingZeroToFourWeeksPc': 'Percentage of people waiting between 0 and 4 weeks', 'NumberWaitingFiveToEightWeeksPc': 'Percentage waiting between 5 and 8 weeks', 'NumberWaitingNineToTwelveWeeksPc': 'Percentage waiting 9 to 12 weeks', 'NumberWaitingThirteenToSixteenWeeksPc': 'Percentage waiting 13 to 16 weeks', 'NumberWaitingSixteenPlusWeeksPc': 'Percentage waiting more than 16 weeks', 'NumberWaitingFourPlusWeeksPc': 'Percentage waiting more than 4 weeks', 'HBName': 'Health board'})


#changing the time in dataset to something flourish will recognise
from datetime import datetime
Musculoskeletal['Month'] = pd.to_datetime(Musculoskeletal['Month'], format='%Y%m').dt.strftime('%d/%m/%y')


#filtering the dataset into different sections so it can be used in flourish
Musculoskeletal_chiro_podia= Musculoskeletal[Musculoskeletal['Specialty']=='Chiropody/Podiatry']
Musculoskeletal_occupationaltherapy= Musculoskeletal[Musculoskeletal['Specialty']=='Occupational Therapy']
Musculoskeletal_Orthotics= Musculoskeletal[Musculoskeletal['Specialty']=='Orthotics']
Musculoskeletal_Physiotherapy= Musculoskeletal[Musculoskeletal['Specialty']=='Physiotherapy']


#writing to csv
Musculoskeletal.to_csv(r'data/Musculoskeletal.csv')

Musculoskeletal_chiro_podia.to_csv(r'data/Musculoskeletal_chiropody_podiatry.csv')
Musculoskeletal_occupationaltherapy.to_csv(r'data/Musculoskeletal_occupationaltherapy.csv')
Musculoskeletal_Orthotics.to_csv(r'data/Musculoskeletal_orthotics.csv')
Musculoskeletal_Physiotherapy.to_csv(r'data/Musculoskeletal_physiotherapy.csv')

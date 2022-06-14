#importing the libraries needed
import pandas as pd

#identifying the source data
#source: https://www.opendata.nhs.scot/dataset/0d36e992-ad75-4ff1-b692-094f3d873ad7/resource/585b3f5c-e32c-45ee-8fed-96187330ac83/download/pt-adjusted-patients-waiting.csv
Patientswaiting= pd.read_csv("https://www.opendata.nhs.scot/dataset/0d36e992-ad75-4ff1-b692-094f3d873ad7/resource/585b3f5c-e32c-45ee-8fed-96187330ac83/download/pt-adjusted-patients-waiting.csv")
HBnames= pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")
Patientsseen= pd.read_csv("https://www.opendata.nhs.scot/dataset/0d36e992-ad75-4ff1-b692-094f3d873ad7/resource/ca3f8e44-9a84-43d6-819c-a880b23bd278/download/pt-adjusted-patients-seen.csv")

#merging datasets
Psychologicaltherapies= pd.merge(Patientswaiting, HBnames, how='outer')
merge2= pd.merge(Patientsseen, HBnames, how='outer')

#deleting columns that aren't necessary for the visualisation (aka they're empty)
Psychologicaltherapies1= Psychologicaltherapies.drop(columns=['TotalPatientsWaitingQF', 'NumberOfPatientsWaiting0To18WeeksQF', 'NumberOfPatientsWaiting19To35WeeksQF', 'NumberOfPatientsWaiting36To52WeeksQF', 'NumberOfPatientsWaitingOver52WeeksQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])
Merge3= merge2.drop(columns=['TotalPatientsSeenQF', 'NumberOfPatientsSeen0To18WeeksQF', 'NumberOfPatientsSeen19To35WeeksQF', 'NumberOfPatientsSeen36To52WeeksQF', 'NumberOfPatientsSeenOver52WeeksQF', 'MedianWeeksPatientsSeenQF', '90thPercentileWeeksPatientsSeenQF', 'HBDateEnacted', 'HBDateArchived', 'Country'])


#sorting the month column into a date format that is flourish compatible for the data visualisation
from datetime import datetime
Psychologicaltherapies1['Month'] = pd.to_datetime(Psychologicaltherapies1['Month'], format='%Y%m').dt.strftime('%d/%m/%y')
Merge3['Month'] = pd.to_datetime(Merge3['Month'], format='%Y%m').dt.strftime('%d/%m/%y')

#renaming columns for flourish visualisation
Psychologicaltherapies2 = Psychologicaltherapies1.rename(columns={'TotalPatientsWaiting': 'Total patients waiting', 'NumberOfPatientsWaiting0To18Weeks': 'Number of patients waiting 0 to 18 weeks','NumberOfPatientsWaiting19To35Weeks': 'Number of patients waiting 19 to 35 weeks', 'NumberOfPatientsWaiting36To52Weeks': 'Number of patients waiting 36 to 52 weeks', 'NumberOfPatientsWaitingOver52Weeks': 'Number of patients waiting over 52 weeks'}, inplace=True)
Merge4 = Merge3.rename(columns={'TotalPatientsSeen': 'Total patients seen', 'NumberOfPatientsSeen0To18Weeks': 'Number of patients seen in 0 to 18 weeks','NumberOfPatientsSeen19To35Weeks': 'Number of patients seen in 19 to 35 weeks', 'NumberOfPatientsSeen36To52Weeks': 'Number of patients seen in 36 to 52 weeks', 'NumberOfPatientsSeenOver52Weeks': 'Number of patients seen in over 52 weeks', 'MedianWeeksPatientsSeen': 'Median number of weeks patients were seen in', '90thPercentileWeeksPatientsSeen': '90th percentile weeks patients seen in', 'HBName': 'Health board'}, inplace=True)


#saving the final dataset as a csv
Psychologicaltherapies1.to_csv(r'data/PsychologicalTherapies.csv')
Merge3.to_csv(r'data/PsychologicalTherapiesSeen.csv')

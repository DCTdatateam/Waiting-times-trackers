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


#saving the final dataset as a csv
merge2.to_csv(r'data/DandAtreatment.csv')
merge3.to_csv(r'data/DandANHS.csv')
merge4.to_csv(r'data/DandAADP.csv')
merge5.to_csv(r'data/DandAPrison.csv')

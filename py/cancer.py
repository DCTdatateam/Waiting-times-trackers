#importing the libraries needed
import pandas as pd

#identifying the source data
#source: https://www.opendata.nhs.scot/dataset/drug-and-alcohol-treatment-waiting-times
cancer31day= pd.read_csv("https://www.opendata.nhs.scot/dataset/11c61a02-205b-43f6-9297-243679103617/resource/58527343-a930-4058-bf9e-3c6e5cb04010/download/cwt_31_day_standard.csv")
cancer61day= pd.read_csv("https://www.opendata.nhs.scot/dataset/11c61a02-205b-43f6-9297-243679103617/resource/23b3bbf7-7a37-4f86-974b-6360d6748e08/download/cwt_62_day_standard.csv")
HBnames= pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#merging datasets
merge1= pd.merge(cancer31day, HBnames, left_on='HBT', right_on='HB')
merge2= pd.merge(cancer61day, HBnames, left_on='HBT', right_on='HB')

#dropping unnecessary columns
cancer31dayfinal = merge1.drop(columns=['HB_x', 'HBTQF', 'CancerTypeQF', 'NumberOfEligibleReferrals31DayStandardQF', 'NumberOfEligibleReferralsTreatedWithin31DaysQF', 'HB_y', 'HBDateEnacted', 'HBDateArchived', 'Country'])
cancer62dayfinal = merge2.drop(columns=['HBQF','CancerTypeQF', 'NumberOfEligibleReferrals62DayStandardQF', 'NumberOfEligibleReferralsTreatedWithin62DaysQF', 'HB_y', 'HBDateEnacted', 'HBDateArchived'])

#renaming columns
cancer31dayfinal = cancer31dayfinal.rename(columns={'CancerType': 'Cancer type', 'NumberOfEligibleReferrals31DayStandard': 'Number of eligible referrals', 'NumberOfEligibleReferralsTreatedWithin31Days': 'Number of eligible referrals treated within 31 days', 'HBName': 'Health board'})

#filtering the columns for individual charting
cancer31_breast= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Breast']
cancer31_cervical= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Cervical']
cancer31_colorectal= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Colorectal']
cancer31_headandneck= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Head & Neck']
cancer31_Lung= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Lung']
cancer31_Lymphoma= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Lymphoma']
cancer31_Melanoma= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Melanoma']
cancer31_Ovarian= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Ovarian']
cancer31_upperGI= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Upper GI']
cancer31_Urological= cancer31dayfinal[cancer31dayfinal['Cancer type']=='Urological']


#saving the final dataset as a csv - only saving 31 days as this is what we are using for the moment
cancer31dayfinal.to_csv(r'data/cancer31day.csv')

cancer31_breast.to_csv(r'data/Cancer_Breast.csv')
cancer31_cervical.to_csv(r'data/Cancer_Cervical.csv')
cancer31_colorectal.to_csv(r'data/Cancer_Colorectal.csv')
cancer31_headandneck.to_csv(r'data/Cancer_HeadandNeck.csv')
cancer31_Lung.to_csv(r'data/Cancer_Lung.csv')
cancer31_Lymphoma.to_csv(r'data/Cancer_Lymphoma.csv')
cancer31_Melanoma.to_csv(r'data/Cancer_Melanoma.csv')
cancer31_Ovarian.to_csv(r'data/Cancer_Ovarian.csv')
cancer31_upperGI.to_csv(r'data/Cancer_UpperGI.csv')
cancer31_Urological.to_csv(r'data/Cancer_Urological.csv')

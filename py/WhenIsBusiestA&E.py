import pandas as pd

#sources
When = pd.read_csv("https://www.opendata.nhs.scot/dataset/997acaa5-afe0-49d9-b333-dcf84584603d/resource/022c3b27-6a58-48dc-8038-8f1f93bb0e78/download/opendata_monthly_ae_when_202412.csv")
healthboards = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#merging sources
Whenmerge= pd.merge(When, healthboards, left_on='HBT', right_on='HB')

##changing order of day column so it's in weekday format not alphabetical order
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Whenmerge['Day'] = pd.Categorical(Whenmerge['Day'], categories=cats, ordered=True)
df_weekday = Whenmerge.sort_values('Day')

#filtering to get rid of minor injury units
#re-coding edit note, data here changed from Emergency Department/MIU to Type 1/3. Type 1 is emergency department, source for this here: https://publichealthscotland.scot/resources-and-tools/health-intelligence-and-data-management/national-data-catalogue/data-dictionary/search-the-data-dictionary/accident-and-emergency-ae-service/
df_weekday2= df_weekday[df_weekday['DepartmentType']=='Type 1']

#renaming columns
df_weekday3= df_weekday2.rename(columns={'NumberOfAttendances': 'Number of attendances'})

df_weekday4= df_weekday3.rename(columns={'InOut': 'In or out of hours?'})


#exporting to csv
df_weekday4.to_csv(r'data/WhenIsBusiestdata.csv')

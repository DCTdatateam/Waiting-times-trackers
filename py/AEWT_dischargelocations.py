##libraries
import pandas as pd

##sources
DD = pd.read_csv("https://www.opendata.nhs.scot/dataset/997acaa5-afe0-49d9-b333-dcf84584603d/resource/c4622324-f59c-4011-a67b-83b59c59ca94/download/opendata_monthly_ae_discharge_202305.csv")
healthboards = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

##merge
DDmerge= pd.merge(DD, healthboards, left_on='HBT', right_on='HB')

#sorting the month column into a date format that is flourish compatible for the data visualisation
from datetime import datetime
DDmerge['Month'] = pd.to_datetime(DDmerge['Month'], format='%Y%m').dt.strftime('%d/%m/%y')

##Replacing the blank columns in discharge column with a value
DDmerge2= DDmerge.mask(DDmerge == '')

##Hospital = DDmerge2.rename(columns={'NumberOfAttendances': 'Number of people discharged to same hospital'})
##Hospital2= Hospital[Hospital['Discharge']=='Admission to same Hospital']


##Hospital discharges
Hospital = DDmerge2.rename(columns={'NumberOfAttendances': 'Same hospital'})
Hospital2= Hospital[Hospital['Discharge']=='Admission to same Hospital']

##Home discharges
Home = DDmerge2.rename(columns={'NumberOfAttendances': 'Home or usual place of residence'})
Home2= Home[Home['Discharge']=='Discharged Home or to usual Place of Residence']

##Hospital transfer
HospitalTransfer = DDmerge2.rename(columns={'NumberOfAttendances': 'Other hospital/service'})
HospitalTransfer2 = HospitalTransfer[HospitalTransfer['Discharge']=='Transferred to Other Hospital/Service']

##Other
Other = DDmerge2.rename(columns={'NumberOfAttendances': 'Other location'})
Other2 = Other[Other['Discharge']=='Other']

##Unknown
Unknown = DDmerge2.rename(columns={'NumberOfAttendances': 'Unknown location'})
Unknown2 = Other[Other['Discharge']=='NaN']

##dropping the discharge column because I really need it to stop merging
Hospital3= Hospital2.drop(columns=['Discharge'])
Home3= Home2.drop(columns=['Discharge'])
HospitalTransfer3= HospitalTransfer2.drop(columns=['Discharge'])
Other3= Other2.drop(columns=['Discharge'])
Unknown3= Unknown2.drop(columns=['Discharge'])



##Merge
Merge1= pd.merge(Hospital3, Home3, how='outer')
Merge2= pd.merge(HospitalTransfer3, Other3, how='outer')
Merge3= pd.merge(Merge1, Merge2, how='outer')
Merge4= pd.merge(Merge3, Unknown3, how='outer')

#Filtering again
Dischargelocations = Merge4[Merge4['DepartmentType']=='Emergency Department']


##Exports
Dischargelocations.to_csv(r'data/DischargeLocations.csv')

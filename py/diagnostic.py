import pandas as pd

hblevel= pd.read_csv("https://www.opendata.nhs.scot/dataset/3d1f49b2-f770-492f-82c9-ebefdc56ece4/resource/10dfe6f3-32de-4039-84c2-7e7794a06b31/download/diagnostics_by_board_december_2021.csv")
scotland= pd.read_csv("https://www.opendata.nhs.scot/dataset/3d1f49b2-f770-492f-82c9-ebefdc56ece4/resource/df75544f-4ba1-488d-97c7-30ab6258270d/download/diagnostics_scotland_december_2021.csv")
HBcodes = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

diagnostic= pd.merge(hblevel, HBcodes, left_on='HBT', right_on='HB')

#sorting the month column into a date format that is flourish compatible for the data visualisation
from datetime import datetime
diagnostic['MonthEnding'] = pd.to_datetime(diagnostic['MonthEnding'], format='%Y%m%d').dt.strftime('%d/%m/%y')

diagnostic1= diagnostic.drop(columns=['NumberOnListQF', 'NumberWaitingOverFourWeeksQF', 'NumberWaitingOverSixWeeksQF', 'HB', 'HBDateEnacted', 'HBDateArchived', 'Country'])
diagnostic2= diagnostic1.rename(columns={'DiagnosticTestType': 'Diagnostic test type', 'DiagnosticTestDescription': 'Diagnostic test description', 'NumberOnList': 'Number of people on list', 'NumberWaitingOverFourWeeks': 'Number of people waiting more than four weeks', 'NumberWaitingOverSixWeeks': 'Number waiting more than six weeks', 'HBName': 'Health board'})
diagnostic2.to_csv(r'data/diagnostic.csv')

diagnostic2_barium= diagnostic2[diagnostic2['Diagnostic test description']=='Barium Studies']
diagnostic2_colonoscopy= diagnostic2[diagnostic2['Diagnostic test description']=='Colonoscopy']
diagnostic2_CT= diagnostic2[diagnostic2['Diagnostic test description']=='Computer Tomography']
diagnostic2_Cystoscopy= diagnostic2[diagnostic2['Diagnostic test description']=='Cystoscopy']
diagnostic2_LowerEndoscopy= diagnostic2[diagnostic2['Diagnostic test description']=='Lower Endoscopy']
diagnostic2_MRI= diagnostic2[diagnostic2['Diagnostic test description']=='Magnetic Resonance Imaging']
diagnostic2_NonObstetricUltrasound= diagnostic2[diagnostic2['Diagnostic test description']=='Non-obstetric ultrasound']
diagnostic2_UpperEndoscopy= diagnostic2[diagnostic2['Diagnostic test description']=='Upper Endoscopy']

diagnostic2_barium.to_csv(r'data/diagnosticBARIUM.csv')
diagnostic2_colonoscopy.to_csv(r'data/diagnosticCOLONOSCOPY.csv')
diagnostic2_CT.to_csv(r'data/diagnosticCT.csv')
diagnostic2_Cystoscopy.to_csv(r'data/diagnosticCYSTOSCOPY.csv')
diagnostic2_LowerEndoscopy.to_csv(r'data/diagnosticLOWERENDOSCOPY.csv')
diagnostic2_MRI.to_csv(r'data/diagnosticMRI.csv')
diagnostic2_NonObstetricUltrasound.to_csv(r'data/diagnosticNONOBULTRASOUND.csv')
diagnostic2_UpperEndoscopy.to_csv(r'data/diagnosticUPPERENDOSCOPY.csv')

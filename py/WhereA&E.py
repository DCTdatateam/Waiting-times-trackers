import pandas as pd

#sources
When = pd.read_csv("https://www.opendata.nhs.scot/dataset/997acaa5-afe0-49d9-b333-dcf84584603d/resource/022c3b27-6a58-48dc-8038-8f1f93bb0e78/download/opendata_monthly_ae_when_202305.csv")
healthboards = pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#merging sources
Whenmerge= pd.merge(When, healthboards, left_on='HBT', right_on='HB')

Whenmerge.to_csv(r'data/Wheredata.csv')


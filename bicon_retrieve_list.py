import pandas as pd
from selenium import webdriver

import pandas as pd
import os
os.chdir('/Users/ksongsom/Library/CloudStorage/OneDrive-Personal/SideHustles/Agri_canberra/BICON_scripts/')
df = pd.read_csv('Export.csv')
print(df.columns.tolist())

df = df.rename(columns={' Case/Tariff Title': 'TariffTitle'})

#df = pd.read_csv('/Users/ksongsom/Library/CloudStorage/OneDrive-Personal/SideHustles/Agri_canberra/BICON_scripts/Export.csv')
driver = webdriver.Chrome()
for index, row in df.iterrows():
    #df['TariffTitle'][1]
    case_id = row['TariffTitle']
    driver.get(f"https://bicon.agriculture.gov.au/search?query={case_id}")
    # Extract full details, save


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# --- Example df setup ---

# --- Setup driver ---
options = Options()
options.add_argument("--headless")  # optional
driver = webdriver.Chrome(options=options)

for index, row in df.iterrows():
    case_id = row['TariffTitle']        # use this column name
    print(case_id)
    driver.get(f"https://bicon.agriculture.gov.au/search?query={case_id}")
    # extract and save details here
    # e.g., html = driver.page_source

driver.quit()

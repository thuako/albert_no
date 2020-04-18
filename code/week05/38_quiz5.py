import matplotlib.pyplot as plt
import pandas as pd
filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)
# 1. plot only district 2 and 3 with legend
# 2. count ncic codes for each district
# 3. create dataframe where the keys are district and rows are ncic_codes
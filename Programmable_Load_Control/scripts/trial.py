import pandas as pd

ewh_log='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/ewh_emcb_open_load_up.csv'
hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_emcb_open_load_up.csv"


df1 = pd.read_csv(ewh_log)
df2 = pd.read_csv(hpwh_log)


print('ewh max =========> ',df1['consumed_watts'].max())
print('hpwh max =========> ',df2['consumed_watts'].max())



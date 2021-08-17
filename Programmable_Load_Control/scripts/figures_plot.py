import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

ewh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_no_loadup_emcb_open_filled_zeros.csv"
df3 = pd.read_csv(ewh_log,parse_dates=True)
def ewh_plots(df3):
    x1 = pd.to_datetime(df3['timestamp'])
    x1 = pd.to_datetime(x1)
    x1 = x1.dt.strftime('%H:%M')
    y1 = df3['real_available_Wh']
    fig = plt.figure(figsize=(12,4))
    ax1 = fig.add_subplot(111)
    ax1.plot(x1,y1)
    ax1.set_xlabel("timestamp")
    plt.title('Open EMCB:HPWH No Load Up Command')
    ax1.set_ylabel("EnergyTake (Wh)")
    ax1.xaxis.tick_bottom()
    #ax1.annotate('Load Up Command received',xy=('18:43',825),xytext=(1000,1200),arrowprops=dict(arrowstyle='-|>'))
    #ax1.annotate('Load Up Command received',xy=('05:54',450),xytext=(0,15),arrowprops=dict(arrowstyle='-|>'))
    ax1.yaxis.tick_left()
    ax1.tick_params(axis='x')
    ax1.tick_params(axis='y')
    y_max = df3['real_available_Wh'].max()
    plt.ylim([0,y_max])
    ax1.xaxis.set_major_locator(plt.MaxNLocator(40))
    #ax1.yaxis.set_major_locator(plt.MaxNLocator(15))
    ax1.xaxis.tick_bottom()
    ax1.yaxis.tick_left()
    fig.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=45)
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/hpwh_No_load_up_emcb_open.png")
ewh_plots(df3)

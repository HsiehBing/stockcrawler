import os
import requests
import pandas as pd
import numpy as np
import pickle

def renew_data():
    filepath = "./Output.pkl"
    while os.path.isfile(filepath):
        os.remove(r"./Input.pkl")
        os.remove(r"./r_Input.pkl")
        os.remove(r"./Output.pkl")
        os.remove(r"./r_Output.pkl")
    
    #上市資料
    EFurl = 'https://www.twse.com.tw/fund/TWT38U?response=json&date=&_=1644690000895'
    res = requests.get(EFurl)
    data = res.json()
    data_all = data['data']

    df_all = []
    for i in range (len(data_all)):
        get0=[]
        for j in range(1,3):
            get0.append(data_all[i][j])
        df_all.append(get0)

        result = []
    for i in range(len(df_all)):
        result0=[]
        for j in range(0,2):
            result0.append(df_all[i][j].replace(" ",""))
        result.append(result0)

    df_all = result
    df_LN= pd.DataFrame(df_all, columns=["ID", "Name"] )
    df_LN['ID'] = df_LN['ID'].astype(str)
    aL_InputNam = zip(df_LN['Name'], df_LN['ID']+".TW")
    aL_InputNum = zip(df_LN['ID'], df_LN['ID']+".TW")
    aL_Output = zip(df_LN['ID']+".TW", df_LN['Name'] + "("+ df_LN['ID']+")")

    L_InputNam = dict(aL_InputNam)
    L_InputNum = dict(aL_InputNum)
    L_Output = dict(aL_Output)

    ##上櫃資料

    url = 'https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_result.php?l=zh-tw&se=EW&t=D&_=1659636941450'
    res = requests.get(url)
    data = res.json()
    data_all = data['aaData']
    df_all = []
    for i in range (len(data_all)):
        get0=[]
        for j in range(0,2):
            get0.append(data_all[i][j])
        df_all.append(get0)

        result = []
    for i in range(len(df_all)):
        result0=[]
        for j in range(0,2):
            result0.append(df_all[i][j].replace(" ",""))
        result.append(result0)

    df_all = result
    df_ON= pd.DataFrame(df_all, columns=["ID", "Name"] )
    df_ON['ID'] = df_ON['ID'].astype(str)
    aO_InputNam = zip(df_ON['Name'],df_ON['ID']+".TWO")
    aO_InputNum = zip(df_ON['ID'], df_ON['ID']+".TWO")
    aO_Output = zip(df_ON['ID']+".TWO", df_ON['Name'] + "("+df_ON['ID']+")")

    O_InputNam = dict(aO_InputNam)
    O_InputNum = dict(aO_InputNum)
    O_Output = dict(aO_Output)

    #merge
    ################
    Input = {**L_InputNam, **L_InputNum, **O_InputNam, **O_InputNum}
    a_file = open('Input.pkl', "wb")
    pickle.dump(Input, a_file)
    a_file.close()

    Output = {**L_Output, **O_Output}

    a_file = open('Output.pkl', "wb")
    pickle.dump(Output, a_file)
    a_file.close()
    #################
    #################
     #上市資料
    EFurl = 'https://www.twse.com.tw/fund/TWT38U?response=json&date=&_=1644690000895'
    res = requests.get(EFurl)
    data = res.json()
    data_all = data['data']

    df_all = []
    for i in range (len(data_all)):
        get0=[]
        for j in range(1,3):
            get0.append(data_all[i][j])
        df_all.append(get0)

        result = []
    for i in range(len(df_all)):
        result0=[]
        for j in range(0,2):
            result0.append(df_all[i][j].replace(" ",""))
        result.append(result0)

    df_all = result
    df_LN= pd.DataFrame(df_all, columns=["ID", "Name"] )
    df_LN['ID'] = df_LN['ID'].astype(str)
    aL_InputNam = zip(df_LN['Name'], df_LN['ID'])
    aL_InputNum = zip(df_LN['ID'], df_LN['ID'])
    aL_Output = zip(df_LN['ID']+".TW", df_LN['Name'] + "("+ df_LN['ID']+")")

    L_InputNam = dict(aL_InputNam)
    L_InputNum = dict(aL_InputNum)
    L_Output = dict(aL_Output)

    ##上櫃資料

    url = 'https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_result.php?l=zh-tw&se=EW&t=D&_=1659636941450'
    res = requests.get(url)
    data = res.json()
    data_all = data['aaData']
    df_all = []
    for i in range (len(data_all)):
        get0=[]
        for j in range(0,2):
            get0.append(data_all[i][j])
        df_all.append(get0)

        result = []
    for i in range(len(df_all)):
        result0=[]
        for j in range(0,2):
            result0.append(df_all[i][j].replace(" ",""))
        result.append(result0)

    df_all = result
    df_ON= pd.DataFrame(df_all, columns=["ID", "Name"] )
    df_ON['ID'] = df_ON['ID'].astype(str)
    aO_InputNam = zip(df_ON['Name'],df_ON['ID'])
    aO_InputNum = zip(df_ON['ID'], df_ON['ID'])
    aO_Output = zip(df_ON['ID']+".TWO", df_ON['Name'] + "("+df_ON['ID']+")")

    O_InputNam = dict(aO_InputNam)
    O_InputNum = dict(aO_InputNum)
    O_Output = dict(aO_Output)

    #merge
    ################
    Input = {**L_InputNam, **L_InputNum, **O_InputNam, **O_InputNum}
    a_file = open('r_Input.pkl', "wb")
    pickle.dump(Input, a_file)
    a_file.close()

    Output = {**L_Output, **O_Output}

    a_file = open('r_Output.pkl', "wb")
    pickle.dump(Output, a_file)
    a_file.close()
    #################
    return "完成資料更新"
import pandas as pd
import numpy as np
import chardet
import json

def getDataFrame():
    with open('mosmetro.json', 'rb') as f:
        result = chardet.detect(f.read())
    stations = pd.read_json('mosmetro.json', encoding=result['encoding'])
    stations.head()
    return stations

def createJSON():
    res = [{"A": "йцуккеены", "B": 2}, {"A": 1, "B": 2}, {"A": 1, "B": 2}]
    with open("s1.json", "w", encoding='utf-8') as f:
        json.dump(res, f, indent=4, ensure_ascii=False)

    st = getDataFrame()
    st.to_csv('s2.csv', encoding='utf-8', sep=';', index=False)

def main():
    createJSON()

if __name__ == '__main__':
    main()

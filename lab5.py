import pandas as pd
import numpy as np

##zad1
# seria = pd.Series([15, 28, 33, 47, 52, 61])
# wartosc_serii = seria.to_numpy()
# print(wartosc_serii)
# print(type(wartosc_serii))
# print(seria[seria>40])

##zad2
# seria = pd.Series({'jabłka': 120, 'gruszki': 85, 'śliwki': 95, 'banany': 140})
# seria.name = "Owoce"
# seria.index.name = "Produkt"
# print(seria)
# print(seria["gruszki"])
# seria["gruszki"]=110
# seria*=2
# print(seria)

##zad3
# d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
# k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']
# seria = pd.Series(d, index=k)
# ## klucz0 oraz klucz4 posiadaja wartosci NaN, w słowniku nie ma kluczy przez nas podanych
# seria.name = "Wartości"
# seria.index.name = "Klucz"
# print(seria)

##zad4
# data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
#         'Matematyka': [4.5, 3.5, 5.0, 3.0],
#         'Fizyka': [4.0, 4.5, 3.5, 3.0],
#         'Informatyka': [5.0, 3.0, 4.5, 4.0]}
# ramka_danych = pd.DataFrame(data, index=data['Student'])
# #df.drop('Student', axis=1, inplace=True) ##inaczej bez index
# print(ramka_danych)
# print(ramka_danych.shape)
# print(ramka_danych.index)
# print(ramka_danych.columns)
# ramka_danych.info()
# print(ramka_danych.count())

##zad5
# data = {'Kraj': ['Polska', 'Niemcy', 'Francja'],
#         'Stolica': ['Warszawa', 'Berlin', 'Paryż'],
#         'Populacja': [38000000, 83000000, 67000000]}
# df = pd.DataFrame(data)
# print(df.iloc[0,0])
# print(df.iloc[2])
# print()
# print(df['Stolica'])
# #df.loc[:,'Stolica'])
# print()
# print(df.loc[1,'Stolica'])

##zad6
# data = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ',
#         'Południe'],
#         'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
#         'Sprzedaż': [150, 200, 130, 180, 220, 170]}
# df = pd.DataFrame(data)
# print(df['Sprzedaż'])
# print(df[df['Sprzedaż'] >180])

##zad7
# data = {
#         'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
#         'Product': ['Electronics', 'Furniture', 'Clothing', 'Electronics',
#     'Furniture', 'Clothing'],
#         'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale',
#     'Retail', 'Online'],
#         'Units_Sold': [120, 80, 200, 150, 90, 300],
#         'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
#         'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
# }
# sales_df = pd.DataFrame(data)
# print(sales_df['Revenue'])
# print(sales_df[sales_df['Profit']> 15.0])
# print(sales_df[sales_df['Profit']> 15.0]['Revenue'])
# print()
# print(sales_df[sales_df['Profit'] == sales_df['Profit'].max()])
# sales_df['Renue_per_Unit']=sales_df['Revenue']/sales_df['Units_Sold']
# print(sales_df)

###########################################################NS####################################
df = pd.read_csv('../imiona.csv')

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[df['Liczba']>1000])
# tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imię'] == "ADRIAN"])
# sumę wszystkich urodzonych dzieci w całym danym okresie,
print(df['Liczba'].sum())
# sumę dzieci urodzonych w latach 2000-2005
print(df[(df.Rok>=2000) & (df.Rok<=2005)]["Liczba"].sum())
# sumę urodzonych chłopców i dziewczynek,
print('Chłopcy: ', df[df.Płeć=='M']['Liczba'].sum())
print('Dziewczęta: ', df[df.Płeć=='K']['Liczba'].sum())
# (*)  najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok]),
# (*)  najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
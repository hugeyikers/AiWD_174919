import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #Zad1
# x1 = [1000,1500,2000,2500,3000]
# y1 = [50,70,90,120,150]
# x2 = [900,1200,1600,2000,2400]
# y2 = [40,60,80,100,130]
#
# plt.figure()
# plt.scatter(x1,y1,color='blue', marker='o',label="A", s=70)
# plt.scatter(x2,y2,color='red',marker='^', label="B", s=70)
# plt.grid(True, alpha=0.3)
# plt.title("Sprzedaż vs budżet reklamowy")
# plt.xlabel("Budżet reklamowy [PLN]")
# plt.ylabel("Sprzedaż [sztuki]")
# plt.legend()
# plt.savefig('zad1.jpg', format='jpg')
# plt.show()

# #Zad2
#
# x=[40, 60, 80, 100, 120]
# y1=[8.5, 7.1, 6.2, 5.9, 6.1]
# y2=[9.5, 8.8, 7.9, 7.2, 7.5]
# y3=[12, 11, 10, 9.5, 9]
#
# plt.figure()
# plt.scatter(x,y1, color='green', marker='s', label='Samochód osobowy', s=90, alpha=0.7)
# plt.scatter(x,y2, color='orange', marker='D', label='SUV', s=90, alpha=0.7)
# plt.scatter(x,y3, color='indianred', marker='^', label='Ciężarówka', s=90, alpha=0.7)
# plt.grid(True, alpha=0.5)
# plt.title('Zużycie paliwa vs prędkość dla różnych typów pojazdów')
# plt.xlabel('Prędkość [km/h]')
# plt.ylabel('Zużycie paliwa [I/100km')
# plt.legend(loc='upper right', title='Typ pojazdu')
# plt.savefig('zad2.tiff', format='tiff'
# plt.show()

#Zad3

# dane = pd.read_csv("ecom_campaigns.csv")
# df = pd.DataFrame(dane)
#print(df)
# plt.scatter(df['visits_campaign_A'], df['orders_campaign_A'], color='red', marker='s', label='Kampania A', s=50)
# plt.scatter(df['visits_campaign_B'], df['orders_campaign_B'], color='green', marker='D', label="Kampania B", s=50)
# plt.scatter(df['visits_campaign_C'], df['orders_campaign_C'], color='blue', marker='^', label="Kampania C", s=50)
# plt.grid(True, alpha=0.5)
# plt.title("Kampanie")
# plt.legend(loc='upper left')
# plt.savefig("zadanie3.webp", format='webp')
# plt.show()

#zad4

# dane = pd.read_csv('footfall_shopping_centers.csv', parsedate='date')
# df = pd.DataFrame(dane)
# x = df['date']
# fig, ax= plt.subplots()
# plt.scatter(x, df['mall_A'], color='red', marker='s', label='Mall A', s=50)
# plt.scatter(x, df['mall_B'], color='green', marker='D', label='Mall B', s=50)
# plt.scatter(x, df['mall_C'], color='blue', marker='^', label='Mall C', s=50)
# plt.grid(True, alpha=0.5)
# fig.autofmt_xdate()
# plt.tight_layout()
# plt.title('Football shopping centers')
# plt.xlabel('Data')
# plt.ylabel('Ilość sprzedaży')
# plt.legend(loc='upper left')
# plt.savefig("zadanie4.eps", format='eps')
# plt.show()


#Zad5

# df = pd.read_csv('footfall_shopping_centers.csv')
# df2 = pd.melt(df, id_vars='date', value_vars=['mall_A', 'mall_B', 'mall_C'], var_name='Sklep', value_name="Sprzedaż")
#
# x=df[df['Sklep'] =='mall_A']['date']
# y1=df[df['Sklep']=='mall_A']['Sprzedaż']
# y2=df[df['Sklep']=='mall_B']['Sprzedaż']
# y3=df[df['Sklep']=='mall_C']['Sprzedaż']
#
# ## Reszta taka sama jak w zad4



#Zad6

# x = [2,3,4,5,6,7,8]
# y = [50,55,65,70,75,80,85]
# plt.scatter(x,y, color='black', marker='o', s=80)
# plt.scatter(x,y, color='royalblue', marker='o', s=65)
# plt.title("Zależność między godzinami nauki a wynikiem egzaminu")
# plt.xlabel("Godziny nauki")
# plt.ylabel("Wynik egzaminu (%)")
# plt.yticks(np.arange(50,91,5))
# plt.tight_layout()
# plt.savefig('Zadanie6.png', format='png')
# plt.show()

#Zad7

x1=[8,10,11,12,13,14,15]
y1=[50,56,57,62,60,62,65]
x2=[9,10,12,13,14,16]
y2=[58,55,60,64,63,66]

plt.figure()
plt.scatter(x2,y2, color='royalblue', marker='o', label='Team Alpha', s=90)
plt.scatter(x1,y1, color='darkorange', marker='s', label='Team Omega', s=90)
plt.title('Trening vs Win-Rate w Esportowych Drużynach')
plt.xlabel('Godziny treningu w tygodniu')
plt.ylabel('Win-Rate (%)')
plt.legend(loc='upper left', title="Drużyny")
plt.yticks(np.arange(50,71,5))
plt.show()
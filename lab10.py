import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad 6

# wartosci = [55.5, 24.8, 13, 6.7]
# labels = ["Inne", "Odzieżowe", "Spożywcze", "Meblowe"]
# colors = ["lavender", "lightcoral", "lightskyblue", "lightgreen"]
# explode = (0, 0.1, 0, 0)
# plt.pie(wartosci, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
# plt.axis('equal')
# plt.title("Wyniki sprzedaży - II-IV 2017")
# # plt.savefig('zad6.pdf', format='pdf')
# plt.show()

#Zad 1

# wartosci1 = [40, 20, 15, 15, 10]
# labels1 = ["Piłka nożna","Koszykówka", "Tenis", "Siatkówka", "Hokej"]
# explode1 = (0.1,0,0,0,0)
# colors1 = ["lightcoral", 'skyblue', 'mediumturquoise', 'sandybrown', 'plum']
# wartosci2 = [25,20,18,15,12,10]
# labels2 = ["Lekkoatletyka","Pływanie", "Boks", "Gimnastyka", "Kolarstwo", "Golf"]
# colors2 = ['lightskyblue', 'palegreen', 'moccasin', 'pink', 'mediumpurple', 'lightgrey']
# explode2= (0.1,0,0,0,0,0)
#
# plt.subplot(2,1,1)
# plt.pie(wartosci1,labels=labels1, explode=explode1, colors=colors1, autopct='%1.1f%%', startangle=90)
# plt.subplot(2,1,2)
# plt.pie(wartosci2,labels=labels2, explode=explode2, colors=colors2, autopct='%1.1f%%', startangle=90)
# plt.tight_layout()
# plt.title("Popularność dyscyplin sportowych")
# # plt.savefig("zad1.png", format='png')
# plt.show()

#Zad 2
# data={'Gazeta':['Fakt', 'Super Express', 'Gazeta wyborcza', 'Rzeczpospolita'], 'Sprzedaż':[130000,75000,40000, 15000]}
# df = pd.DataFrame(data)
# x=np.arange(len(df))
# colors = {'Fakt':'aquamarine', 'Super Express':'peachpuff', "Gazeta wyborcza":'lightsteelblue', 'Rzeczpospolita':'plum'}
# kolory_lista=[colors[kat] for kat in df['Gazeta']]
# fix, ax = plt.subplots(figsize=(8,6))
# ax.bar(x,df['Sprzedaż'], color=kolory_lista, alpha=0.8)
# ax.set_xticks(x,df['Gazeta'], rotation=45)
# ax.set_title("Wyniki sprzedaży dzienników ogólnopolskich za 1Q2023")
# plt.tight_layout()
# # plt.savefig('zad2.png', format='png')
# plt.show()

#Zad 3

# dzieci = np.array([10, 25, 35, 25, 55])
# mlodziez = np.array([20, 25,15, 30, 20])
# kobiety = np.array([25, 20, 30, 20, 10])
#
# ind = np.arange(5)
# # sporty = ['Piłka nożna', 'Koszykówka', 'Tenis', 'Siatkówka', 'Hokej']
# # ind = np.arange(len(sporty))
# width=0.5
# plt.bar(ind,dzieci,width, label='Dzieci', color='sandybrown')
# plt.bar(ind,mlodziez, width, label='Młodzież', bottom=dzieci, color='mediumturquoise')
# plt.bar(ind,kobiety, width, label='Kobiety', bottom=dzieci+mlodziez, color='skyblue')
# plt.ylabel('Liczba uczestników (w tys.)')
# plt.xlabel('Dyscypliny sportu')
# plt.title('Uczestnictwo w różnych dyscyplinach sportu')
# plt.xticks(ind, ('Piłka nożna', 'Koszykówka', 'Tenis', 'Siatkówka', 'Hokej'))
# plt.legend(loc='upper left')
# plt.grid(True, linestyle='--', alpha=0.4, axis='y')
# plt.tight_layout()
# # plt.savefig('zad3.webp', format='webp')
# plt.show()


#zad5

df = pd.read_csv('restauracje14.csv', sep=';', thousands=' ')
df2=pd.melt(df, id_vars='Województwo', var_name='Rok', value_name='Wartość')
df2['Rok']=df2['Rok'].astype(int)

kujpom = df2[df2['Województwo']=="KUJAWSKO-POMORSKIE"]
podlas = df2[df2['Województwo']=="PODLASKIE"]
malopol = df2[df2['Województwo']=="MAŁOPOLSKIE"]
lata = kujpom['Rok'].values
height = 0.3
plt.figure()
plt.barh(lata-height,kujpom['Wartość'], height, color='skyblue', label='Kujawskopomorskie')
plt.barh(lata+height,podlas['Wartość'], height, color='peachpuff', label='Podlaskie')
plt.barh(lata,malopol['Wartość'], height, color='palegreen', label='Małopolskie')
plt.legend(loc='lower center')
plt.ylabel('Rok')
plt.xlabel('Ilość restauracji')
plt.title('Ilość restauracji w latach 2016-2021')
plt.grid(True, alpha=0.4, linestyle='--', axis='x')
plt.xticks(np.arange(0,701, 100))
plt.yticks(lata)
plt.show()
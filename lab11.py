import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# #Zadanie 1
# fig, ax = plt.subplots()
# x = np.linspace(2,4.9, 100)
# y1 = x + 4
# y2 = np.sin(2*x)
# ax.plot(x, y1, color='red', linestyle=':', label=r'$x+4$')
# plt.title('Wykresy - kilka')
# plt.xlabel('oś pozioma')
# ax.set_ylabel('oś pionowa po lewej stronie', color ='green')
# ax.set_ylim(-12, 12)
# ax.legend(loc='upper left')
#
# ax2 = ax.twinx() #wspoldzielenie osi x
# ax2.plot(x, y2, color='saddlebrown', linestyle=':', label=r'sin($2x$)')
# ax2.set_ylim(-2,2)
# ax2.set_ylabel('oś pionowa po prawej stronie')
# ax2.legend(loc='lower center')
# fig.tight_layout()
# plt.show(block=True)

# #Zadanie 2
# fig, ax = plt.subplots()
# x = np.linspace(2,4.9, 100)
# y1 = np.sin(2*x)
# y2 = (np.e)**(2*x)
#
# ax.plot(x, y1, color = 'brown', linestyle=':', label=r'sin($2x$)')
# ax.set_ylabel('oś pionowa po lewej stronie')
# ax.set_ylim(-12,12)
# ax.legend(loc='upper left')
# plt.title("Wykresy - kilka")
# plt.xlabel('oś pozioma')
# ax2 = ax.twinx()
# ax2.plot(x,y2, color = 'blue', linestyle=':', label=r'$e^{2x}$')
# ax2.set_ylabel('oś pionowa po prawej stronie', color ='darkblue')
# ax2.legend(loc = 'lower center')
# fig.tight_layout()
# plt.show(block=True)


# #Zadanie 3
# df1 = pd.DataFrame({
# 'Sklep': ['Sklep A'] * 5 + ['Sklep B'] * 5 + ['Sklep C'] * 5,
# 'Cena (zł/kg)': [3.5, 3.6, 3.7, 3.4, 3.8,
# 3.9, 4.0, 3.8, 4.1, 3.7,
# 4.2, 4.1, 4.3, 4.0, 4.2]
# })
#
# fix, ax = plt.subplots()
# plt.title('Boxplot')
# plt.xlabel('Przykładowe dane')
# plt.ylabel('Wartości')
#
# grupy = df1['Sklep'].unique()
# lista_wartosci = [df1.loc[df1['Sklep']==s, 'Cena (zł/kg)'] for s in grupy]
# plt.boxplot(lista_wartosci, tick_labels=grupy, patch_artist=True, notch=False,
#     boxprops=dict(facecolor='palegreen', edgecolor='darkgreen'),
#     medianprops=dict(color='darkred'),
#     whiskerprops=dict(color='darkgreen'), #najlepiej takie samo jak edgecolor
#     capprops=dict(color='darkgreen'), #najlepiej takie samo jak whisker
#     flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, linestyle='none'))
# plt.tight_layout()
# plt.grid(True, axis='y')
# plt.show(block=True)


#Zadanie 6
df3 = pd.DataFrame({
'Typ rozmowy': ['Przychodzące'] * 8 + ['Wychodzące'] * 7,
'Czas (minuty)': [5, 3, 7, 2, 10, 4, 6, 8, 9, 12, 7, 5, 4, 11, 3]
})

plt.hist(
    df3['Czas (minuty)'],
    bins=4,
    color='lightblue',
    edgecolor='black',
    alpha=0.7,
)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Rozkład czasu rozmowy telefonicznej')
plt.xlabel('Czas rozmowy')
plt.ylabel('Czas połączeń')
plt.xticks(np.arange(2,12.5))
plt.show()
# -*- coding: utf-8 -*-
"""
- Wczytaj danych i wyświetl kilka pierwszych wierszy, aby zapoznać się ze strukturą danych.
  Sprawdź liczby wierszy i kolumn w zbiorze danych.
- Usuń pingwiny z brakami danych i dodaj nową kolumnę, gdzie każdemu pingwinowi przypiszemy liczbę gdzie 1 to pingwin o największej masie (0,25)
- Oblicz średnią i odchylenie standardowe z cech fizycznych pingwinów (wszystkich i dla każdego z gatanku). (0,5)
- Zwizualizuj dane za pomocą histogramu przedstawiającego rozkład mas pingwinów oraz boxplot prezentującego rozkład mas w zależności od gatunku pingwinów. (0,5)
- Utwórz nowy dataset który zwiera tylko pingwiny z masą nie wiekszą niż 3 odchelnia standardowe od średniej (0,25)
- Zobrazuj zależność między "flipper_length_mm" i "bill_length_mm" za pomocą scatter plotu (uwzględnij gatunek) (0,5)

import seaborn as sns
#Wczytanie danych
pingwiny = sns.load_dataset("penguins")
"""
import seaborn as sns
import matplotlib.pyplot as plt

pingwiny = sns.load_dataset("penguins")

print(pingwiny.head(20))
print("Liczba wierszy i kolumn:", pingwiny.shape)

pingwiny = pingwiny.dropna()
pingwiny['mass_rank'] = pingwiny['body_mass_g'].rank(ascending=False)

mean_all = pingwiny.mean(numeric_only=True)
std_all = pingwiny.std(numeric_only=True)

print("Średnia cech fizycznych wszystkich pingwinów:")
print(mean_all)
print("\nOdchylenie standardowe cech fizycznych wszystkich pingwinów:")
print(std_all)

mean_by_species = pingwiny.groupby('species').mean(numeric_only=True)
std_by_species = pingwiny.groupby('species').std(numeric_only=True)

print("\nŚrednia cech fizycznych według gatunku:")
print(mean_by_species)
print("\nOdchylenie standardowe cech fizycznych według gatunku:")
print(std_by_species)

plt.figure(figsize=(10, 6))
plt.hist(pingwiny['body_mass_g'], bins=20, color='skyblue', edgecolor='black')
plt.title('Rozkład mas pingwinów')
plt.xlabel('Masa (g)')
plt.ylabel('Liczba pingwinów')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=pingwiny, x='species', y='body_mass_g')
plt.title('Rozkład mas pingwinów według gatunku')
plt.xlabel('Gatunek')
plt.ylabel('Masa (g)')
plt.grid(True)
plt.show()

threshold = 3 * std_all['body_mass_g']
pingwiny_filtered = pingwiny[pingwiny['body_mass_g'] <= (mean_all['body_mass_g'] + threshold)]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=pingwiny_filtered, x='flipper_length_mm', y='bill_length_mm', hue='species')
plt.title('Zależność między długością dzioba a długością płetwy przedniej')
plt.xlabel('Długość płetwy przedniej (mm)')
plt.ylabel('Długość dzioba (mm)')
plt.grid(True)
plt.legend(title='Gatunek')
plt.show()


1. Se dau 312 serii numerice care reprezinta codul unor aplicatii binare.
   Aceste serii trebuie clusterizate (gasit numarul optim  de grupari din care fac parte) folosind KMeans (un algoritm de invatare ne-supervizata) si chat-GPT

Ce stim:
a) folosim KMeans
b) deoarece KMeans foloseste o distanta pentru a construi grupari in baza distantei, va trebui si noi sa utilizam o astfel de distanta.
   Distantele posibile ar fi: 
   - Euclidean
   - Cosinus
   - K-Shape
   - Soft-DTW (dynamic time warping)
   - DBA (DTW Barycenter Averaging)
c) pentru a calcula numarul optim de clustere se foloseste algoritmul "silhouette analysis" pentru a obtine cate o valoare pentru un numar de clustere intre 2 si 20. Valoarea cea mai mare este pentru numarul optim de clustere
d) deoarece seriile au lungimi diferite vom efectua normalizare + resampling (reducand la dimensiunea seriei celei mai mici) si in domeniul y (-1,+1)
e) numarul de clustere nu poate fi mai mare de 14 si nici mai mic 3, daca cumva obtinem o valoare mai buna pentru analiza siluetei >= 14, atunci luam cea mai mare valoare < 14
f) vom folosi toti algoritmii de distanta si vom alege numarul de clustere cel mai mic dintre toti
g) la final vom plota clusterele intr-o matrice specifica numarului gasit
   <=4 -  2x2
   5-6 -  3x2
   7-9 -  3x3
   10-12- 4x3
h) plotarea finala se face cu o culoare gri sau galben deschis pentru serii si cu rosu sau albastru inchis pentru centroid
g) incarcarea seriilor se face din fisierul "serii.json" care contine o lista de liste
h) atat graficul de la analiza siluetei pentru cele 5 distante cat si clusterele finale, vor fi scrise in fisiere cu extensia .png
i) graficele trebuie sa aiba si grid (plt.grid())
j) folosind indexii seriilor din clusterele gasite, plotati in grafice separate seriile initiale care nu au fost normalizate/resampled

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Urmatorul test se va da pe foaie si nu ar trebui sa ia mai mult de 45m

# Scrie un program Python care primind o propozitie ca input (cu N cuvinte), afiseaza o matrice cu 2 coloane si N linii ce va contine primele 2 si ultimele 2 caractere din fiecare cuvant. 
Input: Ana are mere
Output:
An na
ar re
me re

# Scrie un program Python care sa transforme o serie de numere citite dintr-un fisier, din baza 10 in baza 2, dar dupa urmatoarea regula: fiecare cifra din fiecare numar, reprezinta frecventa de scriere a caracterului 0 sau 1 (0 daca indexul cifrei este par si 1 daca este impar), iar fiecare numar format din 0 si 1 se scrie pe cate 1 rand separat. Daca cifra este 0 in numarul initial, atunci valoarea 0/1 aferenta nu apare in numarul transformat.
Input: 09,0171,0171,0171,0171,09
Output:
111111111
100000001
100000001
100000001
100000001
100000001
111111111

# Un catalog sub forma de dictionar, contine datele unor copii din clasa a 5-a. Aceste date includ numele si o serie de materii cu note. Ajutati profesorul sa gaseasca elevii, materiile si tipul de testare la care au o situatie dificila, construind un alt dictionar. Situatie dificila este definit ca:
- au media <5 la toata materia
- nu au macar 3 note la toate materiile
- din 2 tipuri de notare (oral, test) necesare, au luat note doar dintr-un tip
Pentru exemplul de mai jos:
{
	"Mihai": {
		"Romana": {"oral":[4,5,10,6]},
		"Matematica": {"test":[6,9,5], "oral":[7,8]},
		"Engleza": {"oral": [8,9,8], "test":[6,5,4]}
	},
	"Georgeta": {
		"Romana": {"oral":[2,5,4], "test": [6,3,4]},
		"Matematica": {"test":[4,8,4]},
		"Engleza": {"oral": [3,4,5], "test":[8,4,7]}
	},
	"Alex": {
		"Romana": {"test":[8,5,10], "oral": [10,6,8,9]},
		"Matematica": {"test":[3,4,3], "oral":[5,4,5,3]},
		"Engleza": {"oral": [7,8], "test":[9,7,7,8]}
	}
}

se va construi dictionarul:
{
	"Mihai": { 
		"Romana": {"test": "missing"},
		"Matematica": {"oral": "incomplete"}
	},
	"Georgeta": {
		"Romana": {"media": "<5"},
		"Matemtaica": {"oral": "missing"}
	},
	"Alex": {
		"Matematica": {"media": "<5"},
		"Engleza": {"oral": "incomplete"}
	}
}

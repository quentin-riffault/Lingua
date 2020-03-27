import numpy as np
import matplotlib.pyplot as plt

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
extended = ['é', 'è', 'ê', 'ë', 'à', 'â', 'ä', 'î', 'ï', 'ù', 'û', 'ü', 'ç', 'ô', 'ö', 'œ']
ltot = len(alphabet) + len(extended)
prob = [np.zeros((ltot)) for i in range(ltot+2)] 

# ltot-2 premiers tableaux: probabilité d'avoir la lettre suivante
# avant-dernier tableau: Fréquence d'apparition totale de la lettre
# dernier tableau: probabilités de longueur des mots
length = np.zeros((26))



with open("liste_francais.txt", encoding='iso-8859-1') as f:
	
	for mot in f:
		previous_letter = -1 #Couple 'invalide'
		
		mot = mot.lower()
		prob[27][len(mot)] += 1
		
		for letter in mot:
			if letter in extended:
				l = extended.index(letter)+26
				
				if previous_letter != -1:
					prob[previous_letter][l] += 1
				
				prob[26][l] += 1
				previous_letter = l
			elif ord(letter) < ord('a'):
				previous_letter = -1
			else:
				l = ord(letter)-ord('a')
				
				if previous_letter != -1:
					prob[previous_letter][l] += 1
								
				prob[26][l] += 1
				previous_letter = l
	f.close()


#pondération

print(np.sum(prob[0]))

for i in range(ltot-1):
	prob[i]/=np.sum(prob[i])
	
print(prob[26])

## Graphs

N = np.sum(prob[27])
print(N)

f = plt.figure(1)
plt.bar(alphabet, prob[26][:26]/N)
f.show()
g = plt.figure(2)
plt.bar(extended, prob[26][26:]/N)
g.show()
h = plt.figure(3)
axes = plt.gca()
plt.bar([i for i in range(0, 42)], prob[27]/N)
axes.set_xlim(1, 28)
h.show()

input()

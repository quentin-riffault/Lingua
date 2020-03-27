from analysis import Analysis
from word_gen import WordGen

extended = ['é', 'è', 'ê', 'ë', 'à', 'â', 'ä', 'î', 'ï', 'ù', 'û', 'ü', 'ç', 'ô', 'ö', 'œ']

A = Analysis("liste_francais.txt", extended)
A.run()



B = Analysis("words.txt",[], encoding="utf-8")
B.run()

wordA = WordGen(A)
wordB = WordGen(B)

for j in range(500):
	print(wordA.generate_word(7), " | ", wordB.generate_word(7))

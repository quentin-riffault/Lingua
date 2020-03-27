import procedural

class WordGen:
	def __init__(self, analysis):
		self.language = analysis
	
	def generate_word(self, length):

		lang = self.language
		word=[' ' for i in range(length)]
		previous_word = procedural.distrib(lang.alphabetical_periodicity[:]*100) 
		word[0] = lang.alphabet[previous_word]


		for i in range(1, length):
			temp = procedural.distrib(lang.probability_matrices[previous_word])
			word[i] = lang.alphabet[temp]
			previous_word = temp
		return ''.join(word)

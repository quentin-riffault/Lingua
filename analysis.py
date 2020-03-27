import numpy as np
import matplotlib.pyplot as plt

class Analysis:
	global MAX_WORD_LENGTH
	MAX_WORD_LENGTH = 60
	
	def __init__(self, sample, extension, alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)], encoding="iso-8859-1"):
		self.sample = sample # Sample of language data to use
		self.alphabet = alphabet+extension # Alphabet creation
		self.lalpha = len(self.alphabet) # Lenght of alphabet used
		
		self.nalpha = len(alphabet) #Number of elements in the alphabet array
		self.nextension = len(extension) #Number of elements in the extension array
		
		self.encoding = encoding # Encoding used to read the sample file
		
		self.word_length = np.zeros((MAX_WORD_LENGTH)) # You cannot go over this value, or the software WILL crash due to self.word_length OOB
		self.alphabetical_periodicity = np.zeros((self.lalpha))
		self.probability_matrices = [np.zeros((self.lalpha)) for i in range(self.lalpha)]
		
		self.analysis_done = False
	
	def show(self):
		
		a = self.nalpha
		n = self.nextension
		
		if self.analysis_done == False: # You have to go through an analysis before showing the results!
			self.run()
			self.analysis_done =  True
		
		fig1 = plt.figure(1)
		plt.title("Alphabetical Periodicity (alphabet)")
		plt.bar(self.alphabet[:a], self.alphabetical_periodicity[:a]) # Taking the entire alphabet...
		
		if n > 1:
			fig2 = plt.figure(2)
			plt.title("Alphabetical Periodicity (extension)")
			plt.bar(self.alphabet[a:a+n], self .alphabetical_periodicity[a:a+n]) # ... then the entire extension array
		
		fig3 = plt.figure(3)
		plt.title("Word length")
		plt.bar(np.arange(0, MAX_WORD_LENGTH, 1), self.word_length)
		
		plt.show()
		input()
	
	def run(self):
		print("Running analysis on the sample")
		with open(self.sample, encoding=self.encoding) as word_list:
			
			for word in word_list:
				
				previous_letter = -1 # invalid constant
				word = word.lower() #Switching to lowercase
				
				self.word_length[len(word)] += 1
				
				
				for letter in word:
					
					try:
						l = self.alphabet.index(letter)
						
						if previous_letter != -1:
							self.probability_matrices[previous_letter][l] +=1 #This letter can be after the previous one, so we can update the probability matrices"
							self.alphabetical_periodicity[l] +=1 #This letter has appeared, so we update its alphabetical periodicity
							
						previous_letter = l
						
					except ValueError: # If letter isn't in the alphabet
						previous_letter = -1 # If letter isn't in the alphabet
						
		#Downscaling
		#self.word_length = np.log(self.word_length)
		self.alphabetical_periodicity /= np.sum(self.alphabetical_periodicity) 
		self.probability_matrices[:] /= np.sum(self.probability_matrices[:])		
		
		self.analysis_done = True
		word_list.close()


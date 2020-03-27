import numpy as np
import matplotlib.pyplot as plt
from analysis import Analysis

extended = ['é', 'è', 'ê', 'ë', 'à', 'â', 'ä', 'î', 'ï', 'ù', 'û', 'ü', 'ç', 'ô', 'ö', 'œ']

A = Analysis("liste_francais.txt", extended)
A.show()

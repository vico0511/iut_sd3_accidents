import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import recall_score, f1_score

carac = pd.read_csv("C:/Users/vicol/iut_sd3_accidents/data/carac.csv",sep=';')
lieux = pd.read_csv("C:/Users/vicol/iut_sd3_accidents/data/lieux.csv",sep=';')
veh = pd.read_csv("C:/Users/vicol/iut_sd3_accidents/data/veh.csv",sep=';')
vict = pd.read_csv("C:/Users/vicol/iut_sd3_accidents/data/vict.csv",sep=';')

victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')
# ... (votre code pour la fusion des DataFrames)

# Exporter le DataFrame résultant vers un fichier CSV
victime.to_csv("C:/Users/vicol/iut_sd3_accidents/data/victime_merged.csv", index=False)

print("bonjour")
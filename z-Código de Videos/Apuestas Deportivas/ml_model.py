# -*- coding: utf-8 -*-
"""
Video: Apuestas deportivas
Autor: Guillermo Izquierdo
"""

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import classification_report
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV

WEEK = 3

df_ = pd.read_csv(f'./data/pre_game_{WEEK}_mod.csv').set_index('match_key')
df_1 = pd.read_csv(f'./data/pre_game_{WEEK+1}_mod.csv').set_index('match_key')

df = df_1


x_train, x_test, y_train, y_test = train_test_split(df.iloc[:,1:-1], df.iloc[:,-1], test_size=0.25, random_state=0)

model = LogisticRegression()
#rng = np.random.RandomState(0)
#model = RandomForestClassifier(random_state=rng, )
model.fit(x_train, y_train)


score = model.score(x_test, y_test)
print(score)

## Optimizar Arbol 
# param_dist = {
#     "max_depth": [3, None],
#     "max_features": randint(1, 11),
#     "min_samples_split": randint(2, 11),
#     "bootstrap": [True, False],
#     "criterion": ["gini", "entropy"],
# }

# rsh = HalvingRandomSearchCV(
#     estimator=model, param_distributions=param_dist, factor=2, random_state=rng
# )
# rsh.fit(x_train, y_train)
# rsh.best_params_



model = RandomForestClassifier(random_state=rng, max_features=10, criterion='entropy', bootstrap=True, max_depth=50)
model.fit(x_train, y_train)
score = model.score(x_test, y_test)
print(score)

y_pred = model.predict(x_test)


cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix
class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()


target_names = ['win', 'loose']
print(classification_report(y_test, y_pred, target_names=target_names))


y_pred_proba = model.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()




#############
## Test model
#############


df_ = pd.read_csv(f'./data/pre_game_{WEEK + 2}.csv').set_index('match_key')

y_pred_real = model.predict(df_)
y_pred_proba_real = model.predict_proba(df_)[::,1]

df_real = df_.copy()
df_real['prediction'] = y_pred_real
df_real['proba'] = y_pred_proba_real

df_real.to_csv(f'probas_per_game_{WEEK + 2}.csv')

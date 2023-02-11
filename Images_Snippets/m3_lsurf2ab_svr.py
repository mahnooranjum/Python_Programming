'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
        Model:
            neighboring pixels
            L + SURF ----> A, B 
        Data preprocessed by:
            https://github.com/Abdullah230
'''



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
print(tf.__version__)

data = pd.read_csv('data/M3/m.csv')
cols = list(data.columns)
cols.remove('a')
cols.remove('b')
X_train = data.loc[:, cols]
y_train_A = data.loc[:, ['a']]
y_train_B = data.loc[:, ['b']]

data_test = pd.read_csv('data/M3/test.csv')
X_test = data_test.loc[:, cols]
y_test_A = data_test.loc[:, ['a']]
y_test_B = data_test.loc[:, ['b']]




from sklearn.preprocessing import StandardScaler
obj = StandardScaler() 
X_train = obj.fit_transform(X_train) 
X_test = obj.transform(X_test) 

objy = StandardScaler() 
y_train_A = objy.fit_transform(y_train_A) 
y_test_A = objy.transform(y_test_A) 
y_train_B = objy.transform(y_train_B) 
y_test_B = objy.transform(y_test_B) 



N, D = X_train.shape

y_train_A = y_train_A.reshape(-1)
y_train_B = y_train_B.reshape(-1)
y_test_A = y_test_A.reshape(-1)
y_test_B = y_test_B.reshape(-1)

# from sklearn.svm import SVR
# model_A = SVR(kernel = 'rbf')
# model_A.fit(X_train, y_train_A)

# model_B = SVR(kernel = 'rbf')
# model_B.fit(X_train, y_train_B)


y_pred_A = model_A.predict(X_test)
y_pred_A = objy.inverse_transform(y_pred_A)
y_test_A = objy.inverse_transform(y_test_A)
X_test = obj.inverse_transform(X_test)
print(y_test_A.shape)
print(y_pred_A.shape)

y_pred_B = model_B.predict(X_test)
y_pred_B = objy.inverse_transform(y_pred_B)
y_test_B = objy.inverse_transform(y_test_B)
X_test = obj.inverse_transform(X_test)
print(y_test_B.shape)
print(y_pred_B.shape)


shape = (174,142,1)
imageL = X_test[:,0].reshape(shape)
imagea = y_pred_A.reshape(shape)
imageb = y_pred_B.reshape(shape)

image = np.concatenate((imageL, imagea, imageb), axis=2)

import cv2
imageT = cv2.cvtColor(image.astype('float32'), cv2.COLOR_Lab2RGB)
cv2.imshow('colored',imageT)
cv2.waitKey(0)
cv2.destroyAllWindows()


imageL = X_test[:,0].reshape(shape)
imagea = y_test_A.reshape(shape)
imageb = y_test_B.reshape(shape)

image = np.concatenate((imageL, imagea, imageb), axis=2)
imageT = cv2.cvtColor(image.astype('float32'), cv2.COLOR_Lab2RGB)
cv2.imshow('original',imageT)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
    Author: Mahnoor Anjum
    Description:
        Autocolorization
        Model:
            neighboring pixels
            L + Censure ----> A, B 
        Data preprocessed by:
            https://github.com/Abdullah230
'''



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
print(tf.__version__)

data = pd.read_csv('data/M7/m_n5.csv')
cols = list(data.columns)
cols.remove('a')
cols.remove('b')
X_train = data.loc[:, cols]
y_train = data.loc[:, ['a', 'b']]

data_test = pd.read_csv('data/M7/test_n5.csv')
X_test = data_test.loc[:, cols]
y_test = data_test.loc[:, ['a', 'b']]

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

miniL = X_train.min()
maxiL = X_train.max()
miniAB = y_train.min()
maxiAB = y_train.max()

from sklearn.preprocessing import StandardScaler
obj = StandardScaler() 
X_train = obj.fit_transform(X_train) 
X_test = obj.transform(X_test) 

objy = StandardScaler() 
y_train = objy.fit_transform(y_train) 
y_test = objy.transform(y_test) 
Y = y_train.shape[1]

N, D = X_train.shape


import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
i_layer = Input(shape = (D,))
# h_layer = Dropout(0.4)(h_layer)
h_layer = Dense(16, activation='relu')(i_layer)
h_layer = Dropout(0.4)(h_layer)
h_layer = Dense(32, activation='relu')(h_layer)
#h_layer = Dropout(0.6)(h_layer)
# h_layer = Dense(256, activation='relu')(h_layer)
o_layer = Dense(Y)(h_layer)

model = Model(i_layer, o_layer)

model.summary()

optimizer = tf.keras.optimizers.RMSprop(0.001)

model.compile(loss='mse',
              optimizer='adam',
              metrics=['mae', 'mse'])


#report = model.fit(X_train, y_train,  epochs = 10)
report = model.fit(X_train, y_train, validation_data=(X_test, y_test), \
                   epochs = 20)


plt.plot(report.history['loss'], label="loss")
plt.plot(report.history['val_loss'], label="validation_loss")
plt.legend()

model.save('models/m7_censure_n5') 


print("Train eval: ", model.evaluate(X_train, y_train))
print("Test eval: ", model.evaluate(X_test, y_test))

y_pred = model.predict(X_test)
y_pred = objy.inverse_transform(y_pred)
y_test = objy.inverse_transform(y_test)
X_test = obj.inverse_transform(X_test)
print(y_test.shape)
print(y_pred.shape)


shape = (174,142,1)
imageL = X_test[:,0].reshape(shape)
imagea = y_pred[:,0].reshape(shape)
imageb = y_pred[:,1].reshape(shape)

image = np.concatenate((imageL, imagea, imageb), axis=2)

import cv2
imageT = cv2.cvtColor(image.astype('float32'), cv2.COLOR_Lab2RGB)
cv2.imshow('colored',imageT)
cv2.waitKey(0)
cv2.destroyAllWindows()


imageL = X_test[:,0].reshape(shape)
imagea = y_test[:,0].reshape(shape)
imageb = y_test[:,1].reshape(shape)

image = np.concatenate((imageL, imagea, imageb), axis=2)
imageT = cv2.cvtColor(image.astype('float32'), cv2.COLOR_Lab2RGB)
cv2.imshow('original',imageT)
cv2.waitKey(0)
cv2.destroyAllWindows()


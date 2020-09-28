from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding
from . import word_segmentation

embedding_dim = 8

model = Sequential()
model.add(Embedding(vocabular, embedding_dim, input_length=word_num))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.summary()
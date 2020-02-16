#from keras.applications.inception_v3 import InceptionV3
from keras .applications.resnet50 import ResNet50 , preprocess_input
import numpy as np
# from generator import get_images
import random
from keras.utils import to_categorical

from keras.models import Sequential, Model
from keras.optimizers import SGD
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
# from convnetskeras.convnets import convnet
#from convnetskeras.customlayers import crosschannelnormalization, splittensor
from keras.regularizers import l2
from keras.initializers import RandomNormal, Zeros, Ones

import keras
import keras.models
import keras.layers
import keras.layers.convolutional
import keras.layers.core

import numpy as np


base_model = ResNet50(include_top=True, weights='imagenet')
base_model = Model(input=base_model.input, output=base_model.get_layer(name='avg_pool').output)
#base_model.summary()
top_model = Sequential()
top_model.add(Flatten(input_shape=(128, 224, 224, 3)))
model = Model(input=base_model.input, output=top_model(base_model.output))
"""
model.save('resnet_model.h5')
model.save_weights('complete_resnet_weight.h5')
"""
#model.summary()
# model = base_model

train_path = 'data/image_npy1/train'
test_path = 'data/image_npy1/test'

codes_train_path = 'data/code_npy1/train'
codes_test_path = 'data/code_npy1/test'

import os 

print("Training")
for f in sorted(os.listdir(train_path)):
	fp =  os.path.join(train_path, f)

	print(f)
	data = np.load(fp)
	
	data_processed = preprocess_input(data.astype(float))

	codes = model.predict(data_processed)

	#codes = model.predict(data)
	
	

	np.save(os.path.join(codes_train_path, f), codes)

print("Test")
for f in sorted(os.listdir(test_path)):
	fp =  os.path.join(test_path, f)

	print(f)
	data = np.load(fp)
	data_processed = preprocess_input(data.astype(float))

	codes = model.predict(data_processed)

	#codes = model.predict(data)

	np.save(os.path.join(codes_test_path, f), codes)


	
# model.compile(loss = 'categorical_crossentropy', optimizer =  SGD(lr = 0.01 , momentum = 0.9 ), metrics=['accuracy'] )



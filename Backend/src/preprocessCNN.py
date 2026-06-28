import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory

#Load data
def load_data():
    Base_directory='../database'
    train_data=image_dataset_from_directory(Base_directory,image_size=(200,200),subset='training',
                                        batch_size=32,validation_split=0.2,seed=42)
    test_data=image_dataset_from_directory(Base_directory,image_size=(200,200),subset='validation',
                                       batch_size=32,validation_split=0.2,seed=42)
    print(train_data.class_names)
    train_data=train_data.map(lambda x,y:(x/255.0,y))
    test_data=test_data.map(lambda x,y:(x/255.0,y))
    return train_data,test_data

#Building a model
def load_model():
    model=tf.keras.Sequential([layers.Conv2D(32,(3,3),input_shape=(200,200,3),activation='relu'),
                               layers.MaxPooling2D(2,2),
                               layers.Conv2D(64,(3,3),activation='relu'),
                               layers.MaxPooling2D(2,2),
                               layers.Conv2D(128,(3,3),activation='relu'),
                               layers.MaxPooling2D(2,2),
                               layers.GlobalAveragePooling2D(),
                               layers.BatchNormalization(),
                               layers.Dense(512,activation='relu'),
                               layers.Dropout(0.5),
                               layers.Dense(1,activation='sigmoid')])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

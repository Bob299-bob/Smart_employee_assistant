from preprocessCNN import load_data,load_model
import matplotlib.pyplot as plt

X,Y=load_data()
model=load_model()

history=model.fit(X,epochs=30,validation_data=Y,batch_size=32)
model.save('../models/model.h5')
def accuracy_graph():
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.legend('train','val')
    plt.show()
accuracy_graph()    
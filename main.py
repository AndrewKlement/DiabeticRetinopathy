from tkinter import ttk
import tensorflow as tf
from utils import *
import keras
import os


label_value = ["No Diabetic Retinopathy", "Mild Diabetic Retinopathy", "Moderate Diabetic Retinopathy", "Severe Diabetic Retinopathy", "Proliferative Diabetic Retinopathy"]

def prcsImage(path):
    img = tf.io.read_file(path)
    read_img = tf.io.decode_png(img, channels=3, dtype=tf.dtypes.uint8)
    resized = tf.image.resize(read_img, [256, 256])
    batched_image = tf.expand_dims(resized, axis=0)
    return batched_image

def evalModel(filePath, labelFrame:tkinter.Label):
    global model
    if filePath != '':
        prediction = model.predict(prcsImage(filePath))
        answer = label_value[tf.argmax(prediction[0])]
        print(answer, filePath)
        labelFrame.config(text=answer)


model = keras.models.Sequential([
    keras.layers.Conv2D(64, (3,3), activation='relu',input_shape=(256, 256, 3)),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D((2,2), 2),

    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D((2,2), 2),

    keras.layers.Conv2D(128, (3,3), activation='relu'),
    keras.layers.BatchNormalization(),

    keras.layers.Conv2D(128, (3,3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D((2,2), 2),

    keras.layers.Flatten(),
    keras.layers.Dense(1000, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(5, activation='softmax')
])

model.load_weights(os.getcwd()+"\model\V1.weights.h5")

root = App()
root.configure(padx=10, pady=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, style="Card.TFrame", padding=15)
main.grid(row=0, column=0, sticky="nsew")
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=2)
main.rowconfigure(2, weight=1)

labelImage = ttk.Label(main, text="Awaiting Input...", anchor='center')
labelImage.grid(row=0, column=0, sticky="nsew")

imageFrame = ImageFrame(main, 500, 450)
imageFrame.grid(row=1, column=0)

bottomFrame = ttk.Frame(main, padding=10)
bottomFrame.grid(row=2, column=0, sticky="nsew")
bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)

fileButton = FileButton(bottomFrame, text="Select file", imageFrame = imageFrame)
fileButton.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
analyzeButton = ttk.Button(bottomFrame, text="Analyze Image", command=lambda: eval("evalModel(fileButton.filePath(), labelImage)"))
analyzeButton.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


root.mainloop()


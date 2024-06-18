import os
import gensim
from gensim.utils import simple_preprocess
from gensim.models.word2vec import LineSentence
from datetime import datetime
import subprocess
import yaml


# train data
TRAIN_DATA_PATH = "/veld/input/" + os.getenv("in_train_data_file")

# model data
MODEL_PATH = "/veld/output/" + os.getenv("out_model_file")

# model hyperparameters
EPOCHS = int(os.getenv("epochs"))
VECTOR_SIZE = int(os.getenv("vector_size"))
WINDOW = int(os.getenv("window"))
MIN_COUNT = int(os.getenv("min_count"))


print(f"TRAIN_DATA_PATH: {TRAIN_DATA_PATH}")
print(f"MODEL_PATH: {MODEL_PATH}")
print(f"VECTOR_SIZE: {VECTOR_SIZE}")
print(f"WINDOW: {WINDOW}")
print(f"MIN_COUNT: {MIN_COUNT}")


sentences = LineSentence(TRAIN_DATA_PATH)


model = gensim.models.Word2Vec(
    sentences=sentences,
    epochs=EPOCHS,
    vector_size=VECTOR_SIZE,
    window=WINDOW,
    min_count=MIN_COUNT,
    workers=os.cpu_count(),
)
model.save(MODEL_PATH)

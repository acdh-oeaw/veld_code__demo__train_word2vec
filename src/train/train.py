import os
import gensim
from gensim.models.word2vec import LineSentence


TRAIN_DATA_PATH = "/veld/input/" + os.getenv("in_train_data_file")
MODEL_PATH = "/veld/output/" + os.getenv("out_model_file")
EPOCHS = int(os.getenv("epochs"))
VECTOR_SIZE = int(os.getenv("vector_size"))
WINDOW = int(os.getenv("window"))
MIN_COUNT = int(os.getenv("min_count"))

model = gensim.models.Word2Vec(
    sentences=LineSentence(TRAIN_DATA_PATH),
    epochs=EPOCHS,
    vector_size=VECTOR_SIZE,
    window=WINDOW,
    min_count=MIN_COUNT,
    workers=os.cpu_count(),
)
model.save(MODEL_PATH)


# veld_code__demo__train_word2vec

**Used in chain:** https://github.com/acdh-oeaw/veld_chain__demo__word2vec

This is a demo veld code repo. It contains code that is mainly intended to be integrated into a veld
chain, but can also be run on its own, by defaulting to the `data` folder.

There are two veld code services here:

- [veld_train](./veld_train.yaml): trains a word2vec model, based on a text file, where each line is
  a sentence. 

- [veld_infer](./veld_infer.yaml): launches a jupyter notebook to use a word2vec model for arbitrary
  inference.


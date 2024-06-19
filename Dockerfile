FROM python:3.11.9
RUN pip install notebook==7.0.6
RUN pip install gensim==4.3.2
RUN pip install scipy==1.10.1
RUN pip install matplotlib==3.9.0
RUN pip install scikit-learn==1.5.0


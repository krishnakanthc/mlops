FROM  python
RUN apt-get update
WORKDIR /home
RUN mkdir Titanic_Survival_Prediction
WORKDIR /home/Titanic_Survival_Prediction
COPY .  .
RUN pip install -r requirements.txt
CMD python app.py

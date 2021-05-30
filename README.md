# Python eksamn project spring 2021, gruppe 5
### Jonas Sthur Brøchner-Nielsen cph-jb373@cphbusiness.dk <cph-jb373@cphbusiness.dk>;
### Rasmus Hemmingsen cph-rh178@cphbusiness.dk <cph-rh178@cphbusiness.dk>;
### Claes Lindholm cph-cl303@cphbusiness.dk <cph-cl303@cphbusiness.dk>;

1. Project name: Text analysis of historical US presidents State of The Union speeches

2. Project description: Using NLP and other techniques in Python, we analyze US presidents SOTU speeches. The objective is to identify possible differences in the set of speeches and if possible, their causes, such as party, economical conditions and historical events.

3. Major libraries used: pandas, matplotlib, numpy, nltk, torch

4. The following libraries need to be installed (besides existing libraries in the semester notebooks). In Dockerfile, add the following lines at the bottom and build the project:
   ´RUN pip install -U textblob´
   ´RUN pip install transformers´
   ´RUN pip install wordcloud´
   'RUN pip install vaderSentiment´
   ´RUN pip install -U textblob´
   
   To run the flask_app you need to run the following commads in a terminal where ever you clone the repo to:
   `docker-compose up --build`
   
   `docker exec -it -e FLASK_APP="flask_app/main.py" notebookserver bash`
   
   `flask run --host=0.0.0.0`
   
5. Status: We have done what we planned to do. Ideally, we would have liked to investigate and tweak the LDA topic analysis parameters further but due to the size of the topic, time became a constraint.

6. List of challenges:
Fetch the relevant data.
Persist the fetched data.
Clean the data in order to make it usable for analysis.
Analyse the data with relevant methods.
Present the results visually and in text.


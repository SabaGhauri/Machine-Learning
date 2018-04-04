import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from agents import Agent
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

class Agent_sghauri(Agent):


    def choose_the_best_classifier(self, X_train, y_train, X_val, y_val):


        model2= LogisticRegression()
        model2.fit(X_train,y_train)
        predict2=model2.predict(X_val)
        var2= accuracy_score(predict2,y_val)
        confusion_matrix(y_val,predict2 )
        print ('/'*25)
        print('Accuracy for LogisticRegression')
        print(var2)
        classification_report(predict2,y_val)

        model1 = BernoulliNB()
        model1.fit(X_train, y_train)
        predict1 = model1.predict(X_val)
        var1= accuracy_score(predict1,y_val)
        print ('/'*25)
        print('Accuracy for BernoulliNB')
        print(var1)

        model3= SVC(kernel='poly' , degree=4, probability=True, random_state = 0)
        model3.fit(X_train,y_train)
        predict3=model3.predict(X_val)
        var3= accuracy_score(predict3,y_val)
        print ('/'*25)
        print('Accuracy for SVC')
        print(var3)

        return model2







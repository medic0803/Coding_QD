from pandas import DataFrame
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier

class Validation:
    improve_flag = 0
    pre_roc_auc_score = 0
    pre_f1_score = 0
    pre_accuracy_score = 0
    new_roc_auc_score = 0
    new_f1_score = 0
    new_accuracy_score = 0

    old_roc_auc_score = 0
    old_f1_score = 0
    old_accuracy_score = 0

    @staticmethod
    def validate(model: RandomForestClassifier, X_test : DataFrame, y_test):
        y_preds = model.predict(X_test)
        if (Validation.improve_flag == 1):
            # Validation

            # Improved ROC AUC Score
            Validation.new_roc_auc_score = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
            print("New Roc_AUC Score: ", Validation.new_roc_auc_score)
            print("Impoved Roc_AUC Score ", Validation.new_roc_auc_score - Validation.pre_roc_auc_score)

            Validation.old_roc_auc_score = Validation.pre_roc_auc_score
            Validation.pre_roc_auc_score = Validation.new_roc_auc_score

            # F1-score
            # F1 = (2 * precision * recall) / (precision + recall)
            Validation.new_f1_score = f1_score(y_test, y_preds, average='binary', pos_label='DDoS')
            print("New F1-score", Validation.new_f1_score)
            print("Improved F1-score", Validation.new_f1_score - Validation.pre_f1_score)

            Validation.old_f1_score = Validation.pre_f1_score
            Validation.pre_f1_score = Validation.new_f1_score

            # Accuracy
            # Accuracy = (TP + TN) / (TP + TN + FP + FN)
            Validation.new_accuracy_score = accuracy_score(y_test,y_preds, normalize=True)
            print("New Accuracy", Validation.new_accuracy_score)
            print("Improved Accuracy", Validation.new_accuracy_score - Validation.pre_accuracy_score)

            Validation.old_accuracy_score = Validation.pre_accuracy_score
            Validation.pre_accuracy_score =  Validation.new_f1_score


        else:
            Validation.improve_flag = 1
            # ROC AUC Score
            Validation.pre_roc_auc_score = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
            print("Roc_AUC Score: ", Validation.pre_roc_auc_score)

            # F1-score
            # F1 = (2 * precision * recall) / (precision + recall)

            Validation.pre_f1_score = f1_score(y_test, y_preds, average='binary', pos_label='DDoS')
            print("New F1-score", Validation.pre_f1_score)

            # Accuracy
            # Accuracy = (TP + TN) / (TP + TN + FP + FN)

            Validation.pre_accuracy_score = accuracy_score(y_test,y_preds, normalize=True)
            print("New Accuracy", Validation.pre_accuracy_score)

    @staticmethod
    def rollback():
        if Validation.improve_flag == 1:
            Validation.pre_roc_auc_score = Validation.old_roc_auc_score
            Validation.pre_f1_score = Validation.old_f1_score
            Validation.pre_accuracy_score = Validation.old_accuracy_score

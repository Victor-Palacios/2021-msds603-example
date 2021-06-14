from sklearn import svm
from sklearn import datasets
import pickle


def create_model():
    clf = svm.SVC()
    X, y= datasets.load_iris(return_X_y=True)
    clf.fit(X, y)
    pickle.dump(clf, open("app/model.p", "wb"))

def predict_data(sep_len, sep_wid, pet_len, pet_wid):
    clf2 = pickle.load(open("app/model.p", "rb"))
    return clf2.predict([[sep_len, sep_wid, pet_len, pet_wid]])[0]

if __name__=='__main__':
    create_model()

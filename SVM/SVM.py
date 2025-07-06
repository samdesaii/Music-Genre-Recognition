import inline
import matplotlib
import numpy
import pandas
import joblib
import seaborn as sns

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
# %matplotlib inline
import matplotlib.pyplot as plt


def main():
    data_set = pandas.read_csv('data_set.csv', index_col=False)
    data_set = numpy.array(data_set)
    print("Dataset shape:", data_set.shape)
    number_of_rows, number_of_cols = data_set.shape

    data_x = data_set[:, :number_of_cols - 1]
    data_y = data_set[:, number_of_cols - 1]

    X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2, random_state=4)

    model = SVC(C=100, gamma=0.08)
    print("Training the model.....")
    model.fit(X_train, y_train)

    yhat = model.predict(X_test)

    print("Classification Report.....\n", classification_report(y_test, yhat))

    cnf_matrix = confusion_matrix(y_test, yhat)
    plt.figure()
    sns.heatmap(cnf_matrix, cmap="Blues", annot=True,
                xticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae",
                             "rock"],
                yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae",
                             "rock"]);
    plt.show()

    joblib.dump(model, 'model.pkl')
    print("Trained and saved the model to project folder successfully.")


if __name__ == '__main__':
    main()

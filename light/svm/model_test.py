from sklearn.externals import joblib
# from sklearn import svm
import numpy as np
# from sklearn import model_selection
# import numpy as np
import datetime

if __name__ == '__main__':
    starttime = datetime.datetime.now()

    clf = joblib.load("./model_tf_310.m")

    # data = [[0.019076305, 316.2105263, 97.1, 97.8, 94.1],
    #         [0.972222222,194.3611111, 4.1, 3.4, 1.4, 1]]
    # data = [0.019076305, 316.2105263, 97.1, 97.8, 94.1]
    # data = [0.769230769, 221.3589744, 4.3, 4, 1.4]
    # data = [0.0131034482759, 5.49862068966, 144.3, 144.8, 139.2]
    data = [0.0348837209302 ,9.64631782946 ,143.3 ,143.2 ,139.4 ]
    vec = np.array(data).reshape(1, -1)

    result = clf.predict(vec)
    whether_attck = result[0]
    print(whether_attck)
    if int(whether_attck) == 1:
        print("attack")
    else:
        print("not attack")

    endtime = datetime.datetime.now()

    print("耗时时间为 " + str(endtime-starttime))

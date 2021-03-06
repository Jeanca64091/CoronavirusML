'''
Contagios diarios COVID-19 China
22/01/2020 - 10/11/2020
Luis Fernando Lizama -201602656
'''
#Covid
import numpy as np
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

#Covid

y_data = [
     0,   548,   95,  277,  486,  669,  802, 2632,  578, 2054, 1661,
  2089,  4739, 3086, 3991, 3733, 3147, 3523, 2704, 3015, 2525, 2032,
   373, 15136, 6463, 2055, 2100, 1921, 1777,  408,  458,  473, 1451,
    21,   219,  513,  412,  434,  328,  428,  576,  204,  125,  125,
   151,   153,   80,   53,   37,   27,   34,   11,   13,   32,   26,
    30,    25,   44,   54,   94,   55,  130,   63,   93,   70,  121,
   115,   102,  123,   76,   81,   82,   71,   79,   32,   59,   63,
    53,    91,   74,   58,   73,  120,   79,   93,   50,   47,  357,
    27,    18,   12,   36,   15,   16,   15,   10,    3,    6,   22,
     4,    12,    3,    0,    5,    2,    2,    2,    5,    1,   14,
    20,     1,    7,    6,    5,    9,    6,   10,    9,    0,    0,
     0,    18,    3,   11,    7,    1,    3,    0,   17,    5,   18,
     8,     7,   -1,   11,    6,    9,    5,    4,    3,   11,    7,
    12,    58,   49,   43,   44,   36,   36,    0,   59,   19,   52,
    29,    20,   28,   24,   18,   14,   23,    5,   31,   14,    8,
    19,    14,   18,   28,   33,   42,    0,   79,   46,    0,  109,
    20,    81,   75,   16,   85,  119,   86,  198,  139,  157,  179,
   189,   213,  207,  223,  276,  166,  172,  158,  114,  107,  122,
   132,   120,   92,  121,  113,   52,   87,   99,   70,   65,   96,
    66,    53,   33,   40,   49,   38,   41,   23,   34,   32,   30,
    22,    27,   32,   19,   19,   20,   33,   22,   17,   33,   20,
     9,    13,   27,   18,   23,   29,   22,   16,   18,   41,   17,
    23,    35,   12,   18,   10,   15,   17,   15,   27,   22,   23,
    17,    22,   17,   20,   25,   23,   15,   20,   41,   23,   27,
    34,    18,   28,   11,   36,   20,   30,   17,   34,   16,   22,
    29,    35,   20,   23,   24,   47,   49,   28,   40,   27,   31,
    55,    26,   31,   43,   39,   31,   43,   28,   26
]

def plotCovid():
    #Creacion de datasets
    X = np.asarray(range(len(y_data)))
    Y = np.asarray(y_data)
    X = X[:, np.newaxis]
    Y = Y[:, np.newaxis]
    
    # Creacion de la regresion    
    pipeline = make_pipeline(PolynomialFeatures(6), LinearRegression())
    pipeline.fit(X, Y)

    #Graficas
    seq = np.linspace(X.min(), X.max()).reshape(-1, 1)    
    pyplot.scatter(X, Y)
    pyplot.plot(seq, pipeline.predict(seq), color="orange")
    pyplot.title("Contagios diarios Covid-19")
    pyplot.show()

plotCovid()

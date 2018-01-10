print("Reconhecimento de Imagens")
print("-------------------------")
# Importando pacotes e definindo parâmetros
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import time

#%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# Criando a função para carregar o arquivo csv para um array numpy
def load_data(data_dir):
    train_data = open(data_dir + "train.csv").read()
    train_data = train_data.split("\n")[1:-1]
    train_data = [i.split(",") for i in train_data]

    # print(len(train_data))
    X_train = np.array([[int(i[j]) for j in range(1,len(i))] for i in train_data])
    y_train = np.array([int(i[0]) for i in train_data])

    # print(X_train.shape, y_train.shape)
    test_data = open(data_dir + "test.csv").read()
    test_data = test_data.split("\n")[1:-1]
    test_data = [i.split(",") for i in test_data]

    # print(len(test_data))
    X_test = np.array([[int(i[j]) for j in range(0,len(i))] for i in test_data])

    # print(X_test.shape)
    return X_train, y_train, X_test

    # Criando uma classe
class simple_knn():
    "a simple kNN with L2 distance"

    def __init__(self):
        pass

    def train(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1):
        dists = self.compute_distances(X)
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)

        for i in range(num_test):
            k_closest_y = []
            labels = self.y_train[np.argsort(dists[i,:])].flatten()

            # Encontrando os labels mais próximos
            k_closest_y = labels[:k]

            c = Counter(k_closest_y)
            y_pred[i] = c.most_common(1)[0][0]

        return(y_pred)

    def compute_distances(self, X):
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]

        dot_pro = np.dot(X, self.X_train.T)
        sum_square_test = np.square(X).sum(axis = 1)
        sum_square_train = np.square(self.X_train).sum(axis = 1)
        dists = np.sqrt(-2 * dot_pro + sum_square_train + np.matrix(sum_square_test).T)

        return(dists)

# Carregando os arquivos csv nas variáveis de treino e de teste
# Executa em alguns segundos
#data_dir = "/Users/dmpm/Dropbox/DSA/PythonFundamentos/JupyterNotebooks/Capítulo09/"
data_dir = "/home/jgazal/Documentos/Python_DSA/Capitulo9_IntroducaoAnaliseDados/"
X_train, y_train, X_test = load_data(data_dir)
# Imprimindo as variáveis
print(X_train.shape, y_train.shape, X_test.shape)

# Distribui as imagens dos dígitos randomicamente através do dataset de treino
# Executa em alguns segundos
classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num_classes = len(classes)
samples = 8

for y, cls in enumerate(classes):
    idxs = np.nonzero([i == y for i in y_train])
    idxs = np.random.choice(idxs[0], samples, replace = False)
    for i , idx in enumerate(idxs):
        plt_idx = i * num_classes + y + 1
        plt.subplot(samples, num_classes, plt_idx)
        plt.imshow(X_train[idx].reshape((28, 28)))
        plt.axis("off")
        if i == 0:
            plt.title(cls)

plt.show()

# Visualizando uma imagem de teste, reconhecida pelo modelo
plt.imshow(X_test[2311].reshape((28, 28)))
plt.show()

# Fazendo previsões para as imagens de teste, usando classificador kNN
batch_size = 2000

k = 1
classifier = simple_knn()
classifier.train(X_train, y_train)

# Processando o modelo preditivo na primeira metade do dataset de teste
# Executa em alguns minutos, dependendo da velocidade do computador

predictions = []

for i in range(int(len(X_test)/(2*batch_size))):
    print("Processando " + str(i+1) + "/" + str(int(len(X_test)/batch_size)) + "...")
    tic = time.time()
    predts = classifier.predict(X_test[i * batch_size:(i+1) * batch_size], k)
    toc = time.time()
    predictions = predictions + list(predts)

    print("Processamento concluído em " + str(toc-tic) + " segundos.")

print("Análise preditiva concluída!")

# Processando o modelo preditivo na segunda metade do dataset de teste
# Executa em alguns minutos, dependendo da velocidade do computador

for i in range(int(len(X_test)/(2*batch_size)), int(len(X_test)/batch_size)):
    print("Processando " + str(i+1) + "/" + str(int(len(X_test)/batch_size)) + "...")
    tic = time.time()
    predts = classifier.predict(X_test[i * batch_size:(i+1) * batch_size], k)
    toc = time.time()
    predictions = predictions + list(predts)

    print("Processamento concluído em " + str(toc-tic) + " Secs.")

print("Análise preditiva concluída!")

# Grava o resultado da predição em um arquivo csv

out_file = open("previsoes.csv", "w")
out_file.write("ImageId,Label\n")
for i in range(len(predictions)):
    out_file.write(str(i+1) + "," + str(int(predictions[i])) + "\n")
out_file.close()

# Neural Networks with TensorFlow

```python
import tensorflow as tf
```
#### Process
input > weight (1st synapse) > hidden layer 1 > weights (2nd synapse) > hidden layer 2 > weights (3rd synapse) > output layer

compare  output with expected output (ex: cross entropy, how close?)

optimize (ex: AdamOptimizer, gradient descent)

backpropagation

#### Data
```python
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True) #all or nothing
```

* one\_hot means only one is on for binary ([1, 0, 0, 0], [0, 1, 0, 0])

```python
n_nodes_hl1 = 500 #hidden layer 1, 500 nodes
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes =10 #number of classifications (0 to 9, so 10)
batch_size = 100 #limits each process to 100 since RAM can't handle all the data (usually)

#rows by columns, input data
#creates a placeholder for data, without needing the data until later
x = tf.placeholder(dtype='float', shape=[None, 784]) #float type, x only has columns
y = tf.placeholder(dtype='float', shape=[]) #y only has rows
def neural_network_model(data):
    #weights is tensor variable with specified shape
    #rows of previous by rows of this
    #and random values inside that shape

    #1st layer takes matrix x, weights will be x rows by hidden layer 1 columns
    hidden_1_layer = {'weights' : tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      #n_nodes_hl1 must be in array
                      'biases' : tf.Variable(tf.random_normal([n_nodes_hl1]))}
    
    #layer = input data * weights + biases
    #biases take care of times when input data is 0, so neurons can fire
    '''
    Columns of previous matrix/layer decides whether or not it can be computered.
    For example, if input is 2x2 and 1st layer is 2x3, 2nd layer will use 3 as
    its row to successfully apply the calculation. "takes" means will be multiplied by
    '''
    #layer 2 takes layer 1, weights will be hidden layer 1 rows by hidden layer 2 columns
    hidden_2_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      #n_nodes_hl1 must be in array
                      'biases' : tf.Variable(tf.random_normal([n_nodes_hl2]))}
    
    #layer 3 takes layer 2, weights will be hl2 rows by hl3 columns
    hidden_3_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      #n_nodes_hl1 must be in array
                      'biases' : tf.Variable(tf.random_normal([n_nodes_hl3]))}
    
    #output takes layer 3, output will be hl3 columns by classes
    output_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      #n_nodes_hl1 must be in array
                      'biases' : tf.Variable(tf.random_normal([n_classes]))}

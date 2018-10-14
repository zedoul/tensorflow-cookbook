import tensorflow as tf
import numpy as np

x_data = tf.placeholder(tf.float32)
m = tf.constant(3.)
prod = tf.multiply(x_data, m)
comp_graph = prod

x_val = np.array([1., 3., 5., 7., 9.])
sess = tf.Session()

for x in x_val:
    print(sess.run(comp_graph, feed_dict = {x_data: x}))

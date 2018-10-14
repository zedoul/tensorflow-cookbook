import tensorflow as tf

zeros = tf.zeros([10, 5])
ones = tf.ones([10, 5])
filled = tf.fill([10, 5], 42)
constant = tf.constant([1, 2, 3])
constant = tf.constant(42, shape = [10, 5])

zeros = tf.zeros_like(constant)

unif = tf.random_uniform([10, 5], minval = -3, maxval = 3)
norm = tf.random_normal([10, 5], mean = 0, stddev = 1)



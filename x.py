import tensorflow as tf
original_batch = 1
horizon = 12
action_shape = (1,)
amount = 1000
tf.contrib.rnn.GRUBlockCell
mean = tf.zeros((original_batch, horizon) + action_shape)
stddev = tf.ones((original_batch, horizon) + action_shape)
normal = tf.random_normal((original_batch, amount, horizon) + action_shape)
y=stddev[:, None]
action = normal * stddev[:, None] + mean[:, None]

with tf.Session() as sess:
    print(sess.run(action))
    print(sess.run(y))
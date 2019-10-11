import tensorflow as tf
import numpy as np
import time
# 创建输入数据


cell1 = tf.contrib.rnn.GRUBlockCell(4)
# cell2 =  tf.contrib.rnn.GRUBlockCell(4)
X = tf.placeholder(tf.float32,(2,10,8))
X_lengths = tf.placeholder(tf.float32)

outputs, last_states = tf.nn.dynamic_rnn(
    cell=cell1,
    dtype=tf.float32,
    sequence_length=X_lengths,
    inputs=X)
lable = tf.ones((2,10,4))
loss = lable - outputs
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
outputs2, last_states2 = tf.nn.dynamic_rnn(
    cell=cell1,
    dtype=tf.float32,
    sequence_length=X_lengths[:1],
    inputs=X[:1])

saver = tf.train.Saver()
with tf.Session() as sess:
    X1 = np.ones((2, 10, 8))
    # 第二个example长度为6

    X_lengths1 = [10, 6]
    # X2 =np.ones((1,10,8))
    # X_lengths2 = [10]
    sess.run(tf.global_variables_initializer())
    for i in range(10):
        sess.run(optimizer,feed_dict={X:X1,X_lengths:X_lengths1})
    outputs, last_states,outputs2,last_states2 = sess.run((outputs, last_states,outputs2,last_states2),feed_dict={X:X1,X_lengths:X_lengths1})
    print(last_states)
    print(outputs)
    print(last_states2)
    print(outputs2)
    print(outputs2-outputs[0])
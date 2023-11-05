import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
node1=tf.constant(3.5,tf.float32)
node2=tf.constant(5.4)
sess=tf.Session()
print(sess.run([node1,node2]))

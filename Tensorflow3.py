import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
adder_node=a+b
sess=tf.Session()
print(sess.run(adder_node,{a:[1,3],b:[3,4]}))

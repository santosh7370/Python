import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
w=tf.variable([0.3],tf.float32)
b=tf.variable([-0.3],tf.float32)
x=tf.placeholder(tf.float32)
linear_model=w*x+b
init=tf.globle_variable_initializer()
sess=tf.Session()
sess.run(init)
print(sess.run(linear_model,{x:[1,2,3,4]}))

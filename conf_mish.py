def conf_mish(x):
  x = x * tf.math.sin(tf.math.tanh(tf.math.softplus(x)))
  return x

def squish(x):
	alpha = 0.1
	x = alpha * (x * tf.math.tanh(tf.math.sofplus(x) ** tf.math.softmax(x)))
	return x

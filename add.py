# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf

a = tf.constant([2])
b = tf.constant([3])

result= tf.add(a,b)

with tf.Session() as sess:
  output = sess.run(result)
  print(output)
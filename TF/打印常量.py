import tensorflow as tf
hello = tf.contant('hello')
sess = tf.session()
prinnt(sess.run(hello))

import cv2
print('openCV')

# 不同图片的压缩比
import cv2
# read_type: 1 彩色图片
img = cv2.imread(file_name, read_type)

# IMWRITE_JPG_QUALIFY 图片质量，
# numbers 0~100
# jpg的压缩质量可以控制，即有损压缩，无法设置透明度
# png是无损压缩，还可以设置透明度
cv2.imwrite(file_name, img, [cv2.IMWRITE_JPG_QUALIFY, numbers])
# numbers: 0~9 值越小，压缩效果越差
cv2.imwrite(file_name, img, [cv2.IMWRITE_PNG_COMPRESSION, numbers])

## 像素处理
img = cv2.imread(file_name, 1)
# 100行100列对应的像素
(b,g,r) = img[100,100]

# tf基本信息
data1 = tf.constant(2.5)
data2 = tf.Variable(10, name='var')
data3 = tf.constant(2.5, dtype=tf.int32)
print(data1)
print(data2)
sess = tf.session()
print(sess.run(data1))

init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(data3))

###############################################33
init = tf.global_variables_initializer()
sess = tf.session()
with sess:
    sess.run(init)


###############################################
import tensorflow as tf
data1 = tf.constant(2, dtype=tf.int32)
data2 = tf.constant(4, dtype=tf.int32)
dataAdd = tf.add(data1, data2)
dataMul = tf.multiply(data1, data2)
dataMinus = tf.substract(data1, data2)
dataDiv = tf.divide(data1, data2)
with tf.session() as sess:
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataMinus))
    print(sess.run(dataDiv))

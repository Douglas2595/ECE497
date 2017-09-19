#!/usr/bin/env python 3
#Douglas Wise
#Sep 18, 2017
#testing file


#map testing
# a = "a"
# b = "b"
#
# map1 = {a: 'A', b: 'B'}
# map2 = {a: 'A2', b: 'B2'}
#
# print("Begin Test")
# print("testing map1: " + map1[a] + " " + map1[b])
# print("testing map2: " + map2[a] + " " + map2[b])
# print("Test Finished")

#or testing
# a = 0x10
# b = 0x01
#
# y = a | b
# print('y = {}'.format(format(y, '02x')))

#bit shift testing
a = 0x01
for i in range(1, 5):
    print('a = {}'.format(format(a, '02x')))
    a = a << 1

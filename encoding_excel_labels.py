# -*- coding: utf-8 -*-
'''
==============================================================================
 Created on Fri Sep 01 14:11:23 2017

 @author: Maciej Soltysiak

 Spreadsheets commonly use numeric labels
 for each row, and alphabetic
 labels for each column.
 The alphabetic labels follow this pattern:
 A, B, C... Z,
 AA, AB, AC... AZ
 BA, BB, BC... ZZ
 AAA, AAB, AAC...
 Your program should consume a list of labels
 and transform each label to the opposite label type:
 When a number is provided,
 output the corresponding alphabetic label.
 When an alphabetic label is provided,
 output the corresponding number.

 Keep in mind, the numeric labels are one-indexed
 (1 = A, 2 = B, etc). There is no zero.
==============================================================================
'''


import string


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


#NUMBER_OF_INPUTS = int(raw_input())
NUM2ALPHA = dict(enumerate(string.uppercase, 1))
ALPHA2NUM = {i[1]:i[0] for i in NUM2ALPHA.items()}
ALL_LABELS = []

for label in raw_input().split():
    if label.isdigit():
        encoded_label_list = list()
        label_int = int(label)
        base = 26
        while label_int:
            temp = (label_int-1)%base
            label_int = int((label_int - temp)/ base)
            encoded_label_list.append(NUM2ALPHA[temp+1])
            encoded_label_str = ''.join(list(reversed(encoded_label_list)))
        ALL_LABELS.append(encoded_label_str)
        ALL_LABELS.append(' ')
    elif label.isalpha():
        digit_label = 0
        base = 26
        label_len = len(label)
        for symbol in label:
            label_len -= 1
            digit_label += int(ALPHA2NUM[symbol])*(base**label_len)
        ALL_LABELS.append(str(digit_label))
        ALL_LABELS.append(' ')
    else:
        print('Neither numeric nor alpha')

ALL_LABELS = ALL_LABELS[:-1]
print(''.join(ALL_LABELS))

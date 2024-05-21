#!usrbinpython3

# Copyright (C) 2021 Antipode Polyglot
#
# This program is free software you can redistribute it andor modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see httpswww.gnu.orglicenses.

import csv
import sys
import os
import argparse
import statistics
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# httpsen.wikipedia.orgwikiFormant
# Catford, J.C. (1988) A Practical Introduction to Phonetics, Oxford University Press, p. 161.
std_vowels = {
    'i' (240, 2400), 
    'y' (235, 2100), 
    'e' (390, 2300), 
    'ø' (370, 1900), 
    'ɛ' (610, 1900), 
    'œ' (585, 1710), 
    'a' (850, 1610), 
    'ɶ' (820, 1530), 
    'ɑ' (750, 940), 
    'ɒ' (700, 760), 
    'ʌ' (600, 1170), 
    'ɔ' (500, 700), 
    'ɤ' (460, 1310), 
    'o' (360, 640), 
    'ɯ' (300, 1390), 
    'u' (250, 595), 
}
    


def connect_letters(letters, args, kwargs)
    f1 = []
    f2 = []
    for l in letters
        f1.append(std_vowels[l][0])
        f2.append(std_vowels[l][1])
    plt.plot(f2, f1, args, kwargs)


def main()
    font = {'family'  'normal',
            'size'    22}

    matplotlib.rc('font', font)
    
    gca = plt.gca()
    gca.set_xticks(np.arange(300, 2700, 300))
    gca.set_yticks(np.arange(100, 1000, 100))
    plt.axis([2700, 300, 1000, 100])
    plt.xlabel('F2, Hz')
    plt.ylabel('F1, Hz')
    plt.grid(True)
    connect_letters(('i', 'e', 'ɛ', 'a', 'ɑ', 'ʌ',  'ɤ', 'ɯ', 'i'), color='green', linestyle='')
    connect_letters(('y', 'ø', 'œ', 'ɶ', 'ɒ', 'ɔ',  'o', 'u', 'y'), color='red', linestyle='')

    for v, (f1, f2) in std_vowels.items()
        plt.text(f2, f1, '%s ' % v, color='green')

    
    plt.show()

    

    
if __name__ == '__main__'
    main()
#!/usr/bin/python3

# Copyright (C) 2021 Antipode Polyglot
#
# This program is free software: you can redistribute it and/or modify
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import csv
import sys
import os
import argparse
import praat_objects
import statistics
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Vowel:
    def __init__(self, name, formants):
        self.name = name
        self.formants = formants


def print_csv_vowels(vowels, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['vowel', 'F1', 'F2'])
        for vowel in vowels:
            for f12 in vowel.formants:
                writer.writerow([vowel.name, f12[0], f12[1]])


def find_deltas(vowels):
    deltas = [[], []]
    for vowel in vowels:
        for i in range(len(vowel.formants) - 1):
            for j in 0, 1:
                deltas[j].append(abs(vowel.formants[i][j] - vowel.formants[i + 1][j]))

    for j in 0, 1:
        deltas[j] = sorted(deltas[j])

    print("%s\n\n%s" %(deltas[0], deltas[1]))


def acceptable_delta(a_f12, b_f12, dx):
    DELTAS = [50, 130]
    STD_DX = 0.00625
    for j in 0, 1:
        if abs(a_f12[j] - b_f12[j]) / dx > DELTAS[j] / STD_DX:
            return False
    return True


def draw_std():
    std = {
        'i': (240, 2400),
        'y': (235, 2100),
        'e': (390, 2300),
        'ø': (370, 1900),
        'ɛ': (610, 1900),
        'œ': (585, 1710),
        'a': (850, 1610),
        'ɶ': (820, 1530),
        'ɑ': (750, 940),
        'ɒ': (700, 760),
        'ʌ': (600, 1170),
        'ɔ': (500, 700),
        'ɤ': (460, 1310),
        'o': (360, 640),
        'ɯ': (300, 1390),
        'u': (250, 595),
    }

    def connect_letters(letters, *args, **kwargs):
        f1 = []
        f2 = []
        for l in letters:
            f1.append(std[l][0])
            f2.append(std[l][1])
        plt.plot(f2, f1, *args, **kwargs)

    connect_letters(('i', 'e', 'ɛ', 'a', 'ɑ', 'ɒ', 'ɔ',  'o', 'u', 'i'), color='green', linestyle=':')


def main():
    parser = argparse.ArgumentParser(description='Draw vowel chart.')
    parser.add_argument('--formants', help='Praat Formant file')
    parser.add_argument('--annotations', help='Praat TextGrid file')
    parser.add_argument('--vowels_csv', help='Output vowels CSV file')
    parser.add_argument('--average', help='Show average positions',
                        dest='average', action='store_true')
    parser.set_defaults(average=False)
    parser.add_argument('--text_size',  type=int, help='Text size for the diagram', default=16)

    args = parser.parse_args()

    formants = praat_objects.parse_oo_text_file(args.formants)
    annotations = praat_objects.parse_oo_text_file(args.annotations)
    vowels = []

    for interval in annotations.items[0].intervals:
        if not interval.text:
            # Skip intervals without text.
            continue
        first_frame = min(int(interval.xmin / formants.dx), len(formants.frames))
        last_frame = min(int(interval.xmax / formants.dx) + 1, len(formants.frames))
        vowel_formants = []
        for i in range(first_frame, last_frame):
            f12 = (formants.frames[i].formants[0].frequency,
                   formants.frames[i].formants[1].frequency)
            if not vowel_formants or acceptable_delta(
                    vowel_formants[-1], f12, formants.dx):
                vowel_formants.append(f12)

        if not vowel_formants:
            print("No formants for %s" % interval.text)
            continue
        vowels.append(Vowel(interval.text, vowel_formants))

    if args.vowels_csv:
        print_csv_vowels(vowels, args.vowels_csv)

    font = {'family' : 'normal',
            'size'   : args.text_size}

    matplotlib.rc('font', **font)

    gca = plt.gca()
    gca.set_xticks(np.arange(300, 2700, 300))
    gca.set_yticks(np.arange(100, 1000, 100))
    plt.axis([2700, 300, 1000, 100])
    plt.xlabel('F2, Hz')
    plt.ylabel('F1, Hz')
    plt.grid(True)

    draw_std()

    for vowel in vowels:
        f1 = [f[0] for f in vowel.formants]
        f2 = [f[1] for f in vowel.formants]
        if args.average:
            plt.text(statistics.mean(f2), statistics.mean(f1),
                     vowel.name, color='red')
        else:
            plt.plot(f2, f1)
            plt.text(f2[0], f1[0], vowel.name, color='black')

    plt.show()


if __name__ == '__main__':
    main()
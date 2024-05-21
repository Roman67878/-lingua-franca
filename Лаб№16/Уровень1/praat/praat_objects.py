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

class PraatParsingException(Exception):
    pass


class PraatObject:
    pass


class PraatFormant(PraatObject):
    xmin = 0
    xmax = 0
    dx = 0
    x1 = 0
    maxn_formants = 0
    frames = []

    def long_text(self):
        txt = """File type = "ooTextFile"
Object class = "Formant 2"
xmin = %.17g
xmax = %.17g
nx = %d
dx = %.17g
x1 = %.17g
maxnFormants = %d
frames []:
""" % (self.xmin, self.xmax, len(self.frames), self.dx, self.x1, self.maxn_formants)

        for i_frame, frame in enumerate(self.frames):
            txt += """    frames [%d]:
        intensity = %.17g
        numberOfFormants = %d
        formant []:
""" % (i_frame + 1, frame.intensity, len(frame.formants))
            for i_formant, formant in enumerate(frame.formants):
                txt += """            formant [%d]:
                frequency = %.17g
                bandwidth = %.17g
""" % (i_formant + 1, formant.frequency, formant.bandwidth)
        return txt

    @staticmethod
    def load(iterator):
        pf = PraatFormant()
        pf.xmin = float(next(iterator))
        pf.xmax = float(next(iterator))
        nx = int(next(iterator))
        pf.dx = float(next(iterator))
        pf.x1 = float(next(iterator))
        pf.maxn_formants = int(next(iterator))
        pf.frames = []
        for i_frame in range(nx):
            intensity = float(next(iterator))
            number_of_formants = int(next(iterator))
            formants = []
            for i_formant in range(number_of_formants):
                frequency = float(next(iterator))
                bandwidth = float(next(iterator))
                formants.append(Formant(frequency, bandwidth))
            pf.frames.append(Frame(intensity, formants))
        return pf


class Frame:
    def __init__(self, intensity, formants):
        self.intensity = intensity
        self.formants = formants


class Formant:
    def __init__(self, frequency, bandwidth):
        self.frequency = frequency
        self.bandwidth = bandwidth


class PraatTextGrid(PraatObject):
    xmin = 0
    xmax = 0
    tiers = ''
    size = 0
    items = []

    def long_text(self):
        txt = """File type = "ooTextFile"
Object class = "TextGrid"
xmin = %.17g
xmax = %.17g
tiers? %s
size = %d
item []:
""" % (self.xmin, self.xmax, self.tiers, len(self.items))

        for i_tier, tier in enumerate(self.items):
            txt += """    item [%d]:
        class = %s
        name = %s
        xmin = %.17g
        xmax = %.17g
        intervals: size = %d
""" % (i_tier + 1,
       praat_escape_string(tier.class_name),
       praat_escape_string(tier.name),
       tier.xmin,
       tier.xmax,
       len(tier.intervals))
            for i_interval, interval in enumerate(tier.intervals):
                txt += """        intervals [%d]:
            xmin = %.17g
            xmax = %.17g
            text = %s
""" % (i_interval + 1,
       interval.xmin,
       interval.xmax,
       praat_escape_string(interval.text))
        return txt

    @staticmethod
    def load(iterator):
        tg = PraatTextGrid()
        tg.xmin = float(next(iterator))
        tg.xmax = float(next(iterator))
        tg.tiers = next(iterator)
        tg.size = int(next(iterator))
        tg.items = []
        for i_item in range(tg.size):
            tier_class = praat_unescape_string(next(iterator))
            if tier_class == 'IntervalTier':
                name = praat_unescape_string(next(iterator))
                xmin = float(next(iterator))
                xmax = float(next(iterator))
                size = int(next(iterator))
                intervals = []
                for i_interval in range(size):
                    i_xmin = float(next(iterator))
                    i_xmax = float(next(iterator))
                    i_text = praat_unescape_string(next(iterator))
                    intervals.append(Interval(i_xmin, i_xmax, i_text))
                tg.items.append(IntervalTier(name, xmin, xmax, intervals))
        return tg


class Tier:
    pass


class IntervalTier(Tier):
    class_name = 'IntervalTier'

    def __init__(self, name, xmin, xmax, intervals):
        self.name = name
        self.xmin = xmin
        self.xmax = xmax
        self.intervals = intervals


class Interval:
    def __init__(self, xmin, xmax, text):
        self.xmin = xmin
        self.xmax = xmax
        self.text = text


def praat_unescape_string(s):
    if len(s) < 2:
        return ''
    return s[1:-1].replace('""', '"')


def praat_escape_string(s):
    return '"' + s.replace('"', '""') + '"'


def parse_oo_text_file(filename):
    lines = None
    for encoding in 'utf-16', 'utf-8-sig', 'utf-8', 'ascii':
      try:
        with open(filename, 'rt', encoding=encoding) as f:
            lines = f.readlines()
        break
      except UnicodeError:
        # Try the next encoding
        pass
    if lines is None:
        raise PraatParsingException('Cannot guess encoding for %s' % filename)
    if len(lines) < 4:
        raise PraatParsingException('At least 4 lines expected for %s' % filename)
    if lines[0].strip() != 'File type = "ooTextFile"':
        raise PraatParsingException('File type is not ooTextFile for %s' % filename)
    class_line = lines[1].strip()
    if class_line == 'Object class = "Formant 2"':
        praat_class = PraatFormant
    elif class_line == 'Object class = "TextGrid"':
        praat_class = PraatTextGrid
    else:
        raise PraatParsingException('Unsupported object class %s for %s' % (class_line, filename))
    return praat_class.load(iterate_oo_text_file(lines[3:]))


def iterate_oo_text_file(lines):
    for line in lines:
        line = line.strip()
        i = 0
        while i < len(line):
            if line[i].isdigit() or line[i] == '+' or line[i] == '-':
                # Read a number.
                j = line[i:].find(' ')
                if j == -1:
                    yield line[i:]
                    break
                yield line[i:i + j]
                i += j + 1
            elif line[i] == '"':
                # Read a string in double quotes. Double quotes are escaped as "".
                j = i + 1
                while j < len(line):
                    if line[j] == '"' and (j + 1 == len(line) or line[j + 1] != '"'):
                        break
                    j += 1
                yield line[i:j + 1]
                i = j + 1
            elif line[i] == '<':
                # Read a tag in <>.
                j = line[i:].find('>')
                if j == -1:
                    yield line[i:]
                    break
                yield line[i:i + j]
                i += j + 1
            else:
                # Skip to the next space.
                j = line[i:].find(' ')
                if j == -1:
                    break
                i += j + 1
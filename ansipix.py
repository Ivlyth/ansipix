#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Author : Myth
Date   : 16/1/13
Email  : belongmyth at 163.com
'''

import sys

reload(sys)
sys.setdefaultencoding(u'utf-8')

from PIL import Image
import os


class Color(object):
    def __init__(self, r, g, b, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def RGBA(self):
        return self.r, self.g, self.b, self.a


class TermColor(object):
    def __init__(self, color, text, fg, bg):
        self.color = color
        self.text = text
        self.fg = fg
        self.bg = bg


def fmt(t):
    return u'\033[%d;%dm%s\033[0m' % (t.fg, t.bg, t.text)


TermColorPalette = [
    # Block colors
    TermColor(Color(0, 0, 0, 255), " ", 30, 40),
    TermColor(Color(225, 0, 0, 255), " ", 30, 41),
    TermColor(Color(0, 225, 0, 255), " ", 30, 42),
    TermColor(Color(225, 225, 0, 255), " ", 30, 43),
    TermColor(Color(0, 0, 225, 255), " ", 30, 44),
    TermColor(Color(225, 0, 225, 255), " ", 30, 45),
    TermColor(Color(0, 225, 225, 255), " ", 30, 46),
    TermColor(Color(255, 255, 255, 255), " ", 30, 47),
    # Half block
    TermColor(Color(80, 0, 0, 255), "░", 31, 40),
    TermColor(Color(0, 80, 0, 255), "░", 32, 40),
    TermColor(Color(80, 80, 0, 255), "░", 33, 40),
    TermColor(Color(0, 0, 80, 255), "░", 34, 40),
    TermColor(Color(80, 0, 80, 255), "░", 35, 40),
    TermColor(Color(0, 80, 80, 255), "░", 36, 40),
    TermColor(Color(80, 80, 80, 255), "░", 37, 40),
    # Quarter block
    TermColor(Color(153, 0, 0, 255), "▒", 31, 40),
    TermColor(Color(0, 153, 0, 255), "▒", 32, 40),
    TermColor(Color(153, 153, 0, 255), "▒", 33, 40),
    TermColor(Color(0, 0, 153, 255), "▒", 34, 40),
    TermColor(Color(153, 0, 153, 255), "▒", 35, 40),
    TermColor(Color(0, 153, 153, 255), "▒", 36, 40),
    TermColor(Color(153, 153, 153, 255), "▒", 37, 40),
    # Half block black
    TermColor(Color(102, 0, 0, 255), "░", 30, 41),
    TermColor(Color(0, 102, 0, 255), "░", 30, 42),
    TermColor(Color(102, 102, 0, 255), "░", 30, 43),
    TermColor(Color(0, 0, 102, 255), "░", 30, 44),
    TermColor(Color(102, 0, 102, 255), "░", 30, 45),
    TermColor(Color(0, 102, 102, 255), "░", 30, 46),
    TermColor(Color(102, 102, 102, 255), "░", 30, 47),
    # Half block red
    TermColor(Color(153, 102, 0, 255), "░", 32, 41),
    TermColor(Color(204, 102, 0, 255), "░", 33, 41),
    TermColor(Color(153, 0, 102, 255), "░", 34, 41),
    TermColor(Color(204, 0, 102, 255), "░", 35, 41),
    TermColor(Color(153, 102, 102, 255), "░", 36, 41),
    TermColor(Color(204, 102, 102, 255), "░", 37, 41),
    # Quarter block red
    TermColor(Color(102, 153, 0, 255), "▒", 32, 41),
    TermColor(Color(204, 153, 0, 255), "▒", 33, 41),
    TermColor(Color(102, 0, 153, 255), "▒", 34, 41),
    TermColor(Color(204, 0, 153, 255), "▒", 35, 41),
    TermColor(Color(102, 153, 153, 255), "▒", 36, 41),
    TermColor(Color(204, 153, 153, 255), "▒", 37, 41),
    # Half Block Colors Green
    TermColor(Color(102, 153, 0, 255), "░", 31, 42),
    TermColor(Color(102, 204, 0, 255), "░", 33, 42),
    TermColor(Color(0, 153, 102, 255), "░", 34, 42),
    TermColor(Color(102, 153, 102, 255), "░", 35, 42),
    TermColor(Color(0, 204, 102, 255), "░", 36, 42),
    TermColor(Color(102, 204, 102, 255), "░", 37, 42),
    # Quarter block colors Green
    TermColor(Color(153, 102, 0, 255), "▒", 31, 42),
    TermColor(Color(102, 204, 0, 255), "▒", 33, 42),
    TermColor(Color(0, 102, 153, 255), "▒", 34, 42),
    TermColor(Color(153, 102, 153, 255), "▒", 35, 42),
    TermColor(Color(0, 204, 153, 255), "▒", 36, 42),
    TermColor(Color(153, 204, 153, 255), "▒", 37, 42),
    # Half Block Colors Yellow
    TermColor(Color(204, 153, 0, 255), "░", 31, 43),
    TermColor(Color(153, 204, 0, 255), "░", 32, 43),
    TermColor(Color(153, 153, 102, 255), "░", 34, 43),
    TermColor(Color(204, 153, 102, 255), "░", 35, 43),
    TermColor(Color(153, 204, 102, 255), "░", 36, 43),
    TermColor(Color(204, 204, 102, 255), "░", 37, 43),
    # Quarter block colors Yellow
    TermColor(Color(204, 102, 0, 255), "▒", 31, 43),
    TermColor(Color(102, 204, 0, 255), "▒", 32, 43),
    TermColor(Color(102, 102, 153, 255), "▒", 34, 43),
    TermColor(Color(204, 102, 153, 255), "▒", 35, 43),
    TermColor(Color(102, 204, 153, 255), "▒", 36, 43),
    TermColor(Color(204, 204, 153, 255), "▒", 37, 43),
    # Half Block Blue
    TermColor(Color(102, 0, 153, 255), "░", 31, 44),
    TermColor(Color(0, 102, 153, 255), "░", 32, 44),
    TermColor(Color(102, 102, 153, 255), "░", 33, 44),
    TermColor(Color(102, 0, 204, 255), "░", 35, 44),
    TermColor(Color(0, 102, 204, 255), "░", 36, 44),
    TermColor(Color(102, 102, 204, 255), "░", 37, 44),
    # Quarter block Blue
    TermColor(Color(153, 0, 102, 255), "▒", 31, 44),
    TermColor(Color(0, 153, 102, 255), "▒", 32, 44),
    TermColor(Color(153, 153, 102, 255), "▒", 33, 44),
    TermColor(Color(153, 0, 204, 255), "▒", 35, 44),
    TermColor(Color(0, 153, 204, 255), "▒", 36, 44),
    TermColor(Color(153, 153, 204, 255), "▒", 37, 44),
    # Half Block Magenta
    TermColor(Color(204, 0, 153, 255), "░", 31, 45),
    TermColor(Color(153, 102, 153, 255), "░", 32, 45),
    TermColor(Color(204, 102, 153, 255), "░", 33, 45),
    TermColor(Color(153, 0, 204, 255), "░", 34, 45),
    TermColor(Color(153, 102, 204, 255), "░", 36, 45),
    TermColor(Color(204, 102, 204, 255), "░", 37, 45),
    # Quarter block Magenta
    TermColor(Color(204, 0, 102, 255), "▒", 31, 45),
    TermColor(Color(102, 153, 102, 255), "▒", 32, 45),
    TermColor(Color(204, 153, 102, 255), "▒", 33, 45),
    TermColor(Color(102, 0, 204, 255), "▒", 34, 45),
    TermColor(Color(102, 153, 204, 255), "▒", 36, 45),
    TermColor(Color(204, 153, 204, 255), "▒", 37, 45),
    # Half Block Cyan
    TermColor(Color(102, 153, 153, 255), "░", 31, 46),
    TermColor(Color(0, 204, 153, 255), "░", 32, 46),
    TermColor(Color(102, 204, 153, 255), "░", 33, 46),
    TermColor(Color(0, 153, 204, 255), "░", 34, 46),
    TermColor(Color(102, 153, 204, 255), "░", 35, 46),
    TermColor(Color(102, 204, 204, 255), "░", 37, 46),
    # Quarter block Cyan
    TermColor(Color(153, 102, 102, 255), "▒", 31, 46),
    TermColor(Color(0, 204, 102, 255), "▒", 32, 46),
    TermColor(Color(153, 204, 102, 255), "▒", 33, 46),
    TermColor(Color(0, 102, 204, 255), "▒", 34, 46),
    TermColor(Color(153, 102, 204, 255), "▒", 35, 46),
    TermColor(Color(153, 204, 204, 255), "▒", 37, 46),
    # Half Block white
    TermColor(Color(204, 153, 153, 255), "░", 31, 47),
    TermColor(Color(153, 204, 153, 255), "░", 32, 47),
    TermColor(Color(204, 204, 153, 255), "░", 33, 47),
    TermColor(Color(153, 153, 204, 255), "░", 34, 47),
    TermColor(Color(204, 153, 204, 255), "░", 35, 47),
    TermColor(Color(153, 204, 204, 255), "░", 36, 47),
    # Quarter block white
    TermColor(Color(204, 102, 102, 255), "▒", 31, 47),
    TermColor(Color(102, 204, 102, 255), "▒", 32, 47),
    TermColor(Color(204, 204, 102, 255), "▒", 33, 47),
    TermColor(Color(102, 102, 204, 255), "▒", 34, 47),
    TermColor(Color(204, 102, 204, 255), "▒", 35, 47),
    TermColor(Color(102, 204, 204, 255), "▒", 36, 47)
]


def sqDiff(x, y):
    if x > y:
        d = x - y
    else:
        d = y - x
    return (d * d) >> 2


def Convert(color, TermColorPalette):
    cr, cg, cb, ca = color.RGBA()
    ret, bestSum = 0, 1 << 32 - 1
    for index, termColor in (enumerate(TermColorPalette)):
        vr, vg, vb, va = termColor.color.RGBA()
        s = sqDiff(cr, vr) + sqDiff(cg, vg) + sqDiff(cb, vb) + sqDiff(ca, va)
        if s < bestSum:
            if s == 0:
                return termColor
            ret = index
            bestSum = s
    return TermColorPalette[ret]


def main():
    columns = 80

    if len(sys.argv) < 2:
        print u'not provide image file'
        sys.exit(0)

    image_file = sys.argv[1]

    if len(sys.argv) > 2:
        if not sys.argv[2].strip().isdigit():
            print u'output width must be digit'
            sys.exit(0)
        columns = int(sys.argv[2])

    abs_image_file = os.path.abspath(image_file)
    if not os.path.exists(abs_image_file):
        print u''
        sys.exit(0)

    try:
        image_obj = Image.open(abs_image_file)
    except Exception as e:
        print u'can not open image file `%s`, does it a valid image file ?!' % abs_image_file
        sys.exit(0)

    width, height = image_obj.size

    ratio = width * 1.0 / columns
    rows = int(height * 1.0 / ratio)

    ret = u''

    for j in range(rows):
        for i in range(columns):
            xOffset = int(ratio * i)
            yOffset = int(ratio * j)
            try:
                color = Color(*image_obj.getpixel((xOffset, yOffset)))
                termColor = Convert(color, TermColorPalette)
                ret += fmt(termColor)
            except Exception:
                print image_obj.getpixel((xOffset, yOffset))
        ret += u'\n'

    print ret


if __name__ == u'__main__':
    main()

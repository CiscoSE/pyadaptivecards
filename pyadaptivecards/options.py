# -*- coding: utf-8 -*-
"""PyAdaptiveCards options wrapper.

Copyright (c) 2016-2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from enum import Enum

class AbstractOption(Enum):
    def to_value(self):
        return str(self.name).lower()

    def __str__(self):
        return self.to_value()

    def __repr__(self):
        return self.to_value()

    def to_dict(self):
        return self.to_value()

class VerticalContentAlignment:
    """Specifies the vertical alignment of a component or of components in a 
    container.
    """
    TOP = 1
    CENTER = 2
    BOTTOM = 3

class Colors(AbstractOption):
    """Specifies the color of a textblock"""
    DEFAULT = 1
    DARK = 2
    LIGHT = 3
    ACCENT = 4
    GOOD = 5
    WARNING = 6
    ATTENTION = 7

class HorizontalAlignment(AbstractOption):
    """Specifies the horizontal alignment of a component"""
    LEFT = 1
    CENTER = 2
    RIGHT = 3

class FontSize(AbstractOption):
    """Specifies the font size of a TextBlock"""
    DEFAULT = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    EXTRALARGE = 5

class FontWeight(AbstractOption):
    """Specifies the font weight of a TextBlock"""
    DEFAULT = 1
    LIGHTER = 2
    BOLDER = 3

class BlockElementHeight(AbstractOption):
    """Specifies the way the height of a element is determined. """
    AUTO = 1
    STRETCH = 2

class Spacing(AbstractOption):
    """Specify the spacing around a component"""
    DEFAULT = 1
    NONE = 2
    SMALL = 3
    MEDIUM = 4
    LARGE = 5
    EXTRALARGE = 6
    PADDING = 7

class ImageSize(AbstractOption):
    """Specify the size scaling of a Image"""
    AUTO = 1
    STRETCH = 2
    SMALL = 3
    MEDIUM = 4
    LARGE = 5

class ImageStyle(AbstractOption):
    """Specifies the style of the image. 

    PERSON will make the picture rounded
    """
    DEFAULT = 1
    PERSON = 2

class ContainerStyle(AbstractOption):
    """Specifies the style of the container"""
    DEFAULT = 1
    EMPHASIS = 2

class TextInputStyle(AbstractOption):
    """Specifies the type of input that a Text input can expect"""
    TEXT = 1
    TEL = 2
    URL = 3
    EMAIL = 4

class ChoiceInputStyle(AbstractOption):
    """Specifies the display style for a choice input"""
    COMPACT = 1
    EXPANDED = 2

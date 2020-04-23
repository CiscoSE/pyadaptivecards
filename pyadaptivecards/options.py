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


class AbstractOption(str, Enum):
    def to_value(self):
        return str(self.name).lower()

    def __str__(self):
        return self.to_value()

    def __repr__(self):
        return self.to_value()

class VerticalContentAlignment(AbstractOption):
    """Specifies the vertical alignment of a component or of components in a
    container.
    """
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'

class Colors(AbstractOption):
    """Specifies the color of a textblock"""
    DEFAULT = 'default'
    DARK = 'dark'
    LIGHT = 'light'
    ACCENT = 'accent'
    GOOD = 'good'
    WARNING = 'warning'
    ATTENTION = 'attention'

class HorizontalAlignment(AbstractOption):
    """Specifies the horizontal alignment of a component"""
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'

class FontSize(AbstractOption):
    """Specifies the font size of a TextBlock"""
    DEFAULT = 'default'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRALARGE = 'extralarge'

class FontWeight(AbstractOption):
    """Specifies the font weight of a TextBlock"""
    DEFAULT = 'default'
    LIGHTER = 'lighter'
    BOLDER = 'bolder'

class BlockElementHeight(AbstractOption):
    """Specifies the way the height of a element is determined. """
    AUTO = 'auto'
    STRETCH = 'stretch'

class Spacing(AbstractOption):
    """Specify the spacing around a component"""
    DEFAULT = 'default'
    NONE = 'none'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRALARGE = 'extralarge'
    PADDING = 'padding'

class ImageSize(AbstractOption):
    """Specify the size scaling of a Image"""
    AUTO = 'auto'
    STRETCH = 'stretch'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class ImageStyle(AbstractOption):
    """Specifies the style of the image.

    PERSON will make the picture rounded
    """
    DEFAULT = 'default'
    PERSON = 'person'

class ContainerStyle(AbstractOption):
    """Specifies the style of the container"""
    DEFAULT = 'default'
    EMPHASIS = 'emphasis'

class TextInputStyle(AbstractOption):
    """Specifies the type of input that a Text input can expect"""
    TEXT = 'text'
    TEL = 'tel'
    URL = 'url'
    EMAIL = 'email'

class ChoiceInputStyle(AbstractOption):
    """Specifies the display style for a choice input"""
    COMPACT = 'compact'
    EXPANDED = 'expanded'

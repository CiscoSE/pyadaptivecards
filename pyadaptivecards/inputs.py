# -*- coding: utf-8 -*-
"""PyAdaptiveCards inputs wrapper.

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

from .abstract_components import Serializable
from .components import Choice
from .utils import check_type

class Text(Serializable):
    """Input field that accepts text."""
    def __init__(self, id, isMultiline=None,
                           maxLength=None,
                           placeholder=None,
                           style=None,
                           value=None,
                           height=None,
                           separator=None,
                           spacing=None):
        """Create a new text input.

        Args:
            id(str): The id of this input.
            isMultiline(bool): If True, multline content is allowed.
            maxLength(int): Hint for maximum number of characters (some clients ignore this).
            placeholder(str): Placeholder text to be displayed in this input field.
            style(TextInputStyle): Style of the text input (i.e. are we expecting a mail or a url)
            value(str): Initial value of this field.
            height(BlockElementHeight): Specifies the way the height of this container should
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """

        check_type(id, str, is_list=False, may_be_none=False)
        check_type(isMultiline, bool, is_list=False, may_be_none=True)
        check_type(maxLength, int, is_list=False, may_be_none=True)
        check_type(placeholder, str, is_list=False, may_be_none=True)

        self.type = "Input.Text"
        self.id = id
        self.isMultiline = isMultiline
        self.maxLength = maxLength
        self.placeholder = placeholder
        self.style = style
        self.value = value
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=[],
                         simple_properties=[
                            'id', 'type', 'isMultiline', 'maxLength',
                            'placeholder', 'style', 'value', 'height',
                            'separator', 'spacing'
                        ])

class Number(Serializable):
    """Input field that accepts numbers."""
    def __init__(self, id, max=None,
                           min=None,
                           placeholder=None,
                           value=None,
                           height=None,
                           separator=None,
                           spacing=None):
        """Create a new number input.

        Args:
            id(str): The id of this input.
            max(int): The maximum accepted value. 
            min(int): The minimum accepted value.
            placeholder(str): Placeholder text to be displayed in this input field.
            value(int): Initial value of this field.
            height(BlockElementHeight): Specifies the way the height of this container should 
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """
        self.type = "Input.Number"
        self.id = id
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=[],
                         simple_properties=[
                            'type', 'id', 'max', 'min', 'placeholder', 'value',
                            'height', 'separator', 'spacing'
                         ])

class Date(Serializable):
    """Input field that accepts date inputs."""
    def __init__(self, id, max=None,
                           min=None,
                           placeholder=None,
                           value=None,
                           height=None,
                           separator=None,
                           spacing=None):
        """Create a new Date.

        Args:
            id(str): The id of this input.
            max(str): The maximum date in ISO-8601 format.
            min(str): The minimum date in ISO-8601 format.
            placeholder(str): Placeholder text to be displayed in this input field.
            value(str): Initial value of this field.
            height(BlockElementHeight): Specifies the way the height of this container should 
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """
        self.type = "Input.Date"
        self.id = id
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=[],
                         simple_properties=[
                            'type', 'id', 'max', 'min', 'placeholder', 'value',
                            'height', 'separator', 'spacing'
                         ])
class Time(Serializable):
    """Input field that accepts time inputs."""
    def __init__(self, id, max=None,
                           min=None,
                           placeholder=None,
                           value=None,
                           height=None,
                           separator=None,
                           spacing=None):
        """Create a new time input.
        
        Args:
            id(str): The id of this input. 
            max(str): Maximum value for this time field. Might be ignored by the client.
            min(str): Minimum value for this time field. Might be ignored by the client.
            placeholder(str): Placeholder text to be displayed in this input field.
            value(str): Initial value of this field.
            height(BlockElementHeight): Specifies the way the height of this container should 
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """
        self.id = id
        self.type = "Input.Time"
        self.max = max
        self.min = min
        self.placeholder = placeholder
        self.value = value
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=[],
                         simple_properties=[
                            'id', 'type', 'max', 'min', 'placeholder', 'value',
                            'height', 'separator', 'spacing'
                        ])

class Toggle(Serializable):
    """Input field that lets a user toggle between multiple values."""
    def __init__(self, title, id, value=None,
                                  valueOff=None,
                                  valueOn=None,
                                  height=None,
                                  separator=None,
                                  spacing=None):
        """Create a new Toggle input.

        Args:
            title(str): Title of this toggle
            id(str): The id of this input.
            value(str): Initial selected value. Defaults to "false".
            valueOn(str): The value when toggle is on.
            valueOff(str): The value when toggle is off.
            height(BlockElementHeight): Specifies the way the height of this container should 
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """
        self.title = title
        self.type = "Input.Toggle"
        self.id = id
        self.value = value
        self.valueOff = valueOff
        self.valueOn = valueOn
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=[],
                         simple_properties=[
                            'type', 'id', 'title', 'value', 'valueOff',
                            'valueOn', 'height', 'separator', 'spacing'
                        ])

class Choices(Serializable):
    """Input field that displays choices to the user.
    
    Note:
        The adaptive card documentation calls this input a "ChoiceSet"
    """
    def __init__(self, choices, id, isMultiSelect=None,
                                    style=None,
                                    value=None,
                                    height=None,
                                    separator=None,
                                    spacing=None):
        """Create a new Choices input. 

        Args:
            choices(list): List of Choice components to be displayed to the user.
            id(str): The id of this input.
            isMultiSelect(bool): If True, multiple choices can be selected.
            style(ChoiceInputStyle): The style of this choices input.
            value(str): The initial choice (or choices). Comma-seperated for multiple
                initial selections.
            height(BlockElementHeight): Specifies the way the height of this container should 
                be calculated (stretch or auto).
            separator(bool): Draw a separating line when set to true
            spacing(Spacing): Specify the spacing of this component
        """
        check_type(choices, Choice, is_list=True, may_be_none=False)
        check_type(id, str, is_list=False, may_be_none=False)

        self.choices = choices
        self.type = "Input.ChoiceSet"
        self.id = id
        self.isMultiSelect = isMultiSelect
        self.style = style
        self.value = value
        self.height = height
        self.separator = separator
        self.spacing = spacing

        super().__init__(serializable_properties=['choices'],
                         simple_properties=[
                            'id', 'type', 'isMultiSelect', 'style', 'value',
                            'height', 'separator', 'spacing'
                         ])

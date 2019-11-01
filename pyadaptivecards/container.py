# -*- coding: utf-8 -*-
"""PyAdaptiveCards container wrapper.

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
from .options import ImageSize

class Container(Serializable):
   """Groups items together."""
   def __init__(self, items, selectAction=None,
                             style=None,
                             verticalContentAlignment=None,
                             height=None,
                             separator=None,
                             spacing=None,
                             id=None):
      """Create a new container.

      Args:
         items(list): List of items this container should contain.
         selectAction(OpenURL, Submit): Action to be invoked when container is selected.
         style(ContainerStyle): Style of this container.
         verticalContentAlignment(VerticalContentAlignment): Specifies vertical alignment 
            of the content. 
         height(BlockElementHeight): Specifies the way the height of this container should 
            be calculated (stretch or auto).
         separator(bool): Draw a separating line when set to true
         spacing(Spacing): Specify the spacing of this component
         id(str): The id of this component
      """
      self.type = "Container"
      self.items = items
      self.selectAction = selectAction
      self.style = style
      self.verticalContentAlignment = verticalContentAlignment
      self.height = height
      self.separator = separator
      self.spacing = spacing
      self.id = id

      super().__init__(serializable_properties=['items'],
                       simple_properties=[
                           'selectAction', 'style', 'verticalContentAlignment',
                           'height', 'separator', 'spacing', 'id', 'type'
                       ])

class ColumnSet(Serializable):
   """Set of columns to display content side by side."""
   def __init__(self, columns=None,
                      selectAction=None,
                      height=None,
                      separator=None,
                      spacing=None,
                      id=None):
      """Create a new ColumnSet.

      Args:
         columns(list): List of Column elements.
         selectAction(OpenURL, Submit): Action to be invoked when container is selected.
         height(BlockElementHeight): Specifies the way the height of this container should 
            be calculated (stretch or auto).
         separator(bool): Draw a separating line when set to true
         spacing(Spacing): Specify the spacing of this component
         id(str): The id of this component
      """
      self.type = "ColumnSet"
      self.columns = columns
      self.selectAction = selectAction
      self.height = height
      self.separator = separator
      self.spacing = spacing
      self.id = id

      super().__init__(serializable_properties=['columns'],
                       simple_properties=[
                        'selectAction', 'height', 'separator', 'spacing',
                        'id', 'type'
                      ])

class FactSet(Serializable):
   """Set of facts to create a factoide."""
   def __init__(self, facts, height=None,
                             separator=None,
                             spacing=None,
                             id=None):
      """Create a new FactSet.

      Args:
         facts(list): List of Fact Elements to be displayed.
         height(BlockElementHeight): Specifies the way the height of this container should 
            be calculated (stretch or auto).
         separator(bool): Draw a separating line when set to true
         spacing(Spacing): Specify the spacing of this component
         id(str): The id of this component
      """
      self.type = "FactSet"
      self.facts = facts
      self.height = height
      self.separator = separator
      self.spacing = spacing
      self.id = id

      super().__init__(serializable_properties=['facts'],
                       simple_properties=[
                           'type', 'height', 'separator', 'id', 'spacing'
                       ])

class ImageSet(Serializable):
   def __init__(self, images, imageSize=None,
                              height=None,
                              separator=None,
                              spacing=None,
                              id=None):
      """Create a new ImageSet.
      
      Args:
         images(list): List of Image objects to be displayed in a image set.
         imageSize(ImageSize): Size of the image.
         height(BlockElementHeight): Specifies the way the height of this container should 
            be calculated (stretch or auto).
         separator(bool): Draw a separating line when set to true
         spacing(Spacing): Specify the spacing of this component
         id(str): The id of this component
      """
      
      self.type = "ImageSet"
      self.images = images
      self.imageSize = imageSize
      self.height = height
      self.separator = separator
      self.spacing = spacing
      self.id = id

      super().__init__(serializable_properties=['images'],
                       simple_properties=[
                           'imageSize', 'height', 'separator', 'spacing', 'id',
                           'type'
                      ])

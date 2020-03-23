# -*- coding: utf-8 -*-
"""PyAdaptiveCards Actions Wrapper.

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

class OpenUrl(Serializable):
    """Open a external url when being invoked. """
    def __init__(self, url, title=None,
                            iconURL=None):
        """Create a new OpenUrl action. 

        Args:
            url(str): The URL that is opened upon being invoked.
            title(str): Label for the button or link that represents this action.
            iconURL(str): URL to the icon (currently not supported in Webex Teams)
        """
        self.type = "Action.OpenUrl"
        self.url = url
        self.title = title
        self.iconURL = iconURL

        super().__init__(serializable_properties=[],
                         simple_properties=['type', 'url', 'title', 'iconURL'])

class Submit(Serializable):
    """Gather input fields in the card and submit them."""
    def __init__(self, data=None,
                       title=None,
                       iconURL=None,
                       ):
        """Create a new Submit action.

        Args:
            data(dict): Initial data. In html forms this would be hidden fields.
            title(str): Label for the button or link that represents this action.
            iconURL(str): URL to the icon (currently not supported in Webex Teams).
        """
        self.type = "Action.Submit"
        self.data = data
        self.title = title
        self.iconURL = iconURL

        super().__init__(serializable_properties=['data'],
                         simple_properties=['title', 'iconURL', 'type'])

class ShowCard(Serializable):
    """Shows the specified adaptive card when this action/button is clicked."""
    def __init__(self, card=None,
                       title=None,
                       iconURL=None):
        """Create a new ShowCard action.

        Args:
            card(AdaptiveCard): The adaptive card that is shown.
            title(str): Label for the button or link that represents this action.
            iconURL(str): URL to the icon (currently not supported in Webex Teams).
        """
        self.type = "Action.ShowCard"
        self.card = card
        self.title = title
        self.iconURL = iconURL

        super().__init__(serializable_properties=['card'],
                         simple_properties=['title', 'type', 'iconURL'])

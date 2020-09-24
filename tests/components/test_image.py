import unittest

from webexteamssdk import WebexTeamsAPI

from pyadaptivecards.components import Image
from pyadaptivecards.options import (BlockElementHeight,
                                     HorizontalAlignment,
                                     ImageSize,
                                     ImageStyle,
                                     Spacing)
from pyadaptivecards.actions import OpenUrl

class ImageComponentTest(unittest.TestCase):
    def setUp(self):
        self.component = Image(url="https://via.placeholder.com/150.png",
                               altText="Alternative text",
                               backgroundColor="#ff0000",
                               height=BlockElementHeight.AUTO,
                               horizontalAlignment=HorizontalAlignment.CENTER,
                               selectAction=OpenUrl("https://wwww.cisco.com"),
                               size=ImageSize.AUTO,
                               style=ImageStyle.DEFAULT,
                               width="100px",
                               separator=True,
                               spacing=Spacing.MEDIUM,
                               id="image_test")
    
    def test_url(self):
        d = self.component.to_dict()

        self.assertIn("url", d.keys())
        self.assertIsInstance(d['url'], str)
    
    def test_altText(self):
        d = self.component.to_dict()

        self.assertIn("altText", d.keys())
        self.assertIsInstance(d['altText'], str)
        
    def test_backgroundColor(self):
        d = self.component.to_dict()

        self.assertIn("backgroundColor", d.keys())
        self.assertIsInstance(d["backgroundColor"], str)

    def test_height(self):
        d = self.component.to_dict()

        self.assertIn("height", d.keys())
        self.assertIsInstance(d["height"], str)

    def test_horizontalAlignment(self):
        d = self.component.to_dict()

        self.assertIn("horizontalAlignment", d.keys())
        self.assertIsInstance(d["horizontalAlignment"], str)

    def test_selectAction(self):
        d = self.component.to_dict()

        self.assertIn("selectAction", d.keys())
        self.assertIsInstance(d["selectAction"], dict)

    def test_size(self):
        d = self.component.to_dict()

        self.assertIn("size", d.keys())
        self.assertIsInstance(d["size"], str)

    def test_style(self):
        d = self.component.to_dict()

        self.assertIn("style", d.keys())
        self.assertIsInstance(d["style"], str)

    def test_width(self):
        d = self.component.to_dict()

        self.assertIn("width", d.keys())
        self.assertIsInstance(d["width"], str)
    
    def test_separator(self):
        d = self.component.to_dict()

        self.assertIn("separator", d.keys())
        self.assertIsInstance(d["separator"], bool)

    def test_spacing(self):
        d = self.component.to_dict()

        self.assertIn("spacing", d.keys())
        self.assertIsInstance(d["spacing"], str)

    def test_id(self):
        d = self.component.to_dict()

        self.assertIn("id", d.keys())
        self.assertIsInstance(d["id"], str)


    

    



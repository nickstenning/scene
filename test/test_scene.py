from . import TestCase, helpers as h

from scene import Scene

class TestScene(TestCase):

    def test_empty_scene(self):
        s = Scene()
        img = s.render()
        h.assert_equal(img.getpixel((0, 0)), (0, 0, 0, 0))





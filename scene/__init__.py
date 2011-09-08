from __future__ import division

import pkg_resources
from PIL import Image

SPHERE_IMAGE = pkg_resources.resource_stream(__name__, 'sources/sphere.png')
CUBE_IMAGE = pkg_resources.resource_stream(__name__, 'sources/cube.png')

class Scene(object):
    def __init__(self, box_size=1.0, img_size=None, eye_distance=1.0):
        self.box_size = box_size
        self.img_size = img_size if img_size else (512, 512)
        self.eye_distance = eye_distance
        self.eye_coords = (0.0, 0.0) # x, z

        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def clear_objects(self):
        self.objects = []

    def render(self):
        scene = Image.new("RGBA", self.img_size)

        # Poor man's painter's algorithm: sort objects in depth order.
        self.objects.sort(lambda x, y: cmp(y.coords[1], x.coords[1]))

        for o in self.objects:
            # origin of coordinates is at center of object box, "depth" is
            # distance from nearest face of viewbox:
            depth = o.coords[1] + self.box_size / 2
            depth_factor = self.eye_distance / (self.eye_distance + depth)

            scaled_size = [int(d * o.size * depth_factor) for d in o.image.size]
            image = o.image.resize(scaled_size)

            center_coords = [(o.coords[0] - self.eye_coords[0] * depth_factor) * self.img_size[0],
                             -(o.coords[2] - self.eye_coords[1] * depth_factor) * self.img_size[1]]

            # adjust for coords zeroed at top-left
            center_coords[0] += self.img_size[0] // 2
            center_coords[1] += self.img_size[1] // 2

            # paste so that *center* of image is at object coordinates
            paste_coords = (int(center_coords[0]) - (image.size[0] // 2),
                            int(center_coords[1]) - (image.size[1] // 2))

            # Use image as both pasted image and alpha mask
            scene.paste(image, paste_coords, image)

        return scene

class SceneObject(object):
    def __init__(self, size=1, coords=None):
        self.size = size
        self.coords = coords if coords else (0, 0, 0)

    def __repr__(self):
        return '<%s x%.2f @ %s>' % (self.__class__.__name__, self.size, self.coords)

class SphereObject(SceneObject):
    image = Image.open(SPHERE_IMAGE)

class CubeObject(SceneObject):
    image = Image.open(CUBE_IMAGE)
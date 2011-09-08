from __future__ import division

import random
import Tkinter
from PIL import ImageTk
from . import Scene, SphereObject, CubeObject

def demo():
    current_image = None
    scene = Scene()
    w, h = scene.img_size

    def update_image():
        global current_image
        current_image = ImageTk.PhotoImage(scene.render())
        canvas.create_image(0, 0, image=current_image, anchor=Tkinter.NW)

    def reset_scene(event=None):
        scene.clear_objects()

        # Performance benchmarking
        # for i in range(-4, 5):
        #     for j in range(-4, 5):
        #         for k in range(-4, 5):
        #             scene.add_object(SphereObject(0.1, (i*0.1, j*0.1, k*0.1)))

        # for _ in xrange(4):
        #     klass = random.choice([SphereObject, CubeObject])
        #     obj = klass(size=random.uniform(0.1, 0.5),
        #                 coords=(random.uniform(-0.45,0.45),
        #                         random.uniform(-0.45,0.45),
        #                         random.uniform(-0.45,0.45)))
        #     scene.add_object(obj)

        for klass in (SphereObject, CubeObject):
            obj = klass(size=random.uniform(0.1, 0.5),
                        coords=(random.uniform(-0.45,0.45),
                                random.uniform(-0.45,0.45),
                                random.uniform(-0.45,0.45)))
            scene.add_object(obj)
        update_image()

    def on_motion(event):
        x, y = event.x - w // 2, -(event.y - h // 2)
        scene.eye_coords = (x / w, y / h)
        update_image()

    def quit(event):
        root.destroy()

    root = Tkinter.Tk()

    canvas = Tkinter.Canvas(root, width=w, height=h, background="#000000")
    canvas.pack()

    root.bind('<Motion>', on_motion)
    root.bind('q', quit)
    root.bind('<space>', reset_scene)

    reset_scene()
    root.mainloop()
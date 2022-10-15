from model_elements import PoligonalModel, Flash, Camera, Scene


class IModelChangedObserver:
    def __init__(self, num):
        self.num = num

    def apply_update_model(self):
        return self.num


class IModelChanger:
    def __init__(self, num):
        self.num = num

    def notify_change(self):
        return self.num


class ModelStore:
    def __init__(self, models, scenes, flashes, cameras, change_observers):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self._change_observers = change_observers

    def get_scena(self):
        return self.scenes

    def notify_change(self):
        return IModelChanger.notify_change(self.models)


if "__name__" == "__main__":
    a = PoligonalModel(10, 20)
    b = Flash(1, 90, "red", 80)
    c = Camera(1, 180)
    d = Scene(1, a, b)

    mod = ModelStore(a, d, b, c, 1)
    print(mod.get_scena())
    print(mod.notify_change())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from typing import List

from abc import *

# ˄
from accommodation_manager.image_manager.image import Image
from accommodation_manager.model_3d_manager.model_3d import Model3D


class Accommodable(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def add_model(self, m: Model3D):
        # ˅
        pass
        # ˄

    @abstractmethod
    def add_image(self, img: Image):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_models(self) -> List[Model3D]:
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_images(self) -> List[Image]:
        # ˅
        pass
        # ˄

    # ˅

    # ˄

# ˅

# ˄

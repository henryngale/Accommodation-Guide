#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from typing import List

from accommodation_manager.accommodable import Accommodable
from accommodation_manager.image_manager.image import Image
from accommodation_manager.model_3d_manager.model_3d import Model3D


class AccommodationDomain(Accommodable):
    def add_model(self, m: Model3D):
        pass

    def add_image(self, img: Image):
        pass

    def get_models(self) -> List[Model3D]:
        pass

    def get_images(self) -> List[Image]:
        pass

    def add(self, s):
        # ˅
        pass
        # ˄

    def get(self):
        # ˅
        pass
        # ˄

    def get_accommodations(self) -> List[Accommodable]:
        # ˅
        pass
        # ˄

    def delete_domain(self, s):
        # ˅
        pass
        # ˄

    def delete(self, a: Accommodable):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

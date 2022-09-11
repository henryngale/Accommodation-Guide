#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄
from accommodation_manager.accommodable import Accommodable
from accommodation_manager.image_manager.image import Image


class AgentImageIntegretor(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def add_image(self, img: Image, ac, ag):
        # ˅
        pass
        # ˄

    @abstractmethod
    def remove_mage(self, ac: Accommodable, img: Image):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from Henry.package.AccommodationManager.Geolocalisation.position import Position
from abc import *


# ˄


class Accommodable(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def addModel(self, m):
        # ˅
        pass
        # ˄

    @abstractmethod
    def addImage(self, Img):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getModels(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getImages(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

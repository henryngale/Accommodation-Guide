#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from Henry.package.AccommodationManager.Geolocalisation.accommodation_locator import AccommodationLocator
from Henry.package.AccommodationManager.Geolocalisation.position import Position


# ˄


class Locator(AccommodationLocator):
    # ˅
    
    # ˄

    @abstractmethod
    def setLocation(self, ac, position):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getLogation(self, ac):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

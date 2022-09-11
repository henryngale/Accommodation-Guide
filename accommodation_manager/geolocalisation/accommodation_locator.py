#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class AccommodationLocator(object, metaclass=ABCMeta):
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

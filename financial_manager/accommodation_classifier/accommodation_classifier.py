#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class AccommodationClassifier(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def getCathegories(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getCathegory(self, a):
        # ˅
        pass
        # ˄

    @abstractmethod
    def serCatherogy(self, a, c):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getTypes(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getLevels(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getRanks(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getAmount(self, c, nbAccommodation):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

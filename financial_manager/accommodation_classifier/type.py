#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from Henry.package.FinancialManager.AccommodationClassifier.level import Level
from abc import *


# ˄


class Type(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def getLevel(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getIndice(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

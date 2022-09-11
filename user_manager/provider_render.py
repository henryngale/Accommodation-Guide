#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class ProviderRender(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def getProviders(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def searchProviders(self, v, maxItems):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getProviderInfos(self, p):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

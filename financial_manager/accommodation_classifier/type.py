#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from level import Level
from abc import *


# ˄


class Type(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def get_level(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_indice(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class AccommodationClassifier(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def get_categories(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_category(self, a):
        # ˅
        pass
        # ˄

    @abstractmethod
    def set_category(self, a, c):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_types(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_levels(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_ranks(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_amount(self, c, nb_accommodation):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

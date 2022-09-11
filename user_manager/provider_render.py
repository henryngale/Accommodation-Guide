#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class ProviderRender(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def get_providers(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def search_providers(self, v, max_items):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_provider_infos(self, p):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

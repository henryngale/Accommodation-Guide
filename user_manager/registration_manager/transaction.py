#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from validator.validator import Validator
from abc import *


# ˄


class Transaction(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def validate(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

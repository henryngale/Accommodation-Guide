#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *


# ˄


class AgentStateProvider(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def getStates(self, a):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getStateInRange(self, a, begin, end):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getStatesAmount(self, a, begin, end):
        # ˅
        pass
        # ˄

    @abstractmethod
    def operation2(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getAgentStates(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

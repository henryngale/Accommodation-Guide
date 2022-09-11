#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from Henry.package.FinancialManager.Account.ads_account import AdsAccount
from Henry.package.FinancialManager.AgentState.agent_state_provider import AgentStateProvider
from Henry.package.FinancialManager.resgistrator import Resgistrator
from Henry.package.UserManager.adminstrator import Adminstrator


# ˄


class FinancialManager(Adminstrator):
    # ˅
    
    # ˄

    def validatePreregistration(self, p):
        # ˅
        pass
        # ˄

    def setUpAgentState(self, agent, AgentState):
        # ˅
        pass
        # ˄

    def getAgentStates(self):
        # ˅
        pass
        # ˄

    def addAdsAccout(self, acc):
        # ˅
        pass
        # ˄

    def removeAdsAccount(self, ac):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getCathegories(self):
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
    def getLevels(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def getTypes(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄

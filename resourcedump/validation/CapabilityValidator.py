#######################################################
# 
# CapabilityValidator.py
# Python implementation of the Class CapabilityValidator
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:12:01 AM
# Original author: talve
# 
#######################################################
from fetchers.CapabilityFetcher import CapabilityFetcher


class CapabilityValidator:
    """this class is responsible for validating the capability of the core dump
    register.
    """
    CAP_BIT_VALUE = 0x0200000

    @classmethod
    def _fetch_cap(cls):
        """fetch the core dump capability bit by calling the CapabilityFetcher.
        """
        return CapabilityFetcher.fetch()

    @classmethod
    def validate(cls):
        """validate if core dump register is supported by checking the capability.
        """
        capability_value = cls._fetch_cap()

        if (capability_value & cls.CAP_BIT_VALUE) > 0:
            return True

        return False

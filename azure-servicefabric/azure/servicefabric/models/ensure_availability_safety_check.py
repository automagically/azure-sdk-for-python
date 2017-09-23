# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .partition_safety_check import PartitionSafetyCheck


class EnsureAvailabilitySafetyCheck(PartitionSafetyCheck):
    """Safety check that waits to ensure the availability of the partition. It
    waits until there are replicas available such that bringing down this
    replica will not cause availability loss for the partition.

    :param kind: Polymorphic Discriminator
    :type kind: str
    :param partition_id:
    :type partition_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    def __init__(self, partition_id=None):
        super(EnsureAvailabilitySafetyCheck, self).__init__(partition_id=partition_id)
        self.kind = 'EnsureAvailability'

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

from .aad_metadata import AadMetadata
from .aad_metadata_object import AadMetadataObject
from .service_health_state import ServiceHealthState
from .deployed_application_health_state import DeployedApplicationHealthState
from .application_health import ApplicationHealth
from .health_evaluation import HealthEvaluation
from .health_evaluation_wrapper import HealthEvaluationWrapper
from .application_health_evaluation import ApplicationHealthEvaluation
from .service_type_health_policy import ServiceTypeHealthPolicy
from .service_type_health_policy_map_item import ServiceTypeHealthPolicyMapItem
from .application_health_policy import ApplicationHealthPolicy
from .application_health_policy_map_item import ApplicationHealthPolicyMapItem
from .application_health_policies import ApplicationHealthPolicies
from .application_health_state import ApplicationHealthState
from .replica_health_state_chunk import ReplicaHealthStateChunk
from .replica_health_state_chunk_list import ReplicaHealthStateChunkList
from .partition_health_state_chunk import PartitionHealthStateChunk
from .partition_health_state_chunk_list import PartitionHealthStateChunkList
from .service_health_state_chunk import ServiceHealthStateChunk
from .service_health_state_chunk_list import ServiceHealthStateChunkList
from .deployed_service_package_health_state_chunk import DeployedServicePackageHealthStateChunk
from .deployed_service_package_health_state_chunk_list import DeployedServicePackageHealthStateChunkList
from .deployed_application_health_state_chunk import DeployedApplicationHealthStateChunk
from .deployed_application_health_state_chunk_list import DeployedApplicationHealthStateChunkList
from .application_health_state_chunk import ApplicationHealthStateChunk
from .application_health_state_chunk_list import ApplicationHealthStateChunkList
from .replica_health_state_filter import ReplicaHealthStateFilter
from .partition_health_state_filter import PartitionHealthStateFilter
from .service_health_state_filter import ServiceHealthStateFilter
from .deployed_service_package_health_state_filter import DeployedServicePackageHealthStateFilter
from .deployed_application_health_state_filter import DeployedApplicationHealthStateFilter
from .application_health_state_filter import ApplicationHealthStateFilter
from .application_parameter import ApplicationParameter
from .application_info import ApplicationInfo
from .application_metric_description import ApplicationMetricDescription
from .application_load_info import ApplicationLoadInfo
from .application_name_info import ApplicationNameInfo
from .applications_health_evaluation import ApplicationsHealthEvaluation
from .application_type_applications_health_evaluation import ApplicationTypeApplicationsHealthEvaluation
from .application_type_health_policy_map_item import ApplicationTypeHealthPolicyMapItem
from .application_type_info import ApplicationTypeInfo
from .paged_application_type_info_list import PagedApplicationTypeInfoList
from .application_type_manifest import ApplicationTypeManifest
from .monitoring_policy_description import MonitoringPolicyDescription
from .application_upgrade_description import ApplicationUpgradeDescription
from .upgrade_domain_info import UpgradeDomainInfo
from .safety_check import SafetyCheck
from .safety_check_wrapper import SafetyCheckWrapper
from .node_upgrade_progress_info import NodeUpgradeProgressInfo
from .current_upgrade_domain_progress_info import CurrentUpgradeDomainProgressInfo
from .failure_upgrade_domain_progress_info import FailureUpgradeDomainProgressInfo
from .application_upgrade_progress_info import ApplicationUpgradeProgressInfo
from .cluster_configuration import ClusterConfiguration
from .node_id import NodeId
from .node_health_state import NodeHealthState
from .cluster_health import ClusterHealth
from .node_health_state_chunk import NodeHealthStateChunk
from .node_health_state_chunk_list import NodeHealthStateChunkList
from .cluster_health_chunk import ClusterHealthChunk
from .node_health_state_filter import NodeHealthStateFilter
from .cluster_health_policy import ClusterHealthPolicy
from .cluster_health_chunk_query_description import ClusterHealthChunkQueryDescription
from .cluster_health_policies import ClusterHealthPolicies
from .cluster_manifest import ClusterManifest
from .deactivation_intent_description import DeactivationIntentDescription
from .delta_nodes_check_health_evaluation import DeltaNodesCheckHealthEvaluation
from .deployed_service_package_health_state import DeployedServicePackageHealthState
from .deployed_application_health import DeployedApplicationHealth
from .deployed_application_health_evaluation import DeployedApplicationHealthEvaluation
from .deployed_application_info import DeployedApplicationInfo
from .deployed_applications_health_evaluation import DeployedApplicationsHealthEvaluation
from .deployed_service_package_health import DeployedServicePackageHealth
from .deployed_service_package_health_evaluation import DeployedServicePackageHealthEvaluation
from .deployed_service_packages_health_evaluation import DeployedServicePackagesHealthEvaluation
from .deployed_service_replica_info import DeployedServiceReplicaInfo
from .reconfiguration_information import ReconfigurationInformation
from .deployed_stateful_service_replica_info import DeployedStatefulServiceReplicaInfo
from .deployed_stateless_service_instance_info import DeployedStatelessServiceInstanceInfo
from .health_event import HealthEvent
from .health_state_count import HealthStateCount
from .entity_kind_health_state_count import EntityKindHealthStateCount
from .health_statistics import HealthStatistics
from .entity_health import EntityHealth
from .entity_health_state import EntityHealthState
from .entity_health_state_chunk import EntityHealthStateChunk
from .entity_health_state_chunk_list import EntityHealthStateChunkList
from .epoch import Epoch
from .event_health_evaluation import EventHealthEvaluation
from .fabric_code_version_info import FabricCodeVersionInfo
from .fabric_config_version_info import FabricConfigVersionInfo
from .fabric_error_error import FabricErrorError
from .fabric_error import FabricError, FabricErrorException
from .cluster_configuration_upgrade_status_info import ClusterConfigurationUpgradeStatusInfo
from .health_information import HealthInformation
from .int64_range_partition_information import Int64RangePartitionInformation
from .named_partition_information import NamedPartitionInformation
from .node_deactivation_task_id import NodeDeactivationTaskId
from .node_deactivation_task import NodeDeactivationTask
from .node_deactivation_info import NodeDeactivationInfo
from .node_health import NodeHealth
from .node_health_evaluation import NodeHealthEvaluation
from .node_info import NodeInfo
from .node_load_metric_information import NodeLoadMetricInformation
from .node_load_info import NodeLoadInfo
from .nodes_health_evaluation import NodesHealthEvaluation
from .paged_application_info_list import PagedApplicationInfoList
from .paged_node_info_list import PagedNodeInfoList
from .partition_information import PartitionInformation
from .service_partition_info import ServicePartitionInfo
from .paged_service_partition_info_list import PagedServicePartitionInfoList
from .replica_info import ReplicaInfo
from .paged_replica_info_list import PagedReplicaInfoList
from .service_info import ServiceInfo
from .paged_service_info_list import PagedServiceInfoList
from .replica_health_state import ReplicaHealthState
from .partition_health import PartitionHealth
from .partition_health_evaluation import PartitionHealthEvaluation
from .partition_health_state import PartitionHealthState
from .provision_fabric_description import ProvisionFabricDescription
from .unprovision_fabric_description import UnprovisionFabricDescription
from .resume_cluster_upgrade_description import ResumeClusterUpgradeDescription
from .cluster_upgrade_health_policy_object import ClusterUpgradeHealthPolicyObject
from .start_cluster_upgrade_description import StartClusterUpgradeDescription
from .rolling_upgrade_update_description import RollingUpgradeUpdateDescription
from .update_cluster_upgrade_description import UpdateClusterUpgradeDescription
from .partition_safety_check import PartitionSafetyCheck
from .ensure_availability_safety_check import EnsureAvailabilitySafetyCheck
from .ensure_partition_qurum_safety_check import EnsurePartitionQurumSafetyCheck
from .seed_node_safety_check import SeedNodeSafetyCheck
from .partitions_health_evaluation import PartitionsHealthEvaluation
from .replica_health import ReplicaHealth
from .replica_health_evaluation import ReplicaHealthEvaluation
from .replicas_health_evaluation import ReplicasHealthEvaluation
from .restart_node_description import RestartNodeDescription
from .service_from_template_description import ServiceFromTemplateDescription
from .service_health_evaluation import ServiceHealthEvaluation
from .service_health import ServiceHealth
from .service_name_info import ServiceNameInfo
from .service_placement_invalid_domain_policy_description import ServicePlacementInvalidDomainPolicyDescription
from .service_placement_non_partially_place_service_policy_description import ServicePlacementNonPartiallyPlaceServicePolicyDescription
from .service_placement_policy_description import ServicePlacementPolicyDescription
from .service_placement_prefer_primary_domain_policy_description import ServicePlacementPreferPrimaryDomainPolicyDescription
from .service_placement_required_domain_policy_description import ServicePlacementRequiredDomainPolicyDescription
from .service_placement_require_domain_distribution_policy_description import ServicePlacementRequireDomainDistributionPolicyDescription
from .services_health_evaluation import ServicesHealthEvaluation
from .service_type_extension_description import ServiceTypeExtensionDescription
from .service_type_description import ServiceTypeDescription
from .service_type_info import ServiceTypeInfo
from .service_type_manifest import ServiceTypeManifest
from .singleton_partition_information import SingletonPartitionInformation
from .stateful_service_info import StatefulServiceInfo
from .stateful_service_partition_info import StatefulServicePartitionInfo
from .stateful_service_replica_health import StatefulServiceReplicaHealth
from .stateful_service_replica_health_state import StatefulServiceReplicaHealthState
from .stateful_service_type_description import StatefulServiceTypeDescription
from .stateless_service_info import StatelessServiceInfo
from .stateless_service_instance_health import StatelessServiceInstanceHealth
from .stateless_service_instance_health_state import StatelessServiceInstanceHealthState
from .stateless_service_partition_info import StatelessServicePartitionInfo
from .stateless_service_type_description import StatelessServiceTypeDescription
from .system_application_health_evaluation import SystemApplicationHealthEvaluation
from .upgrade_domain_delta_nodes_check_health_evaluation import UpgradeDomainDeltaNodesCheckHealthEvaluation
from .upgrade_domain_nodes_health_evaluation import UpgradeDomainNodesHealthEvaluation
from .wait_for_inbuild_replica_safety_check import WaitForInbuildReplicaSafetyCheck
from .wait_for_primary_placement_safety_check import WaitForPrimaryPlacementSafetyCheck
from .wait_for_primary_swap_safety_check import WaitForPrimarySwapSafetyCheck
from .wait_for_reconfiguration_safety_check import WaitForReconfigurationSafetyCheck
from .load_metric_report import LoadMetricReport
from .partition_load_information import PartitionLoadInformation
from .stateful_service_replica_info import StatefulServiceReplicaInfo
from .stateless_service_instance_info import StatelessServiceInstanceInfo
from .cluster_upgrade_description_object import ClusterUpgradeDescriptionObject
from .failed_upgrade_domain_progress_object import FailedUpgradeDomainProgressObject
from .cluster_upgrade_progress_object import ClusterUpgradeProgressObject
from .cluster_configuration_upgrade_description import ClusterConfigurationUpgradeDescription
from .application_type_image_store_path import ApplicationTypeImageStorePath
from .application_type_image_store_version import ApplicationTypeImageStoreVersion
from .code_package_entry_point_statistics import CodePackageEntryPointStatistics
from .code_package_entry_point import CodePackageEntryPoint
from .deployed_code_package_info import DeployedCodePackageInfo
from .chaos_context_map_item import ChaosContextMapItem
from .chaos_context import ChaosContext
from .chaos_parameters import ChaosParameters
from .chaos_event import ChaosEvent
from .chaos_event_wrapper import ChaosEventWrapper
from .chaos_report import ChaosReport
from .executing_faults_chaos_event import ExecutingFaultsChaosEvent
from .started_chaos_event import StartedChaosEvent
from .stopped_chaos_event import StoppedChaosEvent
from .test_error_chaos_event import TestErrorChaosEvent
from .validation_failed_chaos_event import ValidationFailedChaosEvent
from .waiting_chaos_event import WaitingChaosEvent
from .application_capacity_description import ApplicationCapacityDescription
from .application_description import ApplicationDescription
from .compose_deployment_status_info import ComposeDeploymentStatusInfo
from .registry_credential import RegistryCredential
from .compose_deployment_upgrade_description import ComposeDeploymentUpgradeDescription
from .compose_deployment_upgrade_progress_info import ComposeDeploymentUpgradeProgressInfo
from .paged_compose_deployment_status_info_list import PagedComposeDeploymentStatusInfoList
from .create_compose_deployment_description import CreateComposeDeploymentDescription
from .deployed_service_package_info import DeployedServicePackageInfo
from .service_correlation_description import ServiceCorrelationDescription
from .service_load_metric_description import ServiceLoadMetricDescription
from .partition_scheme_description import PartitionSchemeDescription
from .named_partition_scheme_description import NamedPartitionSchemeDescription
from .singleton_partition_scheme_description import SingletonPartitionSchemeDescription
from .uniform_int64_range_partition_scheme_description import UniformInt64RangePartitionSchemeDescription
from .service_description import ServiceDescription
from .stateful_service_description import StatefulServiceDescription
from .stateless_service_description import StatelessServiceDescription
from .replicator_queue_status import ReplicatorQueueStatus
from .replicator_status import ReplicatorStatus
from .remote_replicator_acknowledgement_detail import RemoteReplicatorAcknowledgementDetail
from .remote_replicator_acknowledgement_status import RemoteReplicatorAcknowledgementStatus
from .remote_replicator_status import RemoteReplicatorStatus
from .primary_replicator_status import PrimaryReplicatorStatus
from .secondary_replicator_status import SecondaryReplicatorStatus
from .secondary_active_replicator_status import SecondaryActiveReplicatorStatus
from .secondary_idle_replicator_status import SecondaryIdleReplicatorStatus
from .load_metric_report_info import LoadMetricReportInfo
from .deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo
from .key_value_store_replica_status import KeyValueStoreReplicaStatus
from .deployed_stateful_service_replica_detail_info import DeployedStatefulServiceReplicaDetailInfo
from .deployed_stateless_service_instance_detail_info import DeployedStatelessServiceInstanceDetailInfo
from .replica_status_base import ReplicaStatusBase
from .service_update_description import ServiceUpdateDescription
from .stateful_service_update_description import StatefulServiceUpdateDescription
from .stateless_service_update_description import StatelessServiceUpdateDescription
from .file_version import FileVersion
from .file_info import FileInfo
from .folder_info import FolderInfo
from .image_store_content import ImageStoreContent
from .image_store_copy_description import ImageStoreCopyDescription
from .restart_deployed_code_package_description import RestartDeployedCodePackageDescription
from .deployed_service_type_info import DeployedServiceTypeInfo
from .resolved_service_endpoint import ResolvedServiceEndpoint
from .resolved_service_partition import ResolvedServicePartition
from .selected_partition import SelectedPartition
from .invoke_data_loss_result import InvokeDataLossResult
from .invoke_quorum_loss_result import InvokeQuorumLossResult
from .node_result import NodeResult
from .node_transition_result import NodeTransitionResult
from .node_transition_progress import NodeTransitionProgress
from .operation_status import OperationStatus
from .partition_data_loss_progress import PartitionDataLossProgress
from .partition_quorum_loss_progress import PartitionQuorumLossProgress
from .restart_partition_result import RestartPartitionResult
from .partition_restart_progress import PartitionRestartProgress
from .package_sharing_policy_info import PackageSharingPolicyInfo
from .deploy_service_package_to_node_description import DeployServicePackageToNodeDescription
from .resume_application_upgrade_description import ResumeApplicationUpgradeDescription
from .application_upgrade_update_description import ApplicationUpgradeUpdateDescription
from .node_impact import NodeImpact
from .node_repair_impact_description import NodeRepairImpactDescription
from .node_repair_target_description import NodeRepairTargetDescription
from .repair_impact_description_base import RepairImpactDescriptionBase
from .repair_target_description_base import RepairTargetDescriptionBase
from .repair_task_history import RepairTaskHistory
from .repair_task import RepairTask
from .repair_task_approve_description import RepairTaskApproveDescription
from .repair_task_cancel_description import RepairTaskCancelDescription
from .repair_task_delete_description import RepairTaskDeleteDescription
from .repair_task_update_health_policy_description import RepairTaskUpdateHealthPolicyDescription
from .repair_task_update_info import RepairTaskUpdateInfo

__all__ = [
    'AadMetadata',
    'AadMetadataObject',
    'ServiceHealthState',
    'DeployedApplicationHealthState',
    'ApplicationHealth',
    'HealthEvaluation',
    'HealthEvaluationWrapper',
    'ApplicationHealthEvaluation',
    'ServiceTypeHealthPolicy',
    'ServiceTypeHealthPolicyMapItem',
    'ApplicationHealthPolicy',
    'ApplicationHealthPolicyMapItem',
    'ApplicationHealthPolicies',
    'ApplicationHealthState',
    'ReplicaHealthStateChunk',
    'ReplicaHealthStateChunkList',
    'PartitionHealthStateChunk',
    'PartitionHealthStateChunkList',
    'ServiceHealthStateChunk',
    'ServiceHealthStateChunkList',
    'DeployedServicePackageHealthStateChunk',
    'DeployedServicePackageHealthStateChunkList',
    'DeployedApplicationHealthStateChunk',
    'DeployedApplicationHealthStateChunkList',
    'ApplicationHealthStateChunk',
    'ApplicationHealthStateChunkList',
    'ReplicaHealthStateFilter',
    'PartitionHealthStateFilter',
    'ServiceHealthStateFilter',
    'DeployedServicePackageHealthStateFilter',
    'DeployedApplicationHealthStateFilter',
    'ApplicationHealthStateFilter',
    'ApplicationParameter',
    'ApplicationInfo',
    'ApplicationMetricDescription',
    'ApplicationLoadInfo',
    'ApplicationNameInfo',
    'ApplicationsHealthEvaluation',
    'ApplicationTypeApplicationsHealthEvaluation',
    'ApplicationTypeHealthPolicyMapItem',
    'ApplicationTypeInfo',
    'PagedApplicationTypeInfoList',
    'ApplicationTypeManifest',
    'MonitoringPolicyDescription',
    'ApplicationUpgradeDescription',
    'UpgradeDomainInfo',
    'SafetyCheck',
    'SafetyCheckWrapper',
    'NodeUpgradeProgressInfo',
    'CurrentUpgradeDomainProgressInfo',
    'FailureUpgradeDomainProgressInfo',
    'ApplicationUpgradeProgressInfo',
    'ClusterConfiguration',
    'NodeId',
    'NodeHealthState',
    'ClusterHealth',
    'NodeHealthStateChunk',
    'NodeHealthStateChunkList',
    'ClusterHealthChunk',
    'NodeHealthStateFilter',
    'ClusterHealthPolicy',
    'ClusterHealthChunkQueryDescription',
    'ClusterHealthPolicies',
    'ClusterManifest',
    'DeactivationIntentDescription',
    'DeltaNodesCheckHealthEvaluation',
    'DeployedServicePackageHealthState',
    'DeployedApplicationHealth',
    'DeployedApplicationHealthEvaluation',
    'DeployedApplicationInfo',
    'DeployedApplicationsHealthEvaluation',
    'DeployedServicePackageHealth',
    'DeployedServicePackageHealthEvaluation',
    'DeployedServicePackagesHealthEvaluation',
    'DeployedServiceReplicaInfo',
    'ReconfigurationInformation',
    'DeployedStatefulServiceReplicaInfo',
    'DeployedStatelessServiceInstanceInfo',
    'HealthEvent',
    'HealthStateCount',
    'EntityKindHealthStateCount',
    'HealthStatistics',
    'EntityHealth',
    'EntityHealthState',
    'EntityHealthStateChunk',
    'EntityHealthStateChunkList',
    'Epoch',
    'EventHealthEvaluation',
    'FabricCodeVersionInfo',
    'FabricConfigVersionInfo',
    'FabricErrorError',
    'FabricError', 'FabricErrorException',
    'ClusterConfigurationUpgradeStatusInfo',
    'HealthInformation',
    'Int64RangePartitionInformation',
    'NamedPartitionInformation',
    'NodeDeactivationTaskId',
    'NodeDeactivationTask',
    'NodeDeactivationInfo',
    'NodeHealth',
    'NodeHealthEvaluation',
    'NodeInfo',
    'NodeLoadMetricInformation',
    'NodeLoadInfo',
    'NodesHealthEvaluation',
    'PagedApplicationInfoList',
    'PagedNodeInfoList',
    'PartitionInformation',
    'ServicePartitionInfo',
    'PagedServicePartitionInfoList',
    'ReplicaInfo',
    'PagedReplicaInfoList',
    'ServiceInfo',
    'PagedServiceInfoList',
    'ReplicaHealthState',
    'PartitionHealth',
    'PartitionHealthEvaluation',
    'PartitionHealthState',
    'ProvisionFabricDescription',
    'UnprovisionFabricDescription',
    'ResumeClusterUpgradeDescription',
    'ClusterUpgradeHealthPolicyObject',
    'StartClusterUpgradeDescription',
    'RollingUpgradeUpdateDescription',
    'UpdateClusterUpgradeDescription',
    'PartitionSafetyCheck',
    'EnsureAvailabilitySafetyCheck',
    'EnsurePartitionQurumSafetyCheck',
    'SeedNodeSafetyCheck',
    'PartitionsHealthEvaluation',
    'ReplicaHealth',
    'ReplicaHealthEvaluation',
    'ReplicasHealthEvaluation',
    'RestartNodeDescription',
    'ServiceFromTemplateDescription',
    'ServiceHealthEvaluation',
    'ServiceHealth',
    'ServiceNameInfo',
    'ServicePlacementInvalidDomainPolicyDescription',
    'ServicePlacementNonPartiallyPlaceServicePolicyDescription',
    'ServicePlacementPolicyDescription',
    'ServicePlacementPreferPrimaryDomainPolicyDescription',
    'ServicePlacementRequiredDomainPolicyDescription',
    'ServicePlacementRequireDomainDistributionPolicyDescription',
    'ServicesHealthEvaluation',
    'ServiceTypeExtensionDescription',
    'ServiceTypeDescription',
    'ServiceTypeInfo',
    'ServiceTypeManifest',
    'SingletonPartitionInformation',
    'StatefulServiceInfo',
    'StatefulServicePartitionInfo',
    'StatefulServiceReplicaHealth',
    'StatefulServiceReplicaHealthState',
    'StatefulServiceTypeDescription',
    'StatelessServiceInfo',
    'StatelessServiceInstanceHealth',
    'StatelessServiceInstanceHealthState',
    'StatelessServicePartitionInfo',
    'StatelessServiceTypeDescription',
    'SystemApplicationHealthEvaluation',
    'UpgradeDomainDeltaNodesCheckHealthEvaluation',
    'UpgradeDomainNodesHealthEvaluation',
    'WaitForInbuildReplicaSafetyCheck',
    'WaitForPrimaryPlacementSafetyCheck',
    'WaitForPrimarySwapSafetyCheck',
    'WaitForReconfigurationSafetyCheck',
    'LoadMetricReport',
    'PartitionLoadInformation',
    'StatefulServiceReplicaInfo',
    'StatelessServiceInstanceInfo',
    'ClusterUpgradeDescriptionObject',
    'FailedUpgradeDomainProgressObject',
    'ClusterUpgradeProgressObject',
    'ClusterConfigurationUpgradeDescription',
    'ApplicationTypeImageStorePath',
    'ApplicationTypeImageStoreVersion',
    'CodePackageEntryPointStatistics',
    'CodePackageEntryPoint',
    'DeployedCodePackageInfo',
    'ChaosContextMapItem',
    'ChaosContext',
    'ChaosParameters',
    'ChaosEvent',
    'ChaosEventWrapper',
    'ChaosReport',
    'ExecutingFaultsChaosEvent',
    'StartedChaosEvent',
    'StoppedChaosEvent',
    'TestErrorChaosEvent',
    'ValidationFailedChaosEvent',
    'WaitingChaosEvent',
    'ApplicationCapacityDescription',
    'ApplicationDescription',
    'ComposeDeploymentStatusInfo',
    'RegistryCredential',
    'ComposeDeploymentUpgradeDescription',
    'ComposeDeploymentUpgradeProgressInfo',
    'PagedComposeDeploymentStatusInfoList',
    'CreateComposeDeploymentDescription',
    'DeployedServicePackageInfo',
    'ServiceCorrelationDescription',
    'ServiceLoadMetricDescription',
    'PartitionSchemeDescription',
    'NamedPartitionSchemeDescription',
    'SingletonPartitionSchemeDescription',
    'UniformInt64RangePartitionSchemeDescription',
    'ServiceDescription',
    'StatefulServiceDescription',
    'StatelessServiceDescription',
    'ReplicatorQueueStatus',
    'ReplicatorStatus',
    'RemoteReplicatorAcknowledgementDetail',
    'RemoteReplicatorAcknowledgementStatus',
    'RemoteReplicatorStatus',
    'PrimaryReplicatorStatus',
    'SecondaryReplicatorStatus',
    'SecondaryActiveReplicatorStatus',
    'SecondaryIdleReplicatorStatus',
    'LoadMetricReportInfo',
    'DeployedServiceReplicaDetailInfo',
    'KeyValueStoreReplicaStatus',
    'DeployedStatefulServiceReplicaDetailInfo',
    'DeployedStatelessServiceInstanceDetailInfo',
    'ReplicaStatusBase',
    'ServiceUpdateDescription',
    'StatefulServiceUpdateDescription',
    'StatelessServiceUpdateDescription',
    'FileVersion',
    'FileInfo',
    'FolderInfo',
    'ImageStoreContent',
    'ImageStoreCopyDescription',
    'RestartDeployedCodePackageDescription',
    'DeployedServiceTypeInfo',
    'ResolvedServiceEndpoint',
    'ResolvedServicePartition',
    'SelectedPartition',
    'InvokeDataLossResult',
    'InvokeQuorumLossResult',
    'NodeResult',
    'NodeTransitionResult',
    'NodeTransitionProgress',
    'OperationStatus',
    'PartitionDataLossProgress',
    'PartitionQuorumLossProgress',
    'RestartPartitionResult',
    'PartitionRestartProgress',
    'PackageSharingPolicyInfo',
    'DeployServicePackageToNodeDescription',
    'ResumeApplicationUpgradeDescription',
    'ApplicationUpgradeUpdateDescription',
    'NodeImpact',
    'NodeRepairImpactDescription',
    'NodeRepairTargetDescription',
    'RepairImpactDescriptionBase',
    'RepairTargetDescriptionBase',
    'RepairTaskHistory',
    'RepairTask',
    'RepairTaskApproveDescription',
    'RepairTaskCancelDescription',
    'RepairTaskDeleteDescription',
    'RepairTaskUpdateHealthPolicyDescription',
    'RepairTaskUpdateInfo',
]

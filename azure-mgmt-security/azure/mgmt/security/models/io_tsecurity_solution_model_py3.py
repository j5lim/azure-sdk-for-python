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

from msrest.serialization import Model


class IoTSecuritySolutionModel(Model):
    """Security Solution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param location: The resource location.
    :type location: str
    :param workspace_resource_id: The full Azure ID of the workspace to save
     the data in
    :type workspace_resource_id: str
    :param workspace_customer_id: the customer id associate with the workspace
    :type workspace_customer_id: str
    :param display_name: Required. The display name.
    :type display_name: str
    :param enabled: Is the solution Enabled for the customer. Default value:
     True .
    :type enabled: bool
    :param export: list of additional data to export by the system
    :type export: list[str or ~azure.mgmt.security.models.ExtraData]
    :param iot_hubs: Required. Related iot hub resources ID
    :type iot_hubs: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'required': True},
        'iot_hubs': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'workspace_resource_id': {'key': 'properties.workspaceResourceId', 'type': 'str'},
        'workspace_customer_id': {'key': 'properties.workspaceCustomerId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'export': {'key': 'properties.export', 'type': '[str]'},
        'iot_hubs': {'key': 'properties.iotHubs', 'type': '[str]'},
    }

    def __init__(self, *, display_name: str, iot_hubs, tags=None, location: str=None, workspace_resource_id: str=None, workspace_customer_id: str=None, enabled: bool=True, export=None, **kwargs) -> None:
        super(IoTSecuritySolutionModel, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = tags
        self.location = location
        self.workspace_resource_id = workspace_resource_id
        self.workspace_customer_id = workspace_customer_id
        self.display_name = display_name
        self.enabled = enabled
        self.export = export
        self.iot_hubs = iot_hubs

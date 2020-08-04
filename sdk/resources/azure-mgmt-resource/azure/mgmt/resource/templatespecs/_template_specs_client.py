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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import TemplateSpecsClientConfiguration



class TemplateSpecsClient(MultiApiClientMixin, SDKClient):
    """The APIs listed in this specification can be used to manage Template Spec resources through the Azure Resource Manager.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: TemplateSpecsClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-06-01-preview'
    _PROFILE_TAG = "azure.mgmt.resource.templatespecs.TemplateSpecsClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = TemplateSpecsClientConfiguration(credentials, subscription_id, base_url)
        super(TemplateSpecsClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-06-01-preview: :mod:`v2019_06_01_preview.models<azure.mgmt.resource.templatespecs.v2019_06_01_preview.models>`
           * 2019-06-01-preview: :mod:`v2019_06_preview.models<azure.mgmt.resource.templatespecs.v2019_06_preview.models>`
        """
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview import models
            return models
        elif api_version == '2019-06-01-preview':
            from .v2019_06_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def template_spec_versions(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.templatespecs.v2019_06_01_preview.operations.TemplateSpecVersionsOperations>`
           * 2019-06-01-preview: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.templatespecs.v2019_06_preview.operations.TemplateSpecVersionsOperations>`
        """
        api_version = self._get_api_version('template_spec_versions')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TemplateSpecVersionsOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_preview.operations import TemplateSpecVersionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def template_specs(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecsOperations<azure.mgmt.resource.templatespecs.v2019_06_01_preview.operations.TemplateSpecsOperations>`
           * 2019-06-01-preview: :class:`TemplateSpecsOperations<azure.mgmt.resource.templatespecs.v2019_06_preview.operations.TemplateSpecsOperations>`
        """
        api_version = self._get_api_version('template_specs')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TemplateSpecsOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_preview.operations import TemplateSpecsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

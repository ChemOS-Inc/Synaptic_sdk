# coding: utf-8

# flake8: noqa
"""
    ChemOS Web Portal

    API entry point for ChemOS Web Portal. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Web Portal account. You can generate your `API KEY` on your [account information page](https://scientia.chemos.io/user).  # noqa: E501

    The version of the OpenAPI document: beta
    Contact: support@chemos.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.available_files_summary import AvailableFilesSummary
from openapi_client.models.create_project_response import CreateProjectResponse
from openapi_client.models.create_project_response_object import CreateProjectResponseObject
from openapi_client.models.generic_response import GenericResponse
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.list_files_response import ListFilesResponse
from openapi_client.models.list_files_response_objects import ListFilesResponseObjects
from openapi_client.models.list_projects_response import ListProjectsResponse
from openapi_client.models.list_projects_response_objects import ListProjectsResponseObjects
from openapi_client.models.project_create_req import ProjectCreateReq
from openapi_client.models.project_detail import ProjectDetail
from openapi_client.models.project_detail_response import ProjectDetailResponse
from openapi_client.models.project_subscribe_req import ProjectSubscribeReq
from openapi_client.models.project_unsubscribe_req import ProjectUnsubscribeReq
from openapi_client.models.project_update_req import ProjectUpdateReq
from openapi_client.models.result import Result
from openapi_client.models.upload_response import UploadResponse
from openapi_client.models.upload_response_object import UploadResponseObject
# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

from lightly.openapi_generated.swagger_client.api_client import ApiClient
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_datasource_by_dataset_id import GetDatasourceByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_datasource_processed_until_timestamp_by_dataset_id import GetDatasourceProcessedUntilTimestampByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_datasources_by_dataset_id import GetDatasourcesByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_list_of_raw_samples_from_datasource_by_dataset_id import GetListOfRawSamplesFromDatasourceByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_list_of_raw_samples_predictions_from_datasource_by_dataset_id import GetListOfRawSamplesPredictionsFromDatasourceByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.get_prediction_file_read_url_from_datasource_by_dataset_id import GetPredictionFileReadUrlFromDatasourceByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.update_datasource_by_dataset_id import UpdateDatasourceByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.update_datasource_processed_until_timestamp_by_dataset_id import UpdateDatasourceProcessedUntilTimestampByDatasetId
from lightly.openapi_generated.swagger_client.api.datasources_api_endpoints.verify_datasource_by_dataset_id import VerifyDatasourceByDatasetId


class DatasourcesApi(
    GetDatasourceByDatasetId,
    GetDatasourceProcessedUntilTimestampByDatasetId,
    GetDatasourcesByDatasetId,
    GetListOfRawSamplesFromDatasourceByDatasetId,
    GetListOfRawSamplesPredictionsFromDatasourceByDatasetId,
    GetPredictionFileReadUrlFromDatasourceByDatasetId,
    UpdateDatasourceByDatasetId,
    UpdateDatasourceProcessedUntilTimestampByDatasetId,
    VerifyDatasourceByDatasetId,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

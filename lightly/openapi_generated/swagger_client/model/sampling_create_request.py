# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from lightly.openapi_generated.swagger_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class SamplingCreateRequest(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'newTagName',
        'method',
        'config',
    ))

    @classmethod
    @property
    def newTagName(cls) -> typing.Type['TagName']:
        return TagName

    @classmethod
    @property
    def method(cls) -> typing.Type['SamplingMethod']:
        return SamplingMethod

    @classmethod
    @property
    def config(cls) -> typing.Type['SamplingConfig']:
        return SamplingConfig

    @classmethod
    @property
    def preselectedTagId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def queryTagId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def scoreType(cls) -> typing.Type['ActiveLearningScoreType']:
        return ActiveLearningScoreType
    rowCount = NumberSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        newTagName: newTagName,
        method: method,
        config: config,
        preselectedTagId: typing.Union['MongoObjectID', Unset] = unset,
        queryTagId: typing.Union['MongoObjectID', Unset] = unset,
        scoreType: typing.Union['ActiveLearningScoreType', Unset] = unset,
        rowCount: typing.Union[rowCount, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SamplingCreateRequest':
        return super().__new__(
            cls,
            *args,
            newTagName=newTagName,
            method=method,
            config=config,
            preselectedTagId=preselectedTagId,
            queryTagId=queryTagId,
            scoreType=scoreType,
            rowCount=rowCount,
            _configuration=_configuration,
            **kwargs,
        )

from lightly.openapi_generated.swagger_client.model.active_learning_score_type import ActiveLearningScoreType
from lightly.openapi_generated.swagger_client.model.mongo_object_id import MongoObjectID
from lightly.openapi_generated.swagger_client.model.sampling_config import SamplingConfig
from lightly.openapi_generated.swagger_client.model.sampling_method import SamplingMethod
from lightly.openapi_generated.swagger_client.model.tag_name import TagName
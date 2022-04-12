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


class TagData(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'id',
        'datasetId',
        'prevTagId',
        'name',
        'bitMaskData',
        'totSize',
        'createdAt',
    ))

    @classmethod
    @property
    def id(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def datasetId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID
    
    
    class prevTagId(
        _SchemaValidator(
            regex=[{
                'pattern': r'^[a-f0-9]{24}$',  # noqa: E501
            }],
        ),
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        StrBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[str, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'prevTagId':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )

    @classmethod
    @property
    def queryTagId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def preselectedTagId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def name(cls) -> typing.Type['TagName']:
        return TagName

    @classmethod
    @property
    def bitMaskData(cls) -> typing.Type['TagBitMaskData']:
        return TagBitMaskData
    totSize = IntSchema

    @classmethod
    @property
    def createdAt(cls) -> typing.Type['Timestamp']:
        return Timestamp

    @classmethod
    @property
    def lastModifiedAt(cls) -> typing.Type['Timestamp']:
        return Timestamp

    @classmethod
    @property
    def changes(cls) -> typing.Type['TagChangeData']:
        return TagChangeData


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: id,
        datasetId: datasetId,
        prevTagId: prevTagId,
        name: name,
        bitMaskData: bitMaskData,
        totSize: totSize,
        createdAt: createdAt,
        queryTagId: typing.Union['MongoObjectID', Unset] = unset,
        preselectedTagId: typing.Union['MongoObjectID', Unset] = unset,
        lastModifiedAt: typing.Union['Timestamp', Unset] = unset,
        changes: typing.Union['TagChangeData', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'TagData':
        return super().__new__(
            cls,
            *args,
            id=id,
            datasetId=datasetId,
            prevTagId=prevTagId,
            name=name,
            bitMaskData=bitMaskData,
            totSize=totSize,
            createdAt=createdAt,
            queryTagId=queryTagId,
            preselectedTagId=preselectedTagId,
            lastModifiedAt=lastModifiedAt,
            changes=changes,
            _configuration=_configuration,
            **kwargs,
        )

from lightly.openapi_generated.swagger_client.model.mongo_object_id import MongoObjectID
from lightly.openapi_generated.swagger_client.model.tag_bit_mask_data import TagBitMaskData
from lightly.openapi_generated.swagger_client.model.tag_change_data import TagChangeData
from lightly.openapi_generated.swagger_client.model.tag_name import TagName
from lightly.openapi_generated.swagger_client.model.timestamp import Timestamp
# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:45:36+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query
from pydantic import conint

from models import (
    BadRequestException,
    ConflictException,
    CreateBrokerResponse,
    CreateConfigurationResponse,
    CreateUserResponse,
    DeleteBrokerResponse,
    DeleteUserResponse,
    DescribeBrokerEngineTypesResponse,
    DescribeBrokerInstanceOptionsResponse,
    DescribeBrokerResponse,
    DescribeConfigurationResponse,
    DescribeConfigurationRevisionResponse,
    DescribeUserResponse,
    ForbiddenException,
    InternalServerErrorException,
    ListBrokersResponse,
    ListConfigurationRevisionsResponse,
    ListConfigurationsResponse,
    ListTagsResponse,
    ListUsersResponse,
    NotFoundException,
    RebootBrokerResponse,
    TagKeys,
    UnauthorizedException,
    UpdateBrokerResponse,
    UpdateConfigurationResponse,
    UpdateUserResponse,
    V1BrokersBrokerIdPutRequest,
    V1BrokersBrokerIdUsersUsernamePostRequest,
    V1BrokersBrokerIdUsersUsernamePutRequest,
    V1BrokersPostRequest,
    V1ConfigurationsConfigurationIdPutRequest,
    V1ConfigurationsPostRequest,
    V1TagsResourceArnPostRequest,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud. A message broker allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols.',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='AmazonMQ',
    version='2017-11-27',
    servers=[
        {
            'description': 'The AmazonMQ multi-region endpoint',
            'url': 'http://mq.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AmazonMQ multi-region endpoint',
            'url': 'https://mq.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AmazonMQ endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://mq.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The AmazonMQ endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://mq.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.get(
    '/v1/broker-engine-types',
    description=""" Describe available engine types and versions. """,
    tags=['broker_type_description'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_broker_engine_types(
    engine_type: Optional[str] = Query(None, alias='engineType'),
    max_results: Optional[conint(ge=1, le=100)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/broker-instance-options',
    description=""" Describe available broker instance options. """,
    tags=['broker_type_description'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_broker_instance_options(
    engine_type: Optional[str] = Query(None, alias='engineType'),
    host_instance_type: Optional[str] = Query(None, alias='hostInstanceType'),
    max_results: Optional[conint(ge=1, le=100)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    storage_type: Optional[str] = Query(None, alias='storageType'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/brokers',
    description=""" Returns a list of all brokers. """,
    tags=[
        'broker_management',
        'user_account_management',
        'configuration_settings_management',
        'resource_tagging_operations',
        'broker_type_description',
    ],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_brokers(
    max_results: Union[
        Optional[conint(ge=1, le=100)], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='maxResults'),
    next_token: Union[
        Optional[str], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/brokers',
    description=""" <p>Creates a broker. Note: This API is asynchronous.</p> <p>To create a broker, you must either use the AmazonMQFullAccess IAM policy or include the following EC2 permissions in your IAM policy.</p> <ul><li><p>ec2:CreateNetworkInterface</p> <p>This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.</p></li> <li><p>ec2:CreateNetworkInterfacePermission</p> <p>This permission is required to attach the ENI to the broker instance.</p></li> <li><p>ec2:DeleteNetworkInterface</p></li> <li><p>ec2:DeleteNetworkInterfacePermission</p></li> <li><p>ec2:DetachNetworkInterface</p></li> <li><p>ec2:DescribeInternetGateways</p></li> <li><p>ec2:DescribeNetworkInterfaces</p></li> <li><p>ec2:DescribeNetworkInterfacePermissions</p></li> <li><p>ec2:DescribeRouteTables</p></li> <li><p>ec2:DescribeSecurityGroups</p></li> <li><p>ec2:DescribeSubnets</p></li> <li><p>ec2:DescribeVpcs</p></li></ul> <p>For more information, see <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user">Create an IAM User and Get Your AWS Credentials</a> and <a href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface">Never Modify or Delete the Amazon MQ Elastic Network Interface</a> in the <i>Amazon MQ Developer Guide</i>.</p> """,
    tags=['broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_broker(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1BrokersPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/brokers/{broker-id}',
    description=""" Deletes a broker. Note: This API is asynchronous. """,
    tags=['broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_broker(
    broker_id: str = Path(..., alias='broker-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/brokers/{broker-id}',
    description=""" Returns information about the specified broker. """,
    tags=['broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_broker(
    broker_id: str = Path(..., alias='broker-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/v1/brokers/{broker-id}',
    description=""" Adds a pending configuration change to a broker. """,
    tags=['broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_broker(
    broker_id: str = Path(..., alias='broker-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1BrokersBrokerIdPutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/brokers/{broker-id}/reboot',
    description=""" Reboots a broker. Note: This API is asynchronous. """,
    tags=['broker_management', 'user_account_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def reboot_broker(
    broker_id: str = Path(..., alias='broker-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/brokers/{broker-id}/users',
    description=""" Returns a list of all ActiveMQ users. """,
    tags=['broker_management', 'user_account_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_users(
    broker_id: str = Path(..., alias='broker-id'),
    max_results: Optional[conint(ge=1, le=100)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/brokers/{broker-id}/users/{username}',
    description=""" Deletes an ActiveMQ user. """,
    tags=['user_account_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_user(
    broker_id: str = Path(..., alias='broker-id'),
    username: str = ...,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/brokers/{broker-id}/users/{username}',
    description=""" Returns information about an ActiveMQ user. """,
    tags=['user_account_management', 'broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_user(
    broker_id: str = Path(..., alias='broker-id'),
    username: str = ...,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/brokers/{broker-id}/users/{username}',
    description=""" Creates an ActiveMQ user. """,
    tags=['user_account_management', 'broker_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_user(
    broker_id: str = Path(..., alias='broker-id'),
    username: str = ...,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1BrokersBrokerIdUsersUsernamePostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/v1/brokers/{broker-id}/users/{username}',
    description=""" Updates the information for an ActiveMQ user. """,
    tags=['broker_management', 'user_account_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_user(
    broker_id: str = Path(..., alias='broker-id'),
    username: str = ...,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1BrokersBrokerIdUsersUsernamePutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations',
    description=""" Returns a list of all configurations. """,
    tags=[
        'broker_management',
        'user_account_management',
        'configuration_settings_management',
        'resource_tagging_operations',
        'broker_type_description',
    ],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_configurations(
    max_results: Optional[conint(ge=1, le=100)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/configurations',
    description=""" Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version). """,
    tags=['configuration_settings_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_configuration(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1ConfigurationsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations/{configuration-id}',
    description=""" Returns information about the specified configuration. """,
    tags=['configuration_settings_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_configuration(
    configuration_id: str = Path(..., alias='configuration-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/v1/configurations/{configuration-id}',
    description=""" Updates the specified configuration. """,
    tags=['configuration_settings_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_configuration(
    configuration_id: str = Path(..., alias='configuration-id'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1ConfigurationsConfigurationIdPutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations/{configuration-id}/revisions',
    description=""" Returns a list of all revisions for the specified configuration. """,
    tags=['configuration_settings_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_configuration_revisions(
    configuration_id: str = Path(..., alias='configuration-id'),
    max_results: Optional[conint(ge=1, le=100)] = Query(None, alias='maxResults'),
    next_token: Optional[str] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/configurations/{configuration-id}/revisions/{configuration-revision}',
    description=""" Returns the specified configuration revision for the specified configuration. """,
    tags=['configuration_settings_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_configuration_revision(
    configuration_id: str = Path(..., alias='configuration-id'),
    configuration_revision: str = Path(..., alias='configuration-revision'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/tags/{resource-arn}',
    description=""" Lists tags for a resource. """,
    tags=['resource_tagging_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_tags(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/tags/{resource-arn}',
    description=""" Add a tag to a resource. """,
    tags=['resource_tagging_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_tags(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1TagsResourceArnPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/tags/{resource-arn}#tagKeys',
    description=""" Removes a tag from a resource. """,
    tags=['resource_tagging_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_tags(
    resource_arn: str = Path(..., alias='resource-arn'),
    tag_keys: TagKeys = Query(..., alias='tagKeys'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

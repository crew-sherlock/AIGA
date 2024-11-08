# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_index_crud_operations.py
DESCRIPTION:
    This sample demonstrates how to get, create, update, or delete an index.
USAGE:
    python sample_index_crud_operations.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_SEARCH_SERVICE_ENDPOINT - the endpoint of your Azure Cognitive Search
      service
    2) SERVICE PRINCIPAL - your service principal info
"""

import os
from typing import List
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
)

load_dotenv()

tenant_id = os.environ["AZURE_TENANT_ID"]
client_id = os.environ["AZURE_CLIENT_ID"]
client_secret = os.environ["AZURE_CLIENT_SECRET"]
service_name = os.environ["SEARCH_SERVICE_NAME"]

service_endpoint = f"https://{service_name}.search.windows.net"

credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id,
                                    client_secret=client_secret)


def create_index():
    # [START create_index]
    client = SearchIndexClient(service_endpoint, credential)
    name = "hotels"
    fields = [
        SimpleField(name="hotelId", type=SearchFieldDataType.String, key=True),
        SimpleField(name="baseRate", type=SearchFieldDataType.Double),
        SearchableField(name="description", type=SearchFieldDataType.String,
                        collection=True),
        ComplexField(
            name="address",
            fields=[
                SimpleField(name="streetAddress", type=SearchFieldDataType.String),
                SimpleField(name="city", type=SearchFieldDataType.String),
            ],
            collection=True,
        ),
    ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profiles: List[ScoringProfile] = []
    index = SearchIndex(name=name, fields=fields, scoring_profiles=scoring_profiles,
                        cors_options=cors_options)
    result = client.create_index(index)
    return result
    # [END create_index]


def get_index():
    # [START get_index]
    client = SearchIndexClient(service_endpoint, credential)
    name = "hotels"
    result = client.get_index(name)
    return result
    # [END get_index]


def update_index():
    # [START update_index]
    client = SearchIndexClient(service_endpoint, credential)
    name = "hotels"
    fields = [
        SimpleField(name="hotelId", type=SearchFieldDataType.String, key=True),
        SimpleField(name="baseRate", type=SearchFieldDataType.Double),
        SearchableField(name="description", type=SearchFieldDataType.String,
                        collection=True),
        SearchableField(name="hotelName", type=SearchFieldDataType.String),
        ComplexField(
            name="address",
            fields=[
                SimpleField(name="streetAddress", type=SearchFieldDataType.String),
                SimpleField(name="city", type=SearchFieldDataType.String),
                SimpleField(name="state", type=SearchFieldDataType.String),
            ],
            collection=True,
        ),
    ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profile = ScoringProfile(name="MyProfile")
    scoring_profiles = []
    scoring_profiles.append(scoring_profile)
    index = SearchIndex(name=name, fields=fields, scoring_profiles=scoring_profiles,
                        cors_options=cors_options)

    result = client.create_or_update_index(index=index)
    return result
    # [END update_index]


def search_index():
    name = "hotels"
    search_client = SearchClient(
        service_endpoint,
        name,
        credential
    )

    results = search_client.search(
        search_text="test",
        include_total_count=True,
        search_fields=["description"],
        select=["description", "hotelName"],
        top=2
    )

    retrieved_docs = []
    for result in results:
        retrieved_docs.append({
            "content": result.get("description", ""),
            "source": result.get("hotelName", ""),
        })


def delete_index():
    # [START delete_index]
    client = SearchIndexClient(service_endpoint, credential)
    name = "hotels"
    client.delete_index(name)
    # [END delete_index]


if __name__ == "__main__":
    create_index()
    get_index()
    update_index()
    search_index()
    delete_index()

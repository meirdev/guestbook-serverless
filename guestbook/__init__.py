# guestbook/__init__.py

import datetime
import json
import os
import uuid

import boto3
from pydantic import BaseModel, EmailStr, Field

dynamodb_client = boto3.resource("dynamodb")

if os.environ.get("IS_OFFLINE"):
    dynamodb_client = boto3.resource(
        "dynamodb",
        region_name="localhost",
        endpoint_url="http://localhost:8000",
    )

table = dynamodb_client.Table(os.environ["DYNAMODB_TABLE"])


class GuestBook(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    email: EmailStr
    message: str
    date: str = Field(default_factory=lambda: datetime.datetime.now().isoformat())


class GuestBookList(BaseModel):
    __root__: list[GuestBook]


def todict(obj: BaseModel):
    return json.loads(obj.json())

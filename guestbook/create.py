# guestbook/create.py

from guestbook import GuestBook, table, todict


def create(event, context):
    data = GuestBook.parse_raw(event["body"])

    table.put_item(Item=todict(data))

    response = {
        "statusCode": 201,
        "body": data.json(),
    }

    return response

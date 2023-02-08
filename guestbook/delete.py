# guestbook/delete.py

from guestbook import table


def delete(event, context):
    table.delete_item(
        Key={"id": event["pathParameters"]["id"]},
    )

    response = {
        "statusCode": 200,
    }

    return response

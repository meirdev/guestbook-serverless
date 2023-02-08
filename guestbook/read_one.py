# guestbook/read_one.py

from guestbook import GuestBook, table


def read(event, context):
    result = table.get_item(
        Key={"id": event["pathParameters"]["id"]},
    )

    response = {
        "statusCode": 200,
        "body": GuestBook.parse_obj(result["Item"]).json(),
    }

    return response

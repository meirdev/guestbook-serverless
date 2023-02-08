# guestbook/update.py

from guestbook import GuestBook, table


def update(event, context):
    data = GuestBook.parse_raw(event["body"])

    result = table.update_item(
        Key={"id": event["pathParameters"]["id"]},
        UpdateExpression="set #n = :name, #e = :email, #m = :message",
        ExpressionAttributeNames={
            "#n": "name",
            "#e": "email",
            "#m": "message",
        },
        ExpressionAttributeValues={
            ":name": data.name,
            ":email": data.email,
            ":message": data.message,
        },
        ReturnValues="ALL_NEW",
    )

    response = {
        "statusCode": 200,
        "body": GuestBook.parse_obj(result["Attributes"]).json(),
    }

    return response

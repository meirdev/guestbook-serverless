# guestbook/read_all.py

from guestbook import GuestBookList, table


def read(event, context):
    result = table.scan()

    response = {
        "statusCode": 200,
        "body": GuestBookList.parse_obj(result["Items"]).json(),
    }

    return response

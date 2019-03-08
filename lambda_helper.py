import json
import datetime
from uuid import UUID


def proxy_response(code, string_body):
    return {
        'statusCode': code,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps(string_body, default=decoder)
    }


def decoder(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    elif isinstance(o, UUID):
        return str(o)


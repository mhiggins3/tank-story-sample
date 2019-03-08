import json
import connection
import create_models
import summary_service
import lambda_helper
from pymongo import ASCENDING
from datetime import datetime
from uuid import UUID
from tank_story_models import Account, Sample
from pprint import pprint



def lambda_handler(event, context):
    connection.connection()
    if event['httpMethod'] == 'GET':
        return get_handler(event, context)
    elif event['httpMethod'] == 'POST':
        return post_handler(event, context)
    else:
        return lambda_helper.proxy_response(405, "Method not allowed " + event.httpMethod)


def get_handler(event, context):
    # "2019-02-05T16:43:40Z"
    start_date_string = event['queryStringParameters']['startDate'] + "T00:00:00Z"
    end_date_string = event['queryStringParameters']['endDate'] + "T00:00:00Z"
    start_date = datetime.strptime(start_date_string, '%Y-%m-%dT%H:%M:%SZ')
    end_date = datetime.strptime(end_date_string, '%Y-%m-%dT%H:%M:%SZ')
    # db_samples = list(Sample.objects.raw({'account_id': UUID("d2f702a1-36f8-11e9-8305-acde48001122")}))
    db_samples = Sample.objects.raw({'account_id': UUID("d2f702a1-36f8-11e9-8305-acde48001122"), 'created_date': {'$gte': start_date,
                                                           '$lte': end_date}}).order_by([('created_date', ASCENDING)])
    # account = Account.objects.get({'_id': UUID('d2f702a1-36f8-11e9-8305-acde48001122')})
    samples = []
    for sample in db_samples:
        print(sample)
        samples.append(sample.to_son().to_dict())
    return lambda_helper.proxy_response(200, samples)


def post_handler(event, context):
    # This should be coming from the user who loggs into the API gateway function
    try:
        account = Account.objects.get({'_id': UUID('d2f702a1-36f8-11e9-8305-acde48001122')})
        body = json.loads(event['body'])
        # Save our sample
        sample = Sample(
            account_id='d2f702a1-36f8-11e9-8305-acde48001122',
            created_date=body['created_date'],
            measure=body['measure'],
            out_temp=body['out_temp'],
            house_temp=body['house_temp'],
            tank_temp=body['tank_temp'],
            burner_state=body['burner_state']
        ).save()
        summary_service.update_summary(account, sample)

        # calculate summary
    except Account.DoesNotExist:
        pprint("Account does not exist creating")
        create_models.create_base_account()
        return lambda_helper.proxy_response(404, 'User does not exist')
    else:
        return lambda_helper.proxy_response(200, 'Sample saved successfully')

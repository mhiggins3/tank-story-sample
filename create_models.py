from tank_story_models import Account, Config, Summary
import connection
import json
from pymodm.errors import ValidationError

connection.connection()


def create_base_account():
    try:
        this_summary = Summary(
                last_fill_date='',
                total_fills=0,
                total_gallons_used=0,
                tank_size=250,
                current_available=0,
                avg_day=0,
                min_day=0,
                max_day=0,
                min_week=0,
                current_monthly_usage=0
        )
        this_config = Config(
            low_level=.25,
            alert_phone='617-959-6442',
            alert_email='matt.higgins@gmail.com',
            provider_state='MA',
            provider_name='Pioneer',
            provider_phone='617-959-6442',
            provider_emg_phone='617-959-6442'
        )
        account = Account(
            account_id='d2f702a1-36f8-11e9-8305-acde48001122',
            summary=this_summary,
            config=this_config
        ).save()
    except ValidationError as exc:
        print("We had an error " + json.dumps(exc.message))
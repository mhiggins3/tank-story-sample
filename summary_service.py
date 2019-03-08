import arrow
from datetime import datetime
from pymongo import ASCENDING
from tank_story_models import Sample, Account
from uuid import UUID

def update_summary(account, sample):

    # TODO: Save last sample date time
    # TODO: Save previous days usage
    # TODO: gallons used += current_vailable - sample.measure
    # TODO: Count days since last fill add avg_day ((current_vailable - sample.measure) + current_average) / days_since_last_fill
    # TODO: If sample.mesure > current_available (we filled) set last fill date to now.
    # We are in a fill state
    if account.summary.first_sample_date:
        account.summary.first_sample_date = sample.created_date
    if sample.mesure > account.summary.current_available:
        account.summary.last_fill_date = datetime
        account.summary.samples_since_last_fill = 1
        account.summary.avg_day = sample.measure
        account.summary.min_day = sample.measure
        account.summary.max_day = sample.measure
        account.summary.min_week = sample.measure
    else:
        # TODO: Accumulate samples for the current day
        # TODO: Accumulate samples fro the current month
        days_since_last_fill = arrow.Arrow.span_range("day", account.summary.last_fill_date, sample.created_date)
        months_since_last_fill = arrow.Arrow.span_range("month", account.summary.last_fill_date, sample.created_date)
        samples_since_last_fill = Sample.objects.raw(
            {'account_id': UUID("d2f702a1-36f8-11e9-8305-acde48001122"), 'created_date':
                {'$gte': account.summary.last_fill_date}}).order_by([('created_date', ASCENDING)])

        used_since_last_sample = account.summary.current_available - sample.measure

        account.summary.gallons_used = account.summary.gallons_used + used_since_last_sample

    account.summary.current_available = sample.measure
    account.save()

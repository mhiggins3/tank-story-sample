from pymongo import DESCENDING, HASHED
from pymongo.operations import IndexModel
from pymodm import fields, MongoModel, EmbeddedMongoModel


class Summary(EmbeddedMongoModel):
    last_fill_date = fields.DateTimeField()
    total_fills = fields.IntegerField()
    total_gallons_used = fields.IntegerField()
    tank_size = fields.IntegerField()
    current_available = fields.FloatField()
    avg_day = fields.FloatField()
    min_day = fields.FloatField()
    max_day = fields.FloatField()
    min_week = fields.FloatField()
    current_monthly_usage = fields.FloatField()


class Config(EmbeddedMongoModel):
    # This will be a percentage of tank volume 1/4 (.25)
    low_level = fields.FloatField()
    alert_phone = fields.CharField()
    alert_email = fields.EmailField()
    provider_state = fields.CharField()
    provider_name = fields.CharField()
    provider_phone = fields.CharField()
    provider_emg_phone = fields.CharField()


class Sample(MongoModel):
    account_id = fields.UUIDField()
    created_date = fields.DateTimeField()
    measure = fields.FloatField()
    out_temp = fields.FloatField()
    house_temp = fields.FloatField()
    tank_temp = fields.FloatField()
    burner_state = fields.BooleanField()

    class Meta:
        indexes = [
            IndexModel([('created_date', DESCENDING)]),
            IndexModel([('account_id', HASHED)])
        ]


class Account(MongoModel):
    account_id = fields.UUIDField(primary_key=True)
    summary = fields.EmbeddedDocumentField('Summary')
    config = fields.EmbeddedDocumentField('Config')



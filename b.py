import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd

dynamodb = boto3.resource(
    'dynamodb',
)


def push(item_id, keyword, page, idx):
  table = dynamodb.Table('cooviewhistory')

  table.put_item(
    Item={
          'logts': int(pd.Timestamp.now().timestamp()),
          'item_id': int(item_id),
          'page': int(page),
          'keyword': str(keyword),
      }
  )



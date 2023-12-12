import boto3
from botocore.exceptions import ClientError
import json

def create_sns_client():
    session = boto3.session.Session()
    sns_client = session.client('sns')
    return sns_client

def publish_to_sns(sns_client, topic_arn, message):
    try:
        response = sns_client.publish(TopicArn=topic_arn, Message=message)
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise

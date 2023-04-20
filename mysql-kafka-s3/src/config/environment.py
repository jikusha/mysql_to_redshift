import os
from dotenv import load_dotenv
from collections import namedtuple

class EnvironmentVariables:
    def __init__(self):
        load_dotenv()
        kafka_topic_list = []
        # kafka topic names
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_FACT_SALE'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_EMP'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_CUST'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_PROD'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_DATE'))
        kafka_topic_list.append(os.getenv('KAFKA_TOPIC_DIM_LOC'))
        self.kafka_topics = namedtuple("Kafka_topics", kafka_topic_list)(*kafka_topic_list)

        #kafka access keys and server
        kafka_api_key = os.getenv('KAFKA_CLOUD_API_KEY')
        kafka_api_secret = os.getenv('KAFKA_CLOUD_API_SECRET')
        kafka_server = os.getenv('KAFKA_BOOTSTRAP_SERVER')
        self.kafka_config = namedtuple("kafka_server", ["kafka_server", "kafka_api_key", "kafka_api_secret"])(
            kafka_server = kafka_server, kafka_api_key = kafka_api_key, kafka_api_secret = kafka_api_secret
        )

        # mysql
        mysql_server = os.getenv('MYSQL_URI')
        mysql_password = os.getenv('MYSQL_PASSWORD')
        mysql_user = os.getenv('MYSQL_USER_NAME')
        self.mysql = namedtuple("mysql", ["mysql_server", "mysql_user", "mysql_password"])(
            mysql_user=mysql_user, mysql_password=mysql_password, mysql_server=mysql_server
        )

        # aws
        aws_s3_name = os.getenv("bucket_name")
        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws = namedtuple("aws", ["aws_s3_name", "aws_access_key", "aws_secret_key"])(
            aws_secret_key=aws_secret_key, aws_access_key=aws_access_key, aws_s3_name=aws_s3_name
        )
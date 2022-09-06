import datetime
import json
import random
import boto3
import time

STREAM_NAME = "test-input" ## Update this value if default CloudFormation name was not used 

message1 = "Aug 31 05:00:01 ip-172-31-9-195 systemd: Created slice User Slice of root."
message2 = "Aug 31 05:50:01 ip-172-31-9-195 systemd: Started Session 1379 of user root."
message3 = "Aug 31 05:57:37 ip-172-31-9-195 dhclient[2858]: XMT: Solicit on eth0, interval 129880ms."
message4 = "Aug 31 05:59:46 ip-172-31-9-195 ec2net: [get_meta] Querying IMDS for meta-data/network/interfaces/macs/0a:d0:5b:65:b8:14/local-ipv4s"
message5 = "Aug 31 05:50:01 ip-172-31-9-195 systemd: Started Session 1379 of user root."

def get_data():
    return {
        'timestamp': datetime.datetime.now().isoformat(),
        'message': random.choice([message1, message2, message3, message4, message5]),
        'port_number': random.randrange(1, 10)
    }

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        partition_key = str(data["port_number"])
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key)
        time.sleep(0.5)


if __name__ == '__main__':
    kinesis_client = boto3.client('kinesis')
    generate(STREAM_NAME, kinesis_client)


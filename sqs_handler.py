import boto3

# Initialize SQS client
sqs = boto3.client('sqs',region_name='us-west-2')

# Replace with your FIFO queue URL
# queue_url = 'https://sqs.us-west-2.amazonaws.com/343218199303/UsualQueue1'
queue_url = 'https://sqs.us-west-2.amazonaws.com/343218199303/TestQueue1.fifo'
# Create batch messages
messages = [
    {
        'Id': 'msg4',  # Unique ID for each message in the batch
        'MessageBody': 'First message body',
        'MessageGroupId': 'group1',
        'MessageDeduplicationId': 'msg1_dedup'
    },
    {
        'Id': 'msg5',
        'MessageBody': 'Second message body',
        'MessageGroupId': 'group1',
        'MessageDeduplicationId': 'msg2_dedup'
    },
    {
        'Id': 'msg6',
        'MessageBody': 'Third message body',
        'MessageGroupId': 'group2',
        'MessageDeduplicationId': 'msg3_dedup'
    }
]

# Send batch messages
response = sqs.send_message_batch(QueueUrl=queue_url, Entries=messages)

# Print the response
print("Batch response:", response)

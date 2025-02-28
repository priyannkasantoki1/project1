import json
import boto3

# Initialize DynamoDB with the correct region
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    try:
        # Parse the JSON string from the request body
        body = json.loads(event.get('body', '{}'))
        student_id = body.get('studentid')
        name = body.get('name')
        student_class = body.get('class')
        age = body.get('age')

        # Basic validation (optional)
        if not all([student_id, name, student_class, age]):
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps("Missing one or more required parameters")
            }

        # Insert the student record into DynamoDB
        table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps("Student data saved successfully!")
        }
    except Exception as e:
        # Log the error (you can also add print statements here for debugging)
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }


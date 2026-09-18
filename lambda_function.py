import boto3
import base64
import uuid
import json

s3 = boto3.client("s3")

BUCKET_NAME = "yaman-image-upload-2026"


def lambda_handler(event, context):
    print("Lambda code updated from GitHub!")

    try:
        body = event.get("body", "")

        if event.get("isBase64Encoded"):
            image_data = base64.b64decode(body)
        else:
            image_data = base64.b64decode(body)

        filename = f"uploads/{uuid.uuid4()}.jpg"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=image_data,
            ContentType="image/jpeg"
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Image uploaded successfully",
                "filename": filename
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }

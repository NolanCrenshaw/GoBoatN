# Package Requirements
import os
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import ClientError

# Local Requirements
from ..config import Config


bucket = Blueprint('bucket', __name__)

s3 = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY,
)
s3_bucket_name = 'goboatnbucky'


# Routes
@bucket.route('/upload', methods=["POST"])
@jwt_required()
def upload():
    if request.method == "POST":
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            s3.upload_fileobj(
                Fileobj=img,
                Bucket=s3_bucket_name,
                Key=filename
            )
            return jsonify(
                sprite=filename,
                message="file uploaded successfully"), 201
        else:
            return jsonify(message="file failed to upload"), 407

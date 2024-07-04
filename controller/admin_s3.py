import boto3
from credentials.keys_s3 import ACCESS_KEY, ACCESS_KEY

def get_connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, ACCESS_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connection S3")
    except Exception as err:
        print(err)
        
def save_file(photo):
    photo_path = "/tmp/photo1.png"
    
    try: 
        photo.save(photo_path)
        print("photo saved")
    except Exception as e:
        print(f"Error saving photo: {e}")
import boto3
from credentials.keys_s3 import ACCESS_KEY, SECRET_KEY

bucket_name = "vetbucket1"

def get_connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connection S3")
        return s3_resource
    except Exception as err:
        print(err)
        
def save_file(photo):
    try: 
        photo_path = "/tmp/photo1"
        photo.save(photo_path)
        print("photo saved")
        return photo_path
    except Exception as e:
        print(f"Error saving photo: {e}")
        
def upload_file(s3_resource, photo, photo_path_local, id):
    isPhotoSaved = True
    try:
        photo_name = photo.filename
        photo_extension = photo_name.split(".")[-1]
        s3_file_name = f"images/{id}.{photo_extension}"
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, s3_file_name)
        print("File uploaded")
    except Exception as e:
        isPhotoSaved = False
        print(f"Error saving photo in S3: {e}")
    finally:
        return isPhotoSaved
        
def consult_file(s3_resource, id):
    bucket_repo = s3_resource.Bucket(bucket_name)
    bucket_objects = bucket_repo.objects.all()
    for obj in bucket_objects:
        name_photo_s3 = obj.key.split("/")[-1]
        if id == name_photo_s3.split(".")[0]:
            print("photo founded " + id)
            return f"https://vetbucket1.s3.amazonaws.com/images/{name_photo_s3}"
    return None
    
    
    
    
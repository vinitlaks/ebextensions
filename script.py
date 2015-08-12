import os
import zipfile
import botocore.session

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


zipf = zipfile.ZipFile('ebextensions.zip', 'w')
zipdir('./ebextensions', zipf)
zipf.close()
file_path = './ebextensions.zip'
fp = open(file_path, 'rb')
session = botocore.session.get_session()
session.set_credentials(os.environ['access_key_id'], os.environ['secret_access_key'])
client = session.create_client('s3', region_name='us-west-2')
client.put_object(ACL='public_read', Bucket=os.environ['bucket_name'], Body=fp,Key='ebextensions.zip')

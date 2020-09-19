from google.cloud import storage
import os
import pickle
import glob
from typing import Dict


os.environ["GOOGLE_CLOUD_PROJECT"] = 'climatekaraoke'


def storage_client() -> storage.Client:
    return storage.Client(credentials='creds.json')


def list_buckets():
    """Lists all buckets."""

    buckets = storage_client().list_buckets()

    for bucket in buckets:
        print(bucket.name)


def list_objects(bucket_name):
    """Lists all the blobs in the bucket."""

    blobs = storage_client().list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


def dump_dict_to_pickle(dict_filename: str, dictionary: Dict[str, str]) -> str:
    dictionary_path: str = f'{dict_filename}.pickle'
    with open(dictionary_path, 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Saved the dictionary to pickle {dictionary_path}')
    return dictionary_path


def download_object(bucket_name,
                    source_blob_name,
                    destination_file_name) -> str:
    """Downloads a blob from the bucket."""

    bucket = storage_client().bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Object {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )

    return destination_file_name


def upload_object(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    bucket = storage_client().bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def unpickle_dictionary(dictionary_path: str) -> Dict[str, str]:
    with open(dictionary_path, 'rb') as handle:
        unpickled_dict: Dict[str, str] = pickle.load(handle)
        print(f'Unpickled dict from path {dictionary_path}')
        return unpickled_dict


def download_dictionary(gcs_dict_name: str,
                        bucket_name: str = 'python_directories') -> Dict[str, str]:
    return unpickle_dictionary(download_object(bucket_name,
                                               gcs_dict_name,
                                               f''))


def create_folder(bucket_name, destination_folder_name):
    bucket = storage_client().get_bucket(bucket_name)
    blob = bucket.blob(destination_folder_name)

    blob.upload_from_string('')

    print('Created {}'.format(
        destination_folder_name))


def upload_folder(directory_path: str, bucket_name: str):
    dir_name: str = [d for d in directory_path.split('/') if d][-1]
    create_folder(bucket_name, dir_name)
    bucket = storage_client().bucket(bucket_name)
    for fil_path in glob.glob(f'{directory_path}/*'):
        fil_name: str = fil_path.split('[./]')[-1]
        blob = bucket.blob(f'{dir_name}{fil_name}')
        blob.upload_from_filename(fil_path)
        print(f'Uploaded {fil_path}')


def download_folder(directory_name: str, bucket_name: str):
    bucket = storage_client().bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=directory_name)
    for blob in blobs:
        if (not blob.name.endswith("/")):
            try:
                os.makedirs("/".join(blob.name.split('/')[:-1]))
            except FileExistsError:
                pass
            blob.download_to_filename(blob.name)
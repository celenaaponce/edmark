from google.cloud import storage

def download_tflite_model(bucket_name, source_blob_name, destination_file_name):
    """Downloads a TFLite model from Google Cloud Storage."""
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

# Replace with your actual values
bucket_name = 'edmark_sign_detection'
source_blob_name = 'keypoint_classifier.tflite'
destination_file_name = 'model/keypoint_classifier/keypoint_classifier.tflite'

download_tflite_model(bucket_name, source_blob_name, destination_file_name)
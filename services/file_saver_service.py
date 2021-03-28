class FileSavingService:

    def __init__(self):
        self.storage = BlobStorage()

    def save(self, file_to_load):
        url = self.storage.save(file_to_load)
        return url


class BlobStorage:

    CONN_STRING = "DefaultEndpointsProtocol=https;AccountName=speechrecognitionstorage;AccountKey=7fVulw2eHV1K77IDN4ddKB31+d9RrIGCTbw15akLn8LLJ8IVJAUnB/FU3E3yFrzcv2doaLxdvOooEOodHEPQBQ==;EndpointSuffix=core.windows.net"
    CONT_NAME = 'files'

    def __init__(self):
        from azure.storage.blob import BlobServiceClient
        # self.blob = BlobClient.from_connection_string(conn_str=self.CONN_STRING,
        #                                               container_name=self.CONT_NAME,
        #                                               blob_name=self.blob_name)
        self.blob_service = BlobServiceClient.from_connection_string(conn_str=self.CONN_STRING)

    def save(self, file):
        blob = self.blob_service.get_blob_client(container=self.CONT_NAME, blob=file.name)
        blob.upload_blob(file, overwrite=True, content_type=file.content_type)
        return blob.url

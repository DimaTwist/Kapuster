

class FileSavingService:

    def __init__(self, file_to_load, storage):
        self.storage = storage
        self.file = file_to_load

    def save(self):
        self.storage.save(self.file)
        return 'done'


class BlobStorage:

    def __init__(self):
        self.CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=speechrecognitionstorage;AccountKey=7fVulw2eHV1K77IDN4ddKB31+d9RrIGCTbw15akLn8LLJ8IVJAUnB/FU3E3yFrzcv2doaLxdvOooEOodHEPQBQ==;EndpointSuffix=core.windows.net"
        self.CONTAINER_NAME = "files"
        self.BLOB_NAME = "blobname"

    def save(self, file_to_load):
        from azure.storage.blob import BlobClient
        blob = BlobClient.from_connection_string(self.CONNECTION_STRING,
                                                 container_name=self.CONTAINER_NAME,
                                                 blob_name=self.BLOB_NAME)

        with open(file_to_load, 'rb') as data:
            blob.upload_blob(data, blob_type="BlockBlob")

        return "Loaded"

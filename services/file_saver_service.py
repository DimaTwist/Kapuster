class FileSavingService:

    def __init__(self):
        self.storage = BlobStorage()

    def save(self, file_to_load):
        blob = self.storage.save(file_to_load)
        print(blob)
        return blob


class BlobStorage:

    CONN_STRING = "DefaultEndpointsProtocol=https;AccountName=speechrecognitionstorage;AccountKey=7fVulw2eHV1K77IDN4ddKB31+d9RrIGCTbw15akLn8LLJ8IVJAUnB/FU3E3yFrzcv2doaLxdvOooEOodHEPQBQ==;EndpointSuffix=core.windows.net"
    CONT_NAME = 'files'
    BLOB_NAME = 'testfile.wav'

    def __init__(self):
        from azure.storage.blob import BlobClient
        self.blob = BlobClient.from_connection_string(conn_str=self.CONN_STRING,
                                                      container_name=self.CONT_NAME,
                                                      blob_name=self.BLOB_NAME)

    def save(self, file):
        # with open(file, 'rb') as data:
        self.blob.upload_blob(file, overwrite=True, content_type='audio/wav')


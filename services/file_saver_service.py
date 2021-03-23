

class FileSavingService:

    def __init__(self, file_to_load, storage):
        self.storage = storage
        self.file = file_to_load

    def save(self):
        url = self.storage.save(self.file)
        return url


class BlobStorage:

    CONN_STRING = "DefaultEndpointsProtocol=https;AccountName=speechrecognitionstorage;AccountKey=7fVulw2eHV1K77IDN4ddKB31+d9RrIGCTbw15akLn8LLJ8IVJAUnB/FU3E3yFrzcv2doaLxdvOooEOodHEPQBQ==;EndpointSuffix=core.windows.net"
    CONT_NAME = 'files'
    BLOB_NAME = 'testfile.wav'

    def __init__(self):
        from azure.storage.blob import BlobClient, ContentSettings
        self.content_settings = ContentSettings(content_type='audio/wav')
        self.blob = BlobClient.from_connection_string(conn_str=self.CONN_STRING,
                                                 container_name=self.CONT_NAME,
                                                 blob_name=self.BLOB_NAME)

    def save(self, file):
        with open(file, 'rb') as data:
            self.blob.upload_blob(data, content_type=self.content_settings)


# upload = BlobStorage()
# upload.save(r"C:\Users\Dzmitry_Shman\PycharmProjects\Kapuster\media\OSR_us_000_0010_8k_iCVjkpS.wav")

property

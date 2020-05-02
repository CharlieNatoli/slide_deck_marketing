

class HorribleGoogleDriveHandler(object):

    def __init__(self, api_service):
        self.api_service = api_service

    def share_file(self, slide_deck_id, email):

        return self.api_service.drive_service.permissions().create(
            fileId=slide_deck_id,
            body={'role': 'writer', 'type': 'user', 'emailAddress': email}
        ).execute()




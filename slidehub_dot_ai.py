
from authenticate import HorribleGoogleAPIService
from slide_file_utilities import HorribleSlideDeckEditor
from file_sharing import HorribleGoogleDriveHandler

# main function. This can be where we create the command line interface

if __name__ == '__main__':
    api_service = HorribleGoogleAPIService()

    slide_deck_editor = HorribleSlideDeckEditor(api_service)
    google_drive_handler = HorribleGoogleDriveHandler(api_service)

    deck_info = slide_deck_editor.create_slide_deck()

    google_drive_handler.share_file(deck_info['presentationId'], 'slidehub_dot_ai@gmail.com')

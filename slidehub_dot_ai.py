
import numpy as np

from authenticate import HorribleGoogleAPIService
from slide_file_utilities import HorribleSlideDeckEditor
from file_sharing import HorribleGoogleDriveHandler

# main function. This can be where we create the command line interface


def get_emails():
    email_list = input('Please enter a list of contacts that you wish to delight: ')
    email_list = email_list.split(',')
    return [x.strip() for x in email_list]

def get_user_input():
    email_list = get_emails()
    message_text = input('Now, please enter what it is that your contacts must know: ')
    return email_list, message_text


if __name__ == '__main__':

    email_list, message_text = get_user_input()

    api_service = HorribleGoogleAPIService()

    slide_deck_editor = HorribleSlideDeckEditor(api_service)
    google_drive_handler = HorribleGoogleDriveHandler(api_service)

    deck_info = slide_deck_editor.create_slide_deck()

    for i in range(np.random.randint(1, 10)):
        slide_deck_editor.create_text_box(deck_info, message_text)

    for email in email_list:
        google_drive_handler.share_file(deck_info['presentationId'], email)

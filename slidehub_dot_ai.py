
from authenticate import HorribleGoogleAPIService
from slide_file_utilities import HorribleSlideDeckEditor

# main function. This can be where we create the command line interface

if __name__ == '__main__':
    api_service = HorribleGoogleAPIService()

    slide_deck_editor = HorribleSlideDeckEditor(api_service)

    deck_info = slide_deck_editor.create_slide_deck()

    print(f'created slide deck with id {deck_info["presentationId"]}')

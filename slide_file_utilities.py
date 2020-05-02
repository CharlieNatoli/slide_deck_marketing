
import uuid
# add add all api calls to add stuff to the slide deck here
from generate_shapes import add_text_box
from parse_strings import add_text, random_parse_string

DEFAULT_TITLE = 'A [special] message [just] for you'


class HorribleSlideDeckEditor(object):

    def __init__(self, api_service):
        self.api_service = api_service

    def create_slide_deck(self):
        body = {'title': DEFAULT_TITLE}
        return self.api_service.slides_service.presentations().create(body=body).execute()

    def create_text_box(self, deck_info, message_text):
        object_id = str(uuid.uuid4())
        text_box_call = add_text_box(objectId=object_id, pageId=deck_info['slides'][0]['objectId'])

        add_text_call = add_text(objectId=object_id, text=random_parse_string(message_text))

        self.api_service.slides_service.presentations().batchUpdate(
            presentationId=deck_info['presentationId'],
            body={'requests': [text_box_call, add_text_call]}
        ).execute()

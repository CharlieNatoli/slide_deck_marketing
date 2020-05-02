from generate_shapes import random_add_shape

import uuid
# add add all api calls to add stuff to the slide deck here
from generate_shapes import add_text_box, update_object_color
from parse_strings import add_text, random_parse_string


class HorribleSlideDeckEditor(object):

    def __init__(self, api_service):
        self.api_service = api_service

    def create_slide_deck(self):
        return self.api_service.slides_service.presentations().create(body={}).execute()

    def add_random_shape(self, deck_info, **kwargs):
        object_id = str(uuid.uuid4())
        shape = random_add_shape(objectId=object_id, pageId=deck_info['slides'][0]['objectId'], **kwargs)
        add_color = update_object_color(object_id)
        return [shape, add_color]

    def create_text_box(self, deck_info, message_text):
        object_id = str(uuid.uuid4())
        text_box_call = add_text_box(objectId=object_id, pageId=deck_info['slides'][0]['objectId'])

        add_text_call = add_text(objectId=object_id, text=random_parse_string(message_text))
        return [text_box_call, add_text_call]

    def update_all(self, deck_info, requests):
        self.api_service.slides_service.presentations().batchUpdate(
            presentationId=deck_info['presentationId'],
            body={'requests': requests}
        ).execute()

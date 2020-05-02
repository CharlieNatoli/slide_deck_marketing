from generate_shapes import random_add_shape
# add add all api calls to add stuff to the slide deck here


class HorribleSlideDeckEditor(object):

    def __init__(self, api_service):
        self.api_service = api_service

    def create_slide_deck(self):
        return self.api_service.slides_service.presentations().create(body={}).execute()

    def add_random_shape(self, presentationId, pageId, **kwargs):
        shape = random_add_shape(presentationId=presentationId, pageId=pageId, **kwargs)
        return self.api_service.slides_service.presentations().batchUpdate(presentationId=presentationId, body={'requests': [shape]})

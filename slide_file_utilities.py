
# add add all api calls to add stuff to the slide deck here


class HorribleSlideDeckEditor(object):

    def __init__(self, api_service):
        self.api_service = api_service

    def create_slide_deck(self):
        return self.api_service.slides_service.presentations().create(body={}).execute()

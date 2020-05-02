
from authenticate import HorribleGoogleAPIService
from file_sharing import HorribleGoogleDriveHandler
from slidehub_dot_ai import DATABASE_FILE_PATH

DEFAULT_RESPONSE = '<spam style="color:black">{}: Lorem ipsum dolor sit amet, consectetur adipiscing elit.</spam>'


def file_ids():
    with open(DATABASE_FILE_PATH, 'r') as fh:
        file_ids = fh.read( )
    file_ids = file_ids.split(',')
    return [x.strip() for x in file_ids]


def get_comments_for_file(file_id, drive_handler):
    comments = drive_handler.api_service.drive_service.comments().list(fileId=file_id, fields='*').execute()
    return comments


def reply_to_comments(comments,file_id, drive_handler, response):
    for comment in comments['comments']:
        try:
            drive_handler.api_service.drive_service.replies().create(
                commentId=comment['id'], fileId=file_id, fields='*',
                body={'content': response.format(comment['author']['displayName'])
                      }
            ).execute()
        except:
            pass


if __name__ == '__main__':

    api_service = HorribleGoogleAPIService()
    drive_handler = HorribleGoogleDriveHandler(api_service)

    for file_id in file_ids():

        comments = get_comments_for_file(file_id, drive_handler)
        reply_to_comments(comments, file_id, drive_handler, response=DEFAULT_RESPONSE)

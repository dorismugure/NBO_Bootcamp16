import pprint

import sys

from apiclient.discovery import build

api_key = sys.argv[1]

service = build('books', 'v1', developerKey=api_key)

request = service.volumes().list(source='public', q='William Stalling')

response = request.execute()

pprint.pprint(response)

print ('Found %d books:' % len(response['list']))

for book in response.get('list', []):

  print ('Title: %s, ' % (

    book['volumeInfo']['title'],

    book['volumeInfo']))

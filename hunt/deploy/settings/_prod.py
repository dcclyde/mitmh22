from ._base import *

DEBUG = False
ROOT_LOG_LEVEL = 'INFO'

SPOILR_ENABLE_DJANGO_ADMIN = True
SPOILR_ENABLE_DJANGO_ADMIN_DOCS = False

HUNT_LOAD_SAMPLE_ROUND = False
HUNT_PUZZLEVIEWER_ENABLED = False

HUNT_PUBLIC_TEAM_NAME = 'public'

HUNT_ASSETS_SERVE_STATICALLY = True
# STATIC_URL = 'https://storage.googleapis.com/mitmh2022/static/'
STATIC_URL = 'https://storage.googleapis.com/mitmh22/static/'

HUNT_WEBSITE_ACCESS_TOKEN = None

DEFAULT_FROM_EMAIL = 'hunt@mitmh2022.com'
SERVER_EMAIL = 'hunt-server@mitmh2022.com'
HUNT_SUBMISSIONS_EMAIL = 'submissions@mitmh2022.com'
HUNT_BOOKREPORT_EMAIL = None # TODO: enable once tested: 'bookreports@mitmh2022.com' # This isn't used
SPOILR_HQ_DEFAULT_FROM_EMAIL = 'hq@mitmh2022.com'
SPOILR_HINTS_FROM_EMAIL = 'hints@mitmh2022.com'
STORY_FROM_EMAIL = 'story@mitmh2022.com'
BOOK_REPORTS_EMAIL = 'bookreports@mitmh2022.com'
EMOJI_ART_EMAIL = 'emojiart@mitmh2022.com'

HUNT_SOLVES_BEFORE_HINTS_RELEASED = 30
HUNT_RD3_SOLVES_BEFORE_HINTS_RELEASED = 10

HUNT_ENABLE_CACHING = True
HUNT_ENABLE_FILE_CACHING = True
PUZZLE_TECH_SUPPORT_EMAIL = 'no-reply+tech-support@mitmh2022.com'

HUNT_REGISTRATION_CLOSED = False
HUNT_LOGIN_ALLOWED = True

IMPORTS_ADDED = 'imp_add'
IMPORTS_IN_FILE = 'imp_all'

TOTAL = 'total'
TIME_SERIES = 'yyyymm'
FILES = 'files'
LANGS = 'langs'
ADDED = 'add'
DELETED = 'del'
TOUCH_COUNT = 'tch'
START_TIME = 'st'
END_TIME = 'et'
COMMITS = 'commits'
LIBS = 'libs'
LIBRARIES = 'libraries'
PUBLIC_LIBRARIES = 'public_libraries'
STATS = 'stats'
USER = 'user'
IMPORTS = 'imports'
TEAM_MATES = 'team'
SIG_CONTRIB_FILE_LIST = 'sig_contrib_file_list'
UNKOWN = 'unknown'
SIGNIFICANT_CONTRIBUTION = 'sig_cont'
SIGNIFICANT_CONTRIBUTION_WITH_STATS = 'sig_cont_stats'
ORIGINAL_AUTHOR = 'orig'
CODE = 'code'
ONE_MONTH_CHANGE = '1m'
ONE_MONTH_DELTA = '1md'
TOO_BIG_TO_ANALYZE = '2big'
INITIAL_COMMIT = 'init'
REPO = 'repo'
REPO_PATH = 'repo_path'
FILE = 'file'
DIFF = 'diff'
SIG_CODE_SNIPPETS = 'sig_code_snippets'
COMMIT_HASH = 'commit_hash'
TEAM = 'team'
LANGUAGE = 'language'
LABEL = 'label'
LIFE_OF_PY = 'life_of_py'
LIFE_OF_PY_BUCKETS = [f"{LIFE_OF_PY}_{i}" for i in range(0, 100, 10)]

MAX_SCORE = 'max_score'
MIN_SCORE = 'min_score'
SUM_SCORE = 'sum_score'
COUNT_SCORE = 'count_score'

SKILLS = 'skills'
SCORES = 'scores'
MIN_LINES_ADDED = 10
SIGNIFICANT_CONTRIBUTION_CHAR_LIMIT = 1500
MIN_CHUNK_CHAR_LIMIT = 100
# TODO: Change this dynamically based on the language
SIGNIFICANT_CONTRIBUTION_LINE_LIMIT = 20
TOO_BIG_TO_ANALYZE_LIMIT = 10000
REFORMAT_CHAR_LIMIT = 50
MAX_USERS = 1001
MAX_DIFF_SIZE = 5000
GIT_DIFF_BATCH_SIZE = 100
T5_CHUNK_CHAR_LIMIT = 1500

SKILL_PREDICTION_LIMIT = 10
LIFE_OF_PY_PREDICTION_LIMIT = 3

I2S = 'i2s'
C2S = 'c2s'
MLC = 'mlc'
MODEL_TYPES = [I2S, C2S, MLC, LIFE_OF_PY]
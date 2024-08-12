from utils import post
from constants import COZE_API, BOT_ID

user_id = 'peterwu4084'
query = "word: ambulance.n.01, definition: a vehicle that takes people to and from hospitals"
import pdb; pdb.set_trace()

post(query, COZE_API, BOT_ID, user_id)
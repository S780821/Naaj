from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AQBNiSPW4KrGqhBREG0mfR9gkwyiAUR98nuiZRsQPKTXpp3BU8DATptzUdiTFihq2RBodyQ0OQz_LDLNvNTYdRhMCxpTJMVR512JY5jflNATEOVTV-5Vv5eDURtzDn3Di8CBkewjIry6748bvU72RTx-rB5Zhc0lywPitJSUaRFw1aLVHT0h3t35P1Vsu0--bLCnipO0hm3u72UkBdC01OaEOh9e8JHu5wBSjPaNMZ3sOQ2_RQGf3UG4gF8tj9ICnrB4spNE7BdrPfraOcJpJlOpMhy3D4UpY488XZl8SV3UEJqux02ls1IAZ0Ssx-_fw5lBoIeqqPA0Xkpm5nMxhdv9dYEVUQA")
BOT_TOKEN = getenv("BOT_TOKEN", "2057609602:AAFCFboy6H6-LjlXpMWCkU7Fuq-yms9hoJI")
BOT_NAME = getenv("BOT_NAME", "ᏔᎪᎡΝᎬᎡ ᎷႮՏᏆᏟ Ꮩ2")
BOT_USERNAME = getenv("BOT_USERNAME", "WarnerMusic2_bot")
API_ID = int(getenv("API_ID", "4856470"))
API_HASH = getenv("API_HASH", "6dfa58833706557fb52017882bdb1abb")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "40"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2048314609").split()))

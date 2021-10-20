from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AQABxv9zwK3T0XoMfegbHMfVQxJOM0L7H-iKTjSF6Dyyu3OVbVsFHh6q70o-Jkdo1im9cImpScHz9vbCcyUab0SRow7mPds8415eaOhmOQnonljgeFpgGFP4Kh7NUPT9w12zzblocsuDEINySQhfzH6TfXU6qM-9BHWHPjj64yeY20rU7e8QVe61ShJZvb2Yu4zaDG-l9vCclbkBaJvseuTusRRlbGtO5Hp3GDrDvG0zypYVlg09ZlVWs_N-N3ivY0iR_YlGhQh2M8ZE3DIfyz8F4sd0M79bIJCfxzEFxTOH78IO3g5ZmfDNj-fqfhge-N1lYMxm5NuLJdamxYr19ljWeG5_-gA")
BOT_TOKEN = getenv("BOT_TOKEN", "2082128018:AAGn-N-B4_wZWSwUmYiIIcsCsLq3zCWM-i0")
BOT_NAME = getenv("BOT_NAME", "ᏔᎪᎡΝᎬᎡ ᎷႮՏᏆᏟ ")
BOT_USERNAME = getenv("BOT_USERNAME", "WarnerMusic_bot")
API_ID = int(getenv("API_ID", "4856470"))
API_HASH = getenv("API_HASH", "6dfa58833706557fb52017882bdb1abb")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2048314609").split()))

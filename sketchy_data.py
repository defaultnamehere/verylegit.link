
# Yeah yeah yeah you're here to look at the gags go on then do it.
MAX_NUM_SKETCHY_WORDS = 4
MAX_NUM_FILETYPES = 2
MAX_NUM_LETTER_REPLACEMENTS = 1

# Chance to include a big ol random string at the beginning, eg OOF8NS3AJXMFJ371J7G2
LONG_RANDOM_STIRNG_CHANCE = 0.3

#DOMAINS = ("heapslegit.link", "freemalware.club", "spywareexchange.party")
DOMAINS = ("https://sketchify-42ef3.appspot.com",)
SAMPLE_LONG_URLS = ("http://google.com", "http://facebook.com", "http://i.imgur.com/OpYDgt3.gif")

SCARY_WORDS = (
    "mov",
    "free",
    "download",
    "torrent",
    "pcspeedup",
    "malware",
    "virus",
    "resume",
    "index",
    "botnet",
    "trojan",
    "ip-stealer",
    "webcam",
    "spambot",
    "spam",
    "spyware",
    "installer",
    "downloader",
    "movie",
    "pccleaner",
    "invoice",
    "notice",
    "bank",
    "moneygram",
    "paypal",
    "cryptolocker",
    "bitcoin",
    "hack",
    "pcmonitor",
    "speedupurpc",
    "java0day",
    "javaexploit",
    "flashexploit"
    "x86",
    "x64",
    "32",
    "64"
    )

FILETYPES = (
    "mp4",
    "exe",
    "pdf",
    "msi",
    "dmg",
    "apk",
    "jar",
    "swf",
    "malware",
    "virus",
    "zip",
    "rar",
)

# Filetypes that the url could end with.
ENDING_FILETYPES = (
    "exe",
    "rar",
    "zip",
)
# Strings to put between the sketchy words.
DELIMITERS = (
    "",
    "-",
    "__",
    "_",
    "+",
    "=",
    "$",
    "(",
    ")",
    "!"
)

# Characters to replace randomly deleted letters.
# In some ways these are all weird strings.
WEIRD_STRINGS = (
    "0x8"
    "*",
    ";",
    "-"
)


# Yeah yeah yeah you're here to look at the gags go on then do it.
MAX_NUM_SKETCHY_WORDS = 4
MAX_NUM_FILETYPES = 2
MAX_NUM_LETTER_REPLACEMENTS = 1

DOMAINS = ("heapslegit.link", "freemalware.club", "spywareexchange.party")

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

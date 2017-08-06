
# Yeah yeah yeah you're here to look at the gags go on then do it.
MAX_NUM_SKETCHY_WORDS = 4
MAX_NUM_FILETYPES = 2
MAX_NUM_LETTER_REPLACEMENTS = 1

# Chance to include a big ol random string at the beginning, eg
# OOF8NS3AJXMFJ371J7G2
LONG_RANDOM_STIRNG_CHANCE = 0.3

# This is good for a million URLs, but not ten million.
MAX_ANTI_COLLISION_NUMBER = 1000

DOMAINS = ("verylegitlink.appspot.com",
           "verylegit.link",
           "secure.verylegit.link",
           "webhost000.verylegit.link",
           "very.verylegit.link",
           "not.verylegit.link",
           "ftp.verylegit.link",
           "win2003.verylegit.link",
           "irc.verylegit.link",
           "ctf.verylegit.link",
           "w61.verylegit.link",
           "666.verylegit.link",
           "1337.verylegit.link",
           "paypal.verylegit.link",
           "facebook.verylegit.link",
           "extremely.absolutely.completely.verylegit.link",
           "this.is.a.verylegit.link",
           "hey.look.a.verylegit.link",
           "click.on.this.verylegit.link",
           "win.a.free.ipad.verylegit.link",
           "click.here.to.get.ripped.in.three.weeks.verylegit.link"
          )
SAMPLE_LONG_URLS = ("google.com", "facebook.com", "i.imgur.com/OpYDgt3.gif")

SCARY_WORDS = (
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
    "64",
    "ip-camera",
    "botnet",
    "password",
    "filehost",
    "install-now",
    "creditcard",
    "email",
    "login",
    "torrent",
    "warez",
    "cracked",
    "ad",
    "mobiads",
    "shockwave-flash",
    "windows-update",
    "windows7",
    "windows8",
    "iphone",
    "free-iphone",
    "speedup",
    "exploit",
    "test",
    "server1",
    "server1337",
    "private-key"
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
    "png",
    "gif",
    "docx",
    "docm",
    "xlsx",
    "pptx",
    "js",
    "css",
    "min.js",
    "min.css",
    "html",
    "sh",
    "json",
    "pem",
    "gpg"

)

# Filetypes that the url could end with.
ENDING_FILETYPES = (
    "exe",
    "pdf",
    "docm",
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
    "!",
    "!!"
)

# Characters to replace randomly deleted letters.
# In some ways these are all weird strings.
WEIRD_STRINGS = (
    "0x8c"
    "*",
    ";",
    "-",
    ">",
    "@",
    "+"
)

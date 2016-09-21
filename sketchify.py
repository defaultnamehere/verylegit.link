
import random
import urllib
import sketchy_data

def add_random_domain(path):
    return "{domain}/{path}".format(domain=random.choice(sketchy_data.DOMAINS), path=path)


def generate_sketchy_url():
    """Example URL: heapslegit.link/ind%3x_x86_x64(free)___mov_7sk%a6-mov-%resume.pdf.jp%eg.exe.pdf.exe
    This method only generates the bit after the /, since the domain is ignored."""

    # Choose a few random sketchy scary words, removing duplicates in case there are any.
    scary_words = set((random.choice(sketchy_data.SCARY_WORDS) for _ in range(random.randint(1, sketchy_data.MAX_NUM_SKETCHY_WORDS))))

    # Choose the filetypes.
    filetypes = set((
        random.choice(sketchy_data.FILETYPES)
        for _ in range(random.randint(1, sketchy_data.MAX_NUM_FILETYPES))))

    # Choose the single ending filetype.
    ending_filetype = random.choice(sketchy_data.ENDING_FILETYPES)

    # Stick weird punctuation between all these weird words.
    sketchy_filename = [word + random.choice(sketchy_data.DELIMITERS) for word in scary_words]

    # Cut off the extra delimiter we added at the end with this extremely readable and maintanable line of Python.
    sketchy_filename[-1] = sketchy_filename[-1][:-1]

    # DYNAMIC TYPING.
    sketchy_filename = "".join(sketchy_filename)

    # URL encode the path.
    #sketchy_filename = urllib.parse.quote(sketchy_filename, safe="")

    # BUT WE'RE NOT DONE YET, CALL RIGHT NOW AND I'LL TRIPLE THE OFFER.
    weird_string_indicies = (random.choice(range(len(sketchy_filename) - 3)) for _ in range(sketchy_data.MAX_NUM_LETTER_REPLACEMENTS))

    # Make the string a list so we can add stuff at indicies.
    sketchy_filename = list(sketchy_filename)
    for index in weird_string_indicies:
        sketchy_filename.insert(index, random.choice(sketchy_data.WEIRD_STRINGS))

    sketchy_filename = "".join(sketchy_filename)

    # Put it all together.
    sketchy_path = "{sketchy_filename}.{filetypes}.{ending_filetype}".format(sketchy_filename=sketchy_filename, filetypes=".".join(filetypes), ending_filetype=ending_filetype)


    return sketchy_path

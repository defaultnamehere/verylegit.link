
import string
import random

import sketchy_data


def add_random_domain(path):
    return "{domain}/{path}".format(domain=random.choice(sketchy_data.DOMAINS), path=path)


RANDOM_STRING_CHARSET = (
    string.ascii_letters + string.digits + "+=_-;:.,~!`@*")

RANDOM_STRING_CHARSET_FIRST_CHAR = (string.ascii_letters + string.digits)

def generate_random_string(length=10):

    return random.choice(RANDOM_STRING_CHARSET_FIRST_CHAR) + "".join((random.choice(RANDOM_STRING_CHARSET) for _ in range(length - 1 )))


def generate_sketchy_url():
    """Example URL: heapslegit.link/ind%3x_x86_x64(free)___mov_7sk%a6-mov-%resume.pdf.jp%eg.exe.pdf.exe
    This method only generates the bit after the /, since the domain is ignored."""
    # Choose a few random sketchy scary words, removing duplicates in case
    # there are any.
    scary_words = set((
        random.choice(sketchy_data.SCARY_WORDS)
        for _ in range(random.randint(1, sketchy_data.MAX_NUM_SKETCHY_WORDS))))

    # Choose the filetypes.
    filetypes = list(set((
        random.choice(sketchy_data.FILETYPES)
        for _ in range(random.randint(1, sketchy_data.MAX_NUM_FILETYPES)))))

    # Choose the single ending filetype.
    ending_filetype = random.choice(sketchy_data.ENDING_FILETYPES)

    # No adjacent duplicates allowed.
    if filetypes[-1] == ending_filetype:
        # Replace the last random filetype with something other than the ending
        # filetype.
        filetypes[-1] = random.choice(
            list(set(sketchy_data.FILETYPES) - set(ending_filetype)))

    # Stick weird punctuation between all these weird words.
    sketchy_filename = [
        word + random.choice(sketchy_data.DELIMITERS)
        for word in scary_words]

    # Cut off the extra delimiter we added at the end with this extremely
    # readable and maintanable line of Python.
    sketchy_filename[-1] = sketchy_filename[-1][:-1]

    if len(sketchy_filename) > 3:
        # BUT WE'RE NOT DONE YET, CALL RIGHT NOW AND I'LL TRIPLE THE OFFER.
        weird_string_indicies = (
            random.choice(range(len(sketchy_filename) - 3))
            for _ in range(sketchy_data.MAX_NUM_LETTER_REPLACEMENTS))

        for index in weird_string_indicies:
            sketchy_filename.insert(
                index, random.choice(sketchy_data.WEIRD_STRINGS))

    # Sometimes, add a long random string to the beginning.
    if random.random() < sketchy_data.LONG_RANDOM_STIRNG_CHANCE:
        sketchy_filename.insert(
            0, generate_random_string(random.randint(5, 20)))

    # Always add a random number to reduce collisions, halfway through.
    sketchy_filename.insert(
        len(sketchy_filename) // 2,
        str(random.randint(0, sketchy_data.MAX_ANTI_COLLISION_NUMBER)))

    # DYNAMIC TYPING.
    sketchy_filename = "".join(sketchy_filename)

    # Put it all together.
    sketchy_path = "{sketchy_filename}.{filetypes}.{ending_filetype}".format(
        sketchy_filename=sketchy_filename, filetypes=".".join(filetypes), ending_filetype=ending_filetype)

    return sketchy_path

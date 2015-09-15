
import random
import urllib

import sketchy_data


class URLSketchifer():
    """Do the good stuff. YOU know what I mean"""

    # TODO Subdomains

    def __init__(self, long_url):
        """
        long_url: The url to shorten
        """
        self.long_url = long_url

    def generate_sketchy_url(self):
        """Example URL: heapslegit.link/ind%3x_x86_x64(free)___mov_7sk%a6-mov-%resume.pdf.jp%eg.exe.pdf.exe"""

        domain = random.choice(sketchy_data.DOMAINS)

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
        sketchy_filename = urllib.quote(sketchy_filename, safe="%/")

        # BUT WE'RE NOT DONE YET, CALL RIGHT NOW AND I'LL TRIPLE THE OFFER.
        replacement_indicies = (random.choice(range(len(sketchy_filename) - 3)) for _ in range(sketchy_data.MAX_NUM_LETTER_REPLACEMENTS))

        # Make the string a list so we can add stuff at indicies.
        sketchy_filename = list(sketchy_filename)
        for index in replacement_indicies:
            sketchy_filename[index] = random.choice(sketchy_data.WEIRD_STRINGS)

        sketchy_filename = "".join(sketchy_filename)

        # Put it all together.
        sketchy_path = "{sketchy_filename}.{filetypes}.{ending_filetype}".format(sketchy_filename=sketchy_filename, filetypes=".".join(filetypes), ending_filetype=ending_filetype)


        return "{domain}/{path}".format(domain=domain, path=sketchy_path)

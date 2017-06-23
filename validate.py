
import urlparse
import httplib

class URLValidator():
    """Decides whether or not a URL is welcome as part of this 150% legit service."""

    # I'm sure this will be secure enough.
    ALLOWED_PROTOCOLS = set(("http", "https", ""))

    # .... Really?
    MAXIMUM_URL_LENGTH = 2083

    def __init__(self, url):
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
        self.url = url
        self.url_parts = urlparse.urlparse(self.url)
        print(url)
        print(self.url_parts)
        self.protocol = self.url_parts.scheme

        # The domain becomes the path if there is no protocol.
        if self.protocol:
            self.domain = self.url_parts.netloc
        else:
            self.domain = self.url_parts.path

    def validate_url(self):
        """
        Checks that a URL is in fact a URL and not some other string
        url: The url to validate

        To add more validation checks, add a method to this class and call it in the all() function in this method.
        """

        return all((self.check_length(), self.check_external(), self.check_protocol(), self.check_dns()))

    def check_length(self):
        return len(self.url) <= self.MAXIMUM_URL_LENGTH

    def check_protocol(self):
        """Checks that the URL has a protocol that we're willing to obfuscate (http or https or no protocol)"""
        # Reject unknown protocols.
        return self.protocol in self.ALLOWED_PROTOCOLS

    def check_dns(self):
        """
        Does a DNS lookup on the domain part of the URL to check that it resolves
        """
        try:
            httplib.HTTPConnection(self.domain).request("GET", "/")
            return True
        except gaierror:
            return False

    def check_external(self):
        """No localhost for you."""
        return self.domain != "localhost"

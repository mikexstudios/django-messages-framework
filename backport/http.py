from Cookie import SimpleCookie

class CompatCookie(SimpleCookie):
    """
    Cookie class that handles some issues with browser compatibility.
    """
    def value_encode(self, val):
        # Some browsers do not support quoted-string from RFC 2109,
        # including some versions of Safari and Internet Explorer.
        # These browsers split on ';', and some versions of Safari
        # are known to split on ', '. Therefore, we encode ';' and ','

        # SimpleCookie already does the hard work of encoding and decoding.
        # It uses octal sequences like '\\012' for newline etc.
        # and non-ASCII chars.  We just make use of this mechanism, to
        # avoid introducing two encoding schemes which would be confusing
        # and especially awkward for javascript.

        # NB, contrary to Python docs, value_encode returns a tuple containing
        # (real val, encoded_val)
        val, encoded = super(CompatCookie, self).value_encode(val)

        encoded = encoded.replace(";", "\\073").replace(",","\\054")
        # If encoded now contains any quoted chars, we need double quotes
        # around the whole string.
        if "\\" in encoded and not encoded.startswith('"'):
            encoded = '"' + encoded + '"'

        return val, encoded

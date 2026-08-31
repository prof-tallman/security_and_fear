import string

# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
# Frequencies came from Practical Cryptography Website and were calculated from
# the German website Corpora Collection Leipzig and their English "Wortschatz"
# which is a "corpus-based monolingual dictionary" (whatever that means). But it
# included 4.5 billion characters of English text.

_english_monograms = [
    ("E", 12.10), ("T", 8.94), ("A", 8.55), ("O", 7.47), ("I", 7.33), ("N", 7.17),
    ("S", 6.73), ("R", 6.33), ("H", 4.96), ("L", 4.21), ("D", 3.87), ("C", 3.16),
    ("U", 2.68), ("M", 2.53), ("F", 2.18), ("G", 2.09), ("P", 2.07), ("W", 1.83),
    ("Y", 1.72), ("B", 1.60), ("V", 1.06), ("K", 0.81), ("J", 0.22), ("X", 0.19),
    ("Z", 0.11), ("Q", 0.10)
]

_english_digrams = [
    ("TH", 2.71), ("HE", 2.33), ("IN", 2.03), ("ER", 1.78), ("AN", 1.61), ("RE", 1.41),
    ("ES", 1.32), ("ON", 1.32), ("ST", 1.25), ("NT", 1.17), ("EN", 1.13), ("AT", 1.12),
    ("ED", 1.08), ("ND", 1.07), ("TO", 1.07), ("OR", 1.06), ("EA", 1.00), ("TI", 0.99),
    ("AR", 0.98), ("TE", 0.98), ("NG", 0.89), ("AL", 0.88), ("IT", 0.88), ("AS", 0.87),
    ("IS", 0.86), ("HA", 0.83), ("ET", 0.76), ("SE", 0.73), ("OU", 0.72), ("OF", 0.71)
]

_english_trigrams = [
    ("THE", 1.81), ("AND", 0.73), ("ING", 0.72), ("ENT", 0.42), ("ION", 0.42), ("HER", 0.36),
    ("FOR", 0.34), ("THA", 0.33), ("NTH", 0.33), ("INT", 0.32), ("ERE", 0.31), ("TIO", 0.31),
    ("TER", 0.30), ("EST", 0.28), ("ERS", 0.28), ("ATI", 0.26), ("HAT", 0.26), ("ATE", 0.25),
    ("ALL", 0.25), ("ETH", 0.24), ("HES", 0.24), ("VER", 0.24), ("HIS", 0.24), ("OFT", 0.22),
    ("ITH", 0.21), ("FTH", 0.21), ("STH", 0.21), ("OTH", 0.21), ("RES", 0.21), ("ONT", 0.20)
]

_english_quadgrams = [
    ("TION", 0.31), ("OTHE", 0.16), ("THEM", 0.12), ("NTHE", 0.27), ("TTHE", 0.16),
    ("RTHE", 0.12), ("THER", 0.24), ("DTHE", 0.15), ("THEP", 0.11), ("THAT", 0.21),
    ("INGT", 0.15), ("FROM", 0.10), ("OFTH", 0.19), ("ETHE", 0.15), ("THIS", 0.10),
    ("FTHE", 0.19), ("SAND", 0.14), ("TING", 0.10), ("THES", 0.18), ("STHE", 0.14), 
    ("THEI", 0.10), ("WITH", 0.18), ("HERE", 0.13), ("NGTH", 0.10), ("INTH", 0.17), 
    ("THEC", 0.13), ("IONS", 0.10), ("ATIO", 0.17), ("MENT", 0.12), ("ANDT", 0.10)
]

_english_quintgrams = [
    ("OFTHE", 0.18), ("ANDTH", 0.07), ("CTION", 0.05), ("ATION", 0.17), ("NDTHE", 0.07), 
    ("WHICH", 0.05), ("INTHE", 0.16), ("ONTHE", 0.07), ("THESE", 0.05), ("THERE", 0.09), 
    ("EDTHE", 0.06), ("AFTER", 0.05), ("INGTH", 0.09), ("THEIR", 0.06), ("EOFTH", 0.05),
    ("TOTHE", 0.08), ("TIONA", 0.06), ("ABOUT", 0.04), ("NGTHE", 0.08), ("ORTHE", 0.06),
    ("ERTHE", 0.04), ("OTHER", 0.07), ("FORTH", 0.06), ("IONAL", 0.04), ("ATTHE", 0.07),
    ("INGTO", 0.06), ("FIRST", 0.04), ("TIONS", 0.07), ("THECO", 0.05), ("WOULD", 0.04)
]

def _is_valid_key(key:str) -> bool:
    """ Verifies that a mixed alphabet key has exactly 26 (unique) letters. """
    # Key must have exactly 26 letters
    if len(key) != 26:
        return False
    # Key must contain each letter exactly once
    key_lower = key.upper()
    for ch in string.ascii_uppercase:
        if key_lower.count(ch) != 1:
            return False
    return True

def generate_key(password:str) -> str:
    """ Turns a secret password or passphrase into a mixed alphabet key. """
    key = ''
    # Start with each of the unique letters from the password
    for ch in password.upper():
        if ch.isalpha() and ch not in key:
            key += ch
    if len(key) == 0:
        raise ValueError("Password must contain letters A-Z")
    # After the password, fill in any missing letters from the alphabet
    # Start with the letter immediately *after* the last password letter
    # and, after reaching Z, wrap back around to A and continue
    idx = (string.ascii_uppercase.index(key[-1]) + 1) % 26
    for ch in string.ascii_uppercase[idx:] + string.ascii_uppercase[:idx]:
        if ch not in key:
            key += ch
    return key

def print_key(key:str) -> None:
    """ Helper function to display the plaintext and ciphertext alphabets. """
    key = generate_key(key)
    print(f"plaintext:  {string.ascii_lowercase}")
    print(f"CIPHERTEXT: {key}")

def encrypt(plaintext:str, password:str) -> str:
    """
    Encrypts a plaintext message with the given password/key. Spaces, numbers,
    and punctuation are preserved. The caller can remove these manually.
    """
    # Convert password to a full key. If its already a key nothing changes.
    key = generate_key(password)
    if not _is_valid_key(key):
        raise ValueError(f"Invalid password: {password}")
    # Encrypt each letter one at a time; numbers and punctation are unchanged
    plaintext_lower = plaintext.lower()
    for i in range(len(string.ascii_lowercase)):
        pt = string.ascii_lowercase[i]
        ct = key[i]
        plaintext_lower = plaintext_lower.replace(pt, ct)
    return plaintext_lower.upper()

def decrypt(ciphertext:str, password:str) -> str:
    """
    Decrypts a ciphertext message with the given password/key. Spaces, numbers,
    and punctuation are preserved.
    """
    # Convert password to a full key. If its already a key nothing changes.
    key = generate_key(password)
    if not _is_valid_key(key):
        raise ValueError(f"Invalid keywopasswordrd: {password}")
    # Decrypt each letter one at a time; numbers and punctation are unchanged    
    ciphertext_upper = ciphertext.upper()
    for i in range(len(string.ascii_lowercase)):
        pt = string.ascii_lowercase[i]
        ct = key[i]
        ciphertext_upper = ciphertext_upper.replace(ct, pt)
    return ciphertext_upper.lower()

def english_ngrams(n:int) -> list[tuple[str, float]]:
    """
    Returns the expected English ngram frequencies from pre-computed table. 
    Works for values of n=1-5.
    """
    if n == 1:
        return _english_monograms
    elif n == 2:
        return _english_digrams
    elif n == 3:
        return _english_trigrams
    elif n == 4:
        return _english_quadgrams
    elif n == 5:
        return _english_quintgrams
    else:
        raise ValueError(f"N-gram number {n} was not in valid range 1-5")

def print_english_ngrams(n:int, top:int = 10):
    """ Prints the expected English n-grams in a table. """
    ngrams = english_ngrams(n)
    for ngram in ngrams[:top]:
        print(f"{ngram[0]}: {ngram[1]}")

def text_ngrams(text:str, n:int, top:int = 10) -> list[tuple[str, float]]:
    """
    Returns a calculation of all ngrams in the text, ignoring all spaces and
    punctuation. Results are sorted and expressed as frequencies.
    """
    # Removes all spaces, numbers, and punctuation
    text_alpha_only = ""
    for ch in text.upper():
        if ch.isalpha():
            text_alpha_only += ch
    # Extract and count the ngrams
    total = len(text_alpha_only)-n+1
    table = {}
    for i in range(total):
        ngram = text_alpha_only[i:i+n]
        if ngram not in table:
            table[ngram] = 1
        else:
            table[ngram] += 1
    # Convert the raw counts to frequencies and sort the results
    for key, count in table.items():
        table[key] = round(100 * count / total, 3)
    table = sorted(table.items(), key=lambda x: x[1], reverse=True)
    return table

def print_text_ngrams(text:str, n:int, top:int = 10) -> None:
    """ Prints the calculated n-grams for a text as a table. """
    ngrams = text_ngrams(text, n)
    for ngram in ngrams[:top]:
        print(f"{ngram[0]}: {ngram[1]}")
    return None

def print_ngrams_side_by_side(text:str, n:int, top:int = 10) -> None:
    """
    Prints the n-grams for a text and the expected English distributions
    side-by-side for easy comparison. The n-grams are in sorted order based
    on frequency, but that does not mean the side-by-side words map directly
    to each other. 
    """
    ngrams_english = english_ngrams(n)
    ngrams_text = text_ngrams(text, n)
    print("Text Sample     | Standard English ")
    print("--------------- | -----------------")
    for i in range(len(ngrams_english[:top])):
        left_side = f"{ngrams_text[i][0]} {ngrams_text[i][1]:.3f}%"
        right_side = f"{ngrams_english[i][0]} {ngrams_english[i][1]:.3f}%"
        print(f"{left_side:<15} | {right_side:<15}")
    return None

def _format_text(text:str, width:int = 40) -> list[str]:
    """
    Formats a long string to be wrapped at a certain width. If the original
    string contains spaces, the text is wrapped according to words so it will
    appear jagged. If the origianl string had no spaces, it will be wrapped in
    a justified block format.
    """
    # Helps handle paragraphs with double \n at the end of the line.
    text = text.replace('\n\n', '\0').replace('\n', '').replace('\0', '\n')
    output_list = []
    if ' ' in text:
        for line in text.split('\n'):
            # Finds the last word in a line that fits the requested width
            while len(line) > 0:
                i = min(width, len(line))
                while i > 0 and line[i-1] != ' ':
                    i -= 1
                # Adds a line to the output and trims it from the larger string
                if i == 0:
                    output_list += [ line ]
                    line = ''
                else:
                    output_list += [ line[:i] ]
                    line = line[i:]
            # Manually add a new line to re-insert paragraph breaks
            output_list += [ '' ]
    else:
        for line in text.split('\n'):
            # No spaces between words, take chunks of 'width' characters
            for i in range(0, len(line), width):
                output_list += [ line[i:i+width] ]
            output_list += [ '' ]
    return output_list

def crack_side_by_side(ciphertext:str, key:dict[str, str], width:int) -> None:
    """
    Prints a (partially) cracked plaintext side-by-side next to the original
    ciphertext. Helps the cryptanalyst map solved words to the key.
    """
    # Decrypt the known key letters without modifying those that are missing.
    plaintext = ciphertext.upper()
    for ct, pt in key.items():
        plaintext = plaintext.replace(ct.upper(), pt.lower())
    # Word-wrap the two strings to display side-by-side.
    ciphertext_lines = _format_text(ciphertext, width)
    plaintext_lines = _format_text(plaintext, width)
    for i in range(len(ciphertext_lines)):
        print(f"{ciphertext_lines[i]:<{width + 1}} | {plaintext_lines[i]}")
    return None

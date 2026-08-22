# The Unbreakable Cipher #

## The Vigenère Cipher ##

One of the historically significant ciphers created in the Renaissance was le chiffre de Vigenère or simply the Vigenère Cipher. It is attributed to French cryptographer Blaise de Vigenère and was created as a polyalphabetic cipher to minimize the weaknesses of monoalphabetic ciphers to frequency analysis. The algorithm draws on previous work by Italian mathematician Leon Battista Alberti and cryptographer Giovan Battista Bellaso. For many years, the cipher was so secure that it was nicknamed le chiffre indéchiffrable (the indecipherable cipher).

Vigenère works by using a password to create multiple Caesar Shift Ciphers (CSC). Each letter in the password forms the beginning of a new CSC. The first CSC is used to encrypt the first letter of the plaintext, the second CSC is used to encrypt the second letter, and so on, all the way until the last CSC for the last letter in the password. Once all the letters in the password have been used up, the cipher restarts to the beginning of the password and continues on. So, for example, if the password was `"CAT"`, there would be three CSCs with the first being an offset of `2` for `"C"`, the second being an offset of `0` for `"A"`, and the last being an offset of `19` for `"T"`.

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
1st C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
2nd A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
3rd T U V W X Y Z A B C D E F G H I J K L M N O P Q R S

   Plaintext: Please excuse my dear Aunt Sally
Repeated Key: CATCAT CATCAT CA TCAT CATC ATCAT
              ↓↓↓↓↓↓ ↓↓↓↓↓↓ ↓↓ ↓↓↓↓ ↓↓↓↓ ↓↓↓↓↓
  Ciphertext: RLXCSX GXVWSX OY WGAK CUGV STNLR
```

Also, notice that the letter `A` in the key results in a Caesar shift of `0`. This means that every letter encrypted with A remains the same. At first this might seem to be a weakness, and someone might suggest removing any `A` letters from the key. However, assuming the key contains relatively few `A` letters, the unfortunate coincidence would be very difficult for an adversary to discover. By omitting the letter `A` from all keys, the number of keys would be reduced and this would have a greater impact on the overall security than including the letter `A`.

1. Encrypt John 3:16 with the Vigenère Cipher using the key "JOHN".
2. Decrypt the following ciphertext using the keyword "ROMANS".

   ```
   SIF GBV USYOAKKFMTRK YWE OJF CCHE SGI IE IA LYWE: JZZZQ WR OVFQ SGACZ EIAFVFE, PZIWET QAVR ROE MJ.
   ```

## Cryptanalysis ##

The Vigenère was difficult to crack because the rotating key hides the simple frequency patterns that cryptanalysts had exploited for hundreds of years. In fact, the cipher was so advanced that it took some 300 years to be cracked by British cryptographer Charles Babbage, and later, independently by Prussian cryptographer Friedrich Kasiski.

Babbage's critical insight into the Vigenère Cipher was that, for a large enough message, the repeating key will occasionally recycle itself over the same plaintext, causing small repeats in the ciphertext. The spacing between these repeats gives away information about the length of the key. And once the length of the key is known, the ciphertext letters can be divided into groups, one group for each letter in the key. For example, if the key were "CUI":

```
plaintext:  THE eagles landed beside THE north runway
key string: cui cuicui cuicui cuicui cui cuicu icuicu 
ciphertext: VBM guonya nuvfyl dyakxm VBM pizvb zwhecs
```

Once the ciphertext has been separated into groups, each group on its own can be evaluated with the same old frequency analysis tricks. No single group reveals the plaintext, but classic frequency analysis can provide the most likely shift values. Repeating the same technique for each group can help the cryptanalyst to discover the plaintext easily.

## Modern Cryptography ##

Although the Vigenère is now trivial to crack with a computer, it was an important step in the history of cryptography. The ideas gave rise to the first truly perfect cipher, the One-Time Pad. The One Time-Pad (OTP) is basically a Vigenère Cipher with a key that is the same length as the plaintext itself. Since the key does not repeat, there are no patterns for the cryptanalyst to study–not even the small patterns found by Babbage and Kasiski.

One-Time Pads can be demonstrated using letters and a Caesar-shift technique similar to Vigenère. But modern day OTP ciphers work on binary data and use the exclusive-or math operator (XOR). OTP with XOR, when used correctly with a one time random key that is the same length as the plaintext, is provably mathematically secure: it truly cannot be broken. However, there is a big difference between theoretical cryptography and practical in-a-war-in-a-trench cryptography.

3. Convert the text `MARTY` to binary using [8-bit ASCII encoding](ascii_utf8_binary_worksheet.md).
4. How many bits (0s and 1s) are needed to create an OTP key to encrypt `MARTY`?
5. Encrypt `MARTY` with a key that is all ones and provide your answer as a sequence of 0s and 1s binary digits (admittedly, this is a rather unsecure key).

During World War II, Soviet intelligence services used OTP to protect their communications but the American NSA was able to crack the messages. The reason that an unbreakable cipher could be broken was that wartime pressure made it difficult for the Soviets to distribute enough key material, so their agents reused old keys on new messages. This human tendency–perhaps born out of necessity–proved fatal by violating the rules required for perfect security. For more information, research the Venona Project, which was declassified in 1995. For example, see [Wikipedia](https://en.wikipedia.org/wiki/Venona_project), the [NSA Archives](https://www.nsa.gov/Helpful-Links/NSA-FOIA/Declassification-Transparency-Initiatives/Historical-Releases/Venona), and this at-first-glance accurate [YouTube documentary](https://www.youtube.com/watch?v=qvBsBomfL5g).

## Reflection Question ##

The Soviet reuse of OTP keys during World War II demonstrates that even theoretically perfect security systems can fail under operational pressure. In practice, humans often take shortcuts because of fear, urgency, exhaustion, convenience, limited resources, or competing priorities.

6. Describe a real-world situation (technological or otherwise) where people knowingly violate good security or safety procedures because the process is too difficult, slow, expensive, or inconvenient. Explain why the shortcut is attractive, what risks it creates, and whether the tradeoff reflects wise and responsible living.

Once again, assume that readers will not have access to this assignment; your writing should include enough background and introduction to stand on its own.

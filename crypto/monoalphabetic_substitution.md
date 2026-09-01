# Monoalphabetic Substitution #

## Mixed Alphabet Cipher ##

One of the most common families of ciphers is the Monoalphabetic Substitution Cipher. In this type of encryption, each letter in the alphabet is substituted one for another. If, for example, the letter `A` were to be substituted with the letter `X`, then it would mean that `X` always stands for `A` and `X` only ever stands for `A`. There is a 1-to-1 mapping from plaintext letter to ciphertext letter.

In some cases, such as the Caesar Shift Cipher and the Affine Cipher, there is a mathematical operation that is used to calculate the plaintext to ciphertext mapping. For example, the Caesar Shift Cipher rotates the alphabet by a number from 1–25. This mapping can be written mathematically as `C = P + k` (ignoring wraparound). The Affine Cipher uses a slightly more complex linear equation, `C = mP + b`, where `m` and `b` are key values. In both of these examples, the shift is a known mathematical operation.

The mixed alphabet cipher is a monoalphabetic substitution cipher that uses an arbitrary mapping from one letter to another. For instance, the letter `A` might map to `K`, `B` to `T`, `C` to `W`, and so on. The important characteristic is that the mapping appears to be random. With this in mind, the key can no longer be numbers, but must contain the full `A-Z` mapping, like this:

```
plaintext:  a b c d e f g h i j k l m n o p q r s t u v w x y z
CIPHERTEXT: K T W N P C E V U F A M I X D R G Z Y L Q O J H B S
```

1. How many unique keys are possible for this cipher? Explain your reasoning.

### Passwords ###

The arbitrary ordering makes the cipher stronger than Caesar Shift or Affine, but also harder to remember. To simplify, users of the cipher have resorted to using a password to recall the key.

A simple password trick can be used to generate mixed alphabet keys from memory. Begin by removing duplicate letters so that only the first occurrence remains. For instance, if the password was `"PASSWORD"`, the second letter `"S"` would be duplicate and must be removed to form `"PASWORD"`. This forms the beginning of the key. Finish the key by filling in the remaining alphabet letters (`B`, `C`, `E`, …) but beginning with the letter immediately following the last letter in the password, continue on in order, and wrap around from the end of the alphabet back to the beginning. In this case, the last letter of the de-duplicated password is `"D"`, so the next unused letter would be `"E"`, and the two letters remaining to wrap around at the end would be `"B"` and `"C"`, like this:

```
plaintext:  a b c d e f g h i j k l m n o p q r s t u v w x y z
CIPHERTEXT: P A S W O R D E F G H I J K L M N Q T U V X Y Z B C
```

2. Write out a plaintext/CIPHERTEXT encryption key for the password `MARTY`. 

## Cryptanalysis ##

Decrypting an intercepted message without knowing the key is tricky, but doable, for the mixed alphabet cipher. The technique is a bit of a guess-and-check method based on the relative frequency of letters in standard English (or whatever language the message is likely to be written in). Accurate guesses reveal real words while incorrect guesses produce gibberish.

To begin with, some letters can be reasoned out fairly quickly because they form short, common words such as `"a"`, `"I"`, `"the"`, `"and"`, etc. Beyond these initial guesses, the cryptanalyst needs to count the number of occurrences of each letter and compare it to the expected distribution for the plaintext language. For anyone with a sufficient collection of books and documents, these frequencies can be computed by hand or computer, although the work would be a little tedious. Thankfully, other people have published such work for English and other common languages, with the website practicalcryptography.com being one such resource.

Single letter frequencies are often not enough to crack an intercepted message. There are many letters whose frequencies are close to each other and many ciphertexts are relatively short, not necessarily following the standard letter distribution exactly. The next step is to find the most common *digrams* and *trigrams* (two and three letter sequences) and to compare these to the expected frequencies. For example, `"ING"`, `"ENT"`, `"ION"`, and `"ERS"` are all common trigrams in English. Determined individuals will almost always be able to crack these ciphertexts by hand, but computer algorithms have simplified this process considerably.

And finally, cryptanalysis often depends on contextual clues, probable phrases, repeated structures, and knowledge of likely plaintexts. If you recognize patterns--use them!

## Modern Algorithms ##

Many modern cryptographic algorithms use similar key generation techniques to turn passwords and passphrases into suitable keys. The biggest difference is that modern crypto works at the binary level, so the passphrase will be converted to binary data before it is converted to a key.

## Reflection Question ##

3. Use frequency analysis to crack the following mixed alphabet cipher. Include:
   - the plaintext (you may name/describe it if that is easier);
   - the password;
   - a short explanation of your methodology; and 
   - a list of the most helpful resources such as digrams, trigrams, computer tools, etc.

   Assume that readers will not have access to this assignment; your writing should include enough context to stand on its own. The goal is not so much to recover the plaintext, but to understand and explain your reasoning process used during cryptanalysis.

   ```
   MT ZLI EIKMTTMTK KUS NXIGZIS ZLI LIGBITY GTS ZLI IGXZL. ZLI IGXZL CGY JUXRQIYY GTS IRVZF, GTS SGXPTIYY NUBIXIS ZLI SIIV CGZIXY. GTS ZLI YVMXMZ UJ KUS CGY LUBIXMTK UBIX ZLI YAXJGNI UJ ZLI CGZIXY.
   
   ZLIT KUS YGMS, "QIZ ZLIXI EI QMKLZ," GTS ZLIXI CGY QMKLZ. GTS KUS YGC ZLGZ ZLI QMKLZ CGY KUUS. ZLIT LI YIVGXGZIS ZLI QMKLZ JXUR ZLI SGXPTIYY. KUS NGQQIS ZLI QMKLZ "SGF" GTS ZLI SGXPTIYY "TMKLZ."
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI JMXYZ SGF.
   
   ZLIT KUS YGMS, "QIZ ZLIXI EI G YVGNI EIZCIIT ZLI CGZIXY, ZU YIVGXGZI ZLI CGZIXY UJ ZLI LIGBITY JXUR ZLI CGZIXY UJ ZLI IGXZL." GTS ZLGZ MY CLGZ LGVVITIS. KUS RGSI ZLMY YVGNI ZU YIVGXGZI ZLI CGZIXY UJ ZLI IGXZL JXUR ZLI CGZIXY UJ ZLI LIGBITY. KUS NGQQIS ZLI YVGNI "YPF."
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI YINUTS SGF.
   
   ZLIT KUS YGMS, "QIZ ZLI CGZIXY EITIGZL ZLI YPF JQUC ZUKIZLIX MTZU UTI VQGNI, YU SXF KXUATS RGF GVVIGX." GTS ZLGZ MY CLGZ LGVVITIS. KUS NGQQIS ZLI SXF KXUATS "QGTS" GTS ZLI CGZIXY "YIGY." GTS KUS YGC ZLGZ MZ CGY KUUS. ZLIT KUS YGMS, "QIZ ZLI QGTS YVXUAZ CMZL BIKIZGZMUT—IBIXF YUXZ UJ YIIS-EIGXMTK VQGTZ, GTS ZXIIY ZLGZ KXUC YIIS-EIGXMTK JXAMZ. ZLIYI YIISY CMQQ ZLIT VXUSANI ZLI PMTSY UJ VQGTZY GTS ZXIIY JXUR CLMNL ZLIF NGRI." GTS ZLGZ MY CLGZ LGVVITIS. ZLI QGTS VXUSANIS BIKIZGZMUT—GQQ YUXZY UJ YIIS-EIGXMTK VQGTZY, GTS ZXIIY CMZL YIIS-EIGXMTK JXAMZ. ZLIMX YIISY VXUSANIS VQGTZY GTS ZXIIY UJ ZLI YGRI PMTS. GTS KUS YGC ZLGZ MZ CGY KUUS.
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI ZLMXS SGF.
   
   ZLIT KUS YGMS, "QIZ QMKLZY GVVIGX MT ZLI YPF ZU YIVGXGZI ZLI SGF JXUR ZLI TMKLZ. QIZ ZLIR EI YMKTY ZU RGXP ZLI YIGYUTY, SGFY, GTS FIGXY. QIZ ZLIYI QMKLZY MT ZLI YPF YLMTI SUCT UT ZLI IGXZL." GTS ZLGZ MY CLGZ LGVVITIS. KUS RGSI ZCU KXIGZ QMKLZY—ZLI QGXKIX UTI ZU KUBIXT ZLI SGF, GTS ZLI YRGQQIX UTI ZU KUBIXT ZLI TMKLZ. LI GQYU RGSI ZLI YZGXY. KUS YIZ ZLIYI QMKLZY MT ZLI YPF ZU QMKLZ ZLI IGXZL, ZU KUBIXT ZLI SGF GTS TMKLZ, GTS ZU YIVGXGZI ZLI QMKLZ JXUR ZLI SGXPTIYY. GTS KUS YGC ZLGZ MZ CGY KUUS.
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI JUAXZL SGF.
   
   ZLIT KUS YGMS, "QIZ ZLI CGZIXY YCGXR CMZL JMYL GTS UZLIX QMJI. QIZ ZLI YPMIY EI JMQQIS CMZL EMXSY UJ IBIXF PMTS." YU KUS NXIGZIS KXIGZ YIG NXIGZAXIY GTS IBIXF QMBMTK ZLMTK ZLGZ YNAXXMIY GTS YCGXRY MT ZLI CGZIX, GTS IBIXF YUXZ UJ EMXS—IGNL VXUSANMTK UJJYVXMTK UJ ZLI YGRI PMTS. GTS KUS YGC ZLGZ MZ CGY KUUS. ZLIT KUS EQIYYIS ZLIR, YGFMTK, "EI JXAMZJAQ GTS RAQZMVQF. QIZ ZLI JMYL JMQQ ZLI YIGY, GTS QIZ ZLI EMXSY RAQZMVQF UT ZLI IGXZL."
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI JMJZL SGF.
   
   ZLIT KUS YGMS, "QIZ ZLI IGXZL VXUSANI IBIXF YUXZ UJ GTMRGQ, IGNL VXUSANMTK UJJYVXMTK UJ ZLI YGRI PMTS—QMBIYZUNP, YRGQQ GTMRGQY ZLGZ YNAXXF GQUTK ZLI KXUATS, GTS CMQS GTMRGQY." GTS ZLGZ MY CLGZ LGVVITIS. KUS RGSI GQQ YUXZY UJ CMQS GTMRGQY, QMBIYZUNP, GTS YRGQQ GTMRGQY, IGNL GEQI ZU VXUSANI UJJYVXMTK UJ ZLI YGRI PMTS. GTS KUS YGC ZLGZ MZ CGY KUUS.
   
   ZLIT KUS YGMS, "QIZ AY RGPI LARGT EIMTKY MT UAX MRGKI, ZU EI QMPI AY. ZLIF CMQQ XIMKT UBIX ZLI JMYL MT ZLI YIG, ZLI EMXSY MT ZLI YPF, ZLI QMBIYZUNP, GQQ ZLI CMQS GTMRGQY UT ZLI IGXZL, GTS ZLI YRGQQ GTMRGQY ZLGZ YNAXXF GQUTK ZLI KXUATS."
   
   YU KUS NXIGZIS LARGT EIMTKY MT LMY UCT MRGKI.
       MT ZLI MRGKI UJ KUS LI NXIGZIS ZLIR;
       RGQI GTS JIRGQI LI NXIGZIS ZLIR.
   
   ZLIT KUS EQIYYIS ZLIR GTS YGMS, "EI JXAMZJAQ GTS RAQZMVQF. JMQQ ZLI IGXZL GTS KUBIXT MZ. XIMKT UBIX ZLI JMYL MT ZLI YIG, ZLI EMXSY MT ZLI YPF, GTS GQQ ZLI GTMRGQY ZLGZ YNAXXF GQUTK ZLI KXUATS."
   
   ZLIT KUS YGMS, "QUUP! M LGBI KMBIT FUA IBIXF YIIS-EIGXMTK VQGTZ ZLXUAKLUAZ ZLI IGXZL GTS GQQ ZLI JXAMZ ZXIIY JUX FUAX JUUS. GTS M LGBI KMBIT IBIXF KXIIT VQGTZ GY JUUS JUX GQQ ZLI CMQS GTMRGQY, ZLI EMXSY MT ZLI YPF, GTS ZLI YRGQQ GTMRGQY ZLGZ YNAXXF GQUTK ZLI KXUATS—IBIXFZLMTK ZLGZ LGY QMJI." GTS ZLGZ MY CLGZ LGVVITIS.
   
   ZLIT KUS QUUPIS UBIX GQQ LI LGS RGSI, GTS LI YGC ZLGZ MZ CGY BIXF KUUS!
   
   GTS IBITMTK VGYYIS GTS RUXTMTK NGRI, RGXPMTK ZLI YMDZL SGF.
   ```
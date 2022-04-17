# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.style


class NumberingType(object):
    """
    Const Class

    These constants are used to specify which numbering style is used.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API NumberingType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style_1_1NumberingType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.NumberingType'
    __ooo_type_name__: str = 'const'

    CHARS_UPPER_LETTER = 0
    """
    Numbering is put in upper case letters as \"A, B, C, D, ...\".
    """
    CHARS_LOWER_LETTER = 1
    """
    Numbering is in lower case letters as \"a, b, c, e,...\".
    """
    ROMAN_UPPER = 2
    """
    Numbering is in Roman numbers with upper case letters as \"I, II, III, IV, ...\".
    """
    ROMAN_LOWER = 3
    """
    Numbering is in Roman numbers with lower case letters as \"i, ii, iii, iv, ...\".
    """
    ARABIC = 4
    """
    Numbering is in Arabic numbers as \"1, 2, 3, 4, ...\".
    """
    NUMBER_NONE = 5
    """
    Numbering is invisible.
    """
    CHAR_SPECIAL = 6
    """
    Use a character from a specified font.
    """
    PAGE_DESCRIPTOR = 7
    """
    Numbering is specified in the page style.
    """
    BITMAP = 8
    """
    Numbering is displayed as a bitmap graphic.
    """
    CHARS_UPPER_LETTER_N = 9
    """
    Numbering is put in upper case letters as \"A, B, ..., Y, Z, AA, BB, CC, ...
    
    AAA, ...\".
    """
    CHARS_LOWER_LETTER_N = 10
    """
    Numbering is put in lower case letters as \"a, b, ..., y, z, aa, bb, cc, ...
    
    aaa, ...\".
    """
    TRANSLITERATION = 11
    """
    A transliteration module will be used to produce numbers in Chinese, Japanese, etc.
    """
    NATIVE_NUMBERING = 12
    """
    The NativeNumberSupplier service will be called to produce numbers in native languages.
    """
    FULLWIDTH_ARABIC = 13
    """
    Numbering for fullwidth Arabic number.
    """
    CIRCLE_NUMBER = 14
    """
    Bullet for Circle Number.
    """
    NUMBER_LOWER_ZH = 15
    """
    Numbering for Chinese lower case number as \"&#19968;,&#20108;,&#19977;...\".
    """
    NUMBER_UPPER_ZH = 16
    """
    Numbering for Chinese upper case number.
    """
    NUMBER_UPPER_ZH_TW = 17
    """
    Numbering for Traditional Chinese upper case number.
    """
    TIAN_GAN_ZH = 18
    """
    Bullet for Chinese Tian Gan as \"&#30002;,&#20057;,&#19993;...\".
    """
    DI_ZI_ZH = 19
    """
    Bullet for Chinese Di Zi as \"&#23376;,&#19985;,&#23493;...\".
    """
    NUMBER_TRADITIONAL_JA = 20
    """
    Numbering for Japanese traditional number.
    """
    AIU_FULLWIDTH_JA = 21
    """
    Bullet for Japanese AIU fullwidth.
    """
    AIU_HALFWIDTH_JA = 22
    """
    Bullet for Japanese AIU halfwidth.
    """
    IROHA_FULLWIDTH_JA = 23
    """
    Bullet for Japanese IROHA fullwidth.
    """
    IROHA_HALFWIDTH_JA = 24
    """
    Bullet for Japanese IROHA halfwidth.
    """
    NUMBER_UPPER_KO = 25
    """
    Numbering for Korean upper case number as \"&#22777;,&#36019;,&#21443;...\".
    """
    NUMBER_HANGUL_KO = 26
    """
    Numbering for Korean Hangul number as \"&#51068;,&#51060;,&#49340;...\".
    """
    HANGUL_JAMO_KO = 27
    """
    Bullet for Korean Hangul Jamo as \"&#12593;,&#12596;,&#12599;...\".
    """
    HANGUL_SYLLABLE_KO = 28
    """
    Bullet for Korean Hangul Syllable as \"&#44032;,&#45208;,&#45796;...\".
    """
    HANGUL_CIRCLED_JAMO_KO = 29
    """
    Bullet for Korean Hangul Circled Jamo as \"&#12896;,&#12897;,&#12898;...\".
    """
    HANGUL_CIRCLED_SYLLABLE_KO = 30
    """
    Bullet for Korean Hangul Circled Syllable as \"&#12910;,&#12911;,&#12912;...\".
    """
    CHARS_ARABIC = 31
    """
    Numbering in Arabic alphabet letters as \"&#1571;,&#1576;,&#1578;...\".
    
    **since**
    
        OOo 1.1.2
    """
    CHARS_THAI = 32
    """
    Numbering in Thai alphabet letters.
    
    **since**
    
        OOo 1.1.2
    """
    CHARS_HEBREW = 33
    """
    Numbering in Hebrew alphabet letters.
    
    **since**
    
        OOo 2.0
    """
    CHARS_NEPALI = 34
    """
    Numbering in Nepali alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_KHMER = 35
    """
    Numbering in Khmer alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_LAO = 36
    """
    Numbering in Lao alphabet letters.
    
    **since**
    
        OOo 2.0.1
    """
    CHARS_TIBETAN = 37
    """
    Numbering in Tibetan/Dzongkha alphabet letters.
    
    **since**
    
        OOo 2.0.3
    """
    CHARS_CYRILLIC_UPPER_LETTER_BG = 38
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1040;, &#1041;,  &#1042;, &#1043;, ..., &#1070;, &#1071;, &#1040;&#1074;, &#1040;&#1072;, &#1040;&#1074;, ... &#1040;&#1072;&#1072;, &#1040;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_BG = 39
    """
    Numbering in Cyrillic alphabet lower case letters as \"&#1072;, &#1073;, &#1074;, &#1075;, ..., &#1102;, &#1103;, &#1072; &#1072;,  &#1072;&#1073;, &#1072;&#1074;, ...  &#1072; &#1072; &#1072;,  &#1072; &#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_BG = 40
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1041;&#1073;, &#1042;&#1074;, ... &#1040;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_BG = 41
    """
    Numbering in Cyrillic alphabet upper case letters as \"&#1072;, &#1073;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1073;&#1073;, &#1074;&#1074;, ... &#1072;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_RU = 42
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, &#1042;, &#1043;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1040;&#1073;, &#1040;&#1074;, ... &#1040;&#1072;&#1072;, &#1040;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_RU = 43
    """
    Numbering in Russian Cyrillic alphabet lower case letters as \"&#1072;, &#1073;, &#1074;, &#1075;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1072;&#1073;, &#1072;&#1074;, ... &#1072;&#1072;&#1072;, &#1072;&#1072;&#1073;\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_RU = 44
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1040;, &#1041;, ..., &#1070;, &#1071;, &#1040;&#1072;, &#1041;&#1073;, &#1042;&#1074;, ... &#1040;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_RU = 45
    """
    Numbering in Russian Cyrillic alphabet upper case letters as \"&#1072;, &#1073;, ..., &#1102;, &#1103;, &#1072;&#1072;, &#1073;&#1073;, &#1074;&#1074;, ... &#1072;&#1072;&#1072;, ...\".
    
    **since**
    
        OOo 2.0.4
    """
    CHARS_PERSIAN = 46
    """
    Numbering in Persian alphabet letters (aa, be, pe, te, ...)
    
    **since**
    
        OOo 2.4
    """
    CHARS_MYANMAR = 47
    """
    Numbering in Myanmar alphabet letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_UPPER_LETTER_SR = 48
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_LOWER_LETTER_SR = 49
    """
    Numbering in Russian Serbian alphabet lower case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_UPPER_LETTER_N_SR = 50
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_CYRILLIC_LOWER_LETTER_N_SR = 51
    """
    Numbering in Serbian Cyrillic alphabet upper case letters.
    
    **since**
    
        OOo 3.1
    """
    CHARS_GREEK_UPPER_LETTER = 52
    """
    Numbering in Greek alphabet upper case letters.
    
    **since**
    
        LibreOffice 3.3
    """
    CHARS_GREEK_LOWER_LETTER = 53
    """
    Numbering in Greek alphabet lower case letters.
    
    **since**
    
        LibreOffice 3.3
    """
    CHARS_ARABIC_ABJAD = 54
    """
    Numbering in Arabic alphabet using abjad sequence.
    
    **since**
    
        LibreOffice 3.5
    """
    CHARS_PERSIAN_WORD = 55
    """
    Numbering in Persian words.
    
    **since**
    
        LibreOffice 3.5
    """
    NUMBER_HEBREW = 56
    """
    Numbering in Hebrew numerals.
    
    **since**
    
        LibreOffice 5.4
    """
    NUMBER_ARABIC_INDIC = 57
    """
    Numbering in Arabic-Indic numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    NUMBER_EAST_ARABIC_INDIC = 58
    """
    Numbering in East Arabic-Indic numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    NUMBER_INDIC_DEVANAGARI = 59
    """
    Numbering in Indic Devanagari numerals.
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_NUMBER = 60
    """
    Numbering in ordinal numbers of the language of the text node for example, 1st, 2nd, 3rd...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_CARDINAL = 61
    """
    Numbering in cardinal numbers of the language of the text node for example, One, Two, Three...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    TEXT_ORDINAL = 62
    """
    Numbering in ordinal numbers of the language of the text node for example, First, Second, Third...
    
    in English
    
    **since**
    
        LibreOffice 6.1
    """
    SYMBOL_CHICAGO = 63
    """
    Footnoting symbols according the University of Chicago style: *, &#2020;, &#2021;, &#00a7;, **, &#2020;&#2020; etc.
    
    **since**
    
        LibreOffice 6.4
    """
    ARABIC_ZERO = 64
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least two, as \"01,
    02, ..., 10, 11, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO3 = 65
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least three, as \"001, 002, ..., 100, 101, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO4 = 66
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least four, as \"0001, 0002, ..., 1000, 1001, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    ARABIC_ZERO5 = 67
    """
    Numbering is in Arabic numbers, padded with zero to have a length of at least five, as \"00001, 00002, ..., 10000, 10001, ...\".
    
    **since**
    
        LibreOffice 7.0
    """
    SZEKELY_ROVAS = 68
    """
    Numbering is in Szekely rovas (Old Hungarian) numerals.
    
    **since**
    
        LibreOffice 7.1
    """
    NUMBER_DIGITAL_KO = 69
    """
    Numbering is in Korean Digital number as \"ì¼,ì´,ì¼,...,ì¼ì,ì¼ìì, ...\".
    
    **since**
    
        LibreOffice 7.3
    """
    NUMBER_DIGITAL2_KO = 70
    """
    Numbering is in Korean Digital Number, reserved \"koreanDigital2\", as \"ä¸,äº,ä¸,...,ä¸ï¦²,ä¸ï¦²ï¦², ...\".
    
    **since**
    
        LibreOffice 7.3
    """
    NUMBER_LEGAL_KO = 71
    """
    Numbering is in Korean Legal Number, reserved \"koreanLegal\", as \"íë,ë,ì
    ,...\".
    
    **since**
    
        LibreOffice 7.3
    """

__all__ = ['NumberingType']
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.i18n.TransliterationModulesNew import (CharToNumHangul_ko, CharToNumLower_ko, CharToNumLower_zh_CN, CharToNumLower_zh_TW, CharToNumUpper_ko, CharToNumUpper_zh_CN, CharToNumUpper_zh_TW, END_OF_MODULE, FULLWIDTH_HALFWIDTH, HALFWIDTH_FULLWIDTH, HIRAGANA_KATAKANA, IGNORE_CASE, IGNORE_KANA, IGNORE_WIDTH, KATAKANA_HIRAGANA, LOWERCASE_UPPERCASE, NumToCharFullwidth, NumToCharHangul_ko, NumToCharKanjiShort_ja_JP, NumToCharLower_ko, NumToCharLower_zh_CN, NumToCharLower_zh_TW, NumToCharUpper_ko, NumToCharUpper_zh_CN, NumToCharUpper_zh_TW, NumToTextFormalHangul_ko, NumToTextFormalLower_ko, NumToTextFormalUpper_ko, NumToTextInformalHangul_ko, NumToTextInformalLower_ko, NumToTextInformalUpper_ko, NumToTextLower_zh_CN, NumToTextLower_zh_TW, NumToTextUpper_zh_CN, NumToTextUpper_zh_TW, TextToNumFormalHangul_ko, TextToNumFormalLower_ko, TextToNumFormalUpper_ko, TextToNumInformalHangul_ko, TextToNumInformalLower_ko, TextToNumInformalUpper_ko, TextToNumLower_zh_CN, TextToNumLower_zh_TW, TextToNumUpper_zh_CN, TextToNumUpper_zh_TW, UPPERCASE_LOWERCASE, ignoreBaFa_ja_JP, ignoreHyuByu_ja_JP, ignoreIandEfollowedByYa_ja_JP, ignoreIterationMark_ja_JP, ignoreKiKuFollowedBySa_ja_JP, ignoreMiddleDot_ja_JP, ignoreMinusSign_ja_JP, ignoreProlongedSoundMark_ja_JP, ignoreSeZe_ja_JP, ignoreSeparator_ja_JP, ignoreSize_ja_JP, ignoreSpace_ja_JP, ignoreTiJi_ja_JP, ignoreTraditionalKana_ja_JP, ignoreTraditionalKanji_ja_JP, ignoreZiZu_ja_JP, largeToSmall_ja_JP, smallToLarge_ja_JP)

    def _get_enum():
        # Dynamically create class that actually contains UNO enum instances
        _dict = {
            "__doc__": "Dynamically created class that represents com.sun.star.i18n.TransliterationModulesNew Enum. Class loosly mimics Enum",
            "__new__": uno_enum_class_new,
            "__ooo_ns__": "com.sun.star.i18n",
            "__ooo_full_ns__": "com.sun.star.i18n.TransliterationModulesNew",
            "__ooo_type_name__": "enum",
            "CharToNumHangul_ko": CharToNumHangul_ko,
            "CharToNumLower_ko": CharToNumLower_ko,
            "CharToNumLower_zh_CN": CharToNumLower_zh_CN,
            "CharToNumLower_zh_TW": CharToNumLower_zh_TW,
            "CharToNumUpper_ko": CharToNumUpper_ko,
            "CharToNumUpper_zh_CN": CharToNumUpper_zh_CN,
            "CharToNumUpper_zh_TW": CharToNumUpper_zh_TW,
            "END_OF_MODULE": END_OF_MODULE,
            "FULLWIDTH_HALFWIDTH": FULLWIDTH_HALFWIDTH,
            "HALFWIDTH_FULLWIDTH": HALFWIDTH_FULLWIDTH,
            "HIRAGANA_KATAKANA": HIRAGANA_KATAKANA,
            "IGNORE_CASE": IGNORE_CASE,
            "IGNORE_KANA": IGNORE_KANA,
            "IGNORE_WIDTH": IGNORE_WIDTH,
            "KATAKANA_HIRAGANA": KATAKANA_HIRAGANA,
            "LOWERCASE_UPPERCASE": LOWERCASE_UPPERCASE,
            "NumToCharFullwidth": NumToCharFullwidth,
            "NumToCharHangul_ko": NumToCharHangul_ko,
            "NumToCharKanjiShort_ja_JP": NumToCharKanjiShort_ja_JP,
            "NumToCharLower_ko": NumToCharLower_ko,
            "NumToCharLower_zh_CN": NumToCharLower_zh_CN,
            "NumToCharLower_zh_TW": NumToCharLower_zh_TW,
            "NumToCharUpper_ko": NumToCharUpper_ko,
            "NumToCharUpper_zh_CN": NumToCharUpper_zh_CN,
            "NumToCharUpper_zh_TW": NumToCharUpper_zh_TW,
            "NumToTextFormalHangul_ko": NumToTextFormalHangul_ko,
            "NumToTextFormalLower_ko": NumToTextFormalLower_ko,
            "NumToTextFormalUpper_ko": NumToTextFormalUpper_ko,
            "NumToTextInformalHangul_ko": NumToTextInformalHangul_ko,
            "NumToTextInformalLower_ko": NumToTextInformalLower_ko,
            "NumToTextInformalUpper_ko": NumToTextInformalUpper_ko,
            "NumToTextLower_zh_CN": NumToTextLower_zh_CN,
            "NumToTextLower_zh_TW": NumToTextLower_zh_TW,
            "NumToTextUpper_zh_CN": NumToTextUpper_zh_CN,
            "NumToTextUpper_zh_TW": NumToTextUpper_zh_TW,
            "TextToNumFormalHangul_ko": TextToNumFormalHangul_ko,
            "TextToNumFormalLower_ko": TextToNumFormalLower_ko,
            "TextToNumFormalUpper_ko": TextToNumFormalUpper_ko,
            "TextToNumInformalHangul_ko": TextToNumInformalHangul_ko,
            "TextToNumInformalLower_ko": TextToNumInformalLower_ko,
            "TextToNumInformalUpper_ko": TextToNumInformalUpper_ko,
            "TextToNumLower_zh_CN": TextToNumLower_zh_CN,
            "TextToNumLower_zh_TW": TextToNumLower_zh_TW,
            "TextToNumUpper_zh_CN": TextToNumUpper_zh_CN,
            "TextToNumUpper_zh_TW": TextToNumUpper_zh_TW,
            "UPPERCASE_LOWERCASE": UPPERCASE_LOWERCASE,
            "ignoreBaFa_ja_JP": ignoreBaFa_ja_JP,
            "ignoreHyuByu_ja_JP": ignoreHyuByu_ja_JP,
            "ignoreIandEfollowedByYa_ja_JP": ignoreIandEfollowedByYa_ja_JP,
            "ignoreIterationMark_ja_JP": ignoreIterationMark_ja_JP,
            "ignoreKiKuFollowedBySa_ja_JP": ignoreKiKuFollowedBySa_ja_JP,
            "ignoreMiddleDot_ja_JP": ignoreMiddleDot_ja_JP,
            "ignoreMinusSign_ja_JP": ignoreMinusSign_ja_JP,
            "ignoreProlongedSoundMark_ja_JP": ignoreProlongedSoundMark_ja_JP,
            "ignoreSeZe_ja_JP": ignoreSeZe_ja_JP,
            "ignoreSeparator_ja_JP": ignoreSeparator_ja_JP,
            "ignoreSize_ja_JP": ignoreSize_ja_JP,
            "ignoreSpace_ja_JP": ignoreSpace_ja_JP,
            "ignoreTiJi_ja_JP": ignoreTiJi_ja_JP,
            "ignoreTraditionalKana_ja_JP": ignoreTraditionalKana_ja_JP,
            "ignoreTraditionalKanji_ja_JP": ignoreTraditionalKanji_ja_JP,
            "ignoreZiZu_ja_JP": ignoreZiZu_ja_JP,
            "largeToSmall_ja_JP": largeToSmall_ja_JP,
            "smallToLarge_ja_JP": smallToLarge_ja_JP,
        }
        result = type('TransliterationModulesNew', (object,), _dict)
        return result

    TransliterationModulesNew = _get_enum()
else:
    from ...lo.i18n.transliteration_modules_new import TransliterationModulesNew as TransliterationModulesNew

__all__ = ['TransliterationModulesNew']


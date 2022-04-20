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
    from com.sun.star.i18n.TransliterationModules import (END_OF_MODULE, FULLWIDTH_HALFWIDTH, HALFWIDTH_FULLWIDTH, HIRAGANA_KATAKANA, IGNORE_CASE, IGNORE_KANA, IGNORE_MASK, IGNORE_WIDTH, KATAKANA_HIRAGANA, LOWERCASE_UPPERCASE, NON_IGNORE_MASK, NumToTextFormalHangul_ko, NumToTextFormalLower_ko, NumToTextFormalUpper_ko, NumToTextLower_zh_CN, NumToTextLower_zh_TW, NumToTextUpper_zh_CN, NumToTextUpper_zh_TW, UPPERCASE_LOWERCASE, ignoreBaFa_ja_JP, ignoreHyuByu_ja_JP, ignoreIandEfollowedByYa_ja_JP, ignoreIterationMark_ja_JP, ignoreKiKuFollowedBySa_ja_JP, ignoreMiddleDot_ja_JP, ignoreMinusSign_ja_JP, ignoreProlongedSoundMark_ja_JP, ignoreSeZe_ja_JP, ignoreSeparator_ja_JP, ignoreSize_ja_JP, ignoreSpace_ja_JP, ignoreTiJi_ja_JP, ignoreTraditionalKana_ja_JP, ignoreTraditionalKanji_ja_JP, ignoreZiZu_ja_JP, largeToSmall_ja_JP, smallToLarge_ja_JP)

    def _get_enum():
        # Dynamically create class that actually contains UNO enum instances
        _dict = {
            "__doc__": "Dynamically created class that represents com.sun.star.i18n.TransliterationModules Enum. Class loosly mimics Enum",
            "__new__": uno_enum_class_new,
            "__ooo_ns__": "com.sun.star.i18n",
            "__ooo_full_ns__": "com.sun.star.i18n.TransliterationModules",
            "__ooo_type_name__": "enum",
            "END_OF_MODULE": END_OF_MODULE,
            "FULLWIDTH_HALFWIDTH": FULLWIDTH_HALFWIDTH,
            "HALFWIDTH_FULLWIDTH": HALFWIDTH_FULLWIDTH,
            "HIRAGANA_KATAKANA": HIRAGANA_KATAKANA,
            "IGNORE_CASE": IGNORE_CASE,
            "IGNORE_KANA": IGNORE_KANA,
            "IGNORE_MASK": IGNORE_MASK,
            "IGNORE_WIDTH": IGNORE_WIDTH,
            "KATAKANA_HIRAGANA": KATAKANA_HIRAGANA,
            "LOWERCASE_UPPERCASE": LOWERCASE_UPPERCASE,
            "NON_IGNORE_MASK": NON_IGNORE_MASK,
            "NumToTextFormalHangul_ko": NumToTextFormalHangul_ko,
            "NumToTextFormalLower_ko": NumToTextFormalLower_ko,
            "NumToTextFormalUpper_ko": NumToTextFormalUpper_ko,
            "NumToTextLower_zh_CN": NumToTextLower_zh_CN,
            "NumToTextLower_zh_TW": NumToTextLower_zh_TW,
            "NumToTextUpper_zh_CN": NumToTextUpper_zh_CN,
            "NumToTextUpper_zh_TW": NumToTextUpper_zh_TW,
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
        result = type('TransliterationModules', (object,), _dict)
        return result

    TransliterationModules = _get_enum()
else:
    from ...lo.i18n.transliteration_modules import TransliterationModules as TransliterationModules

__all__ = ['TransliterationModules']


from yimt_bitext.utils.filters import get_lang2script, CharacterRatioFilter, AlphabetRatioFilter

if __name__ == "__main__":
    lang2script = get_lang2script()

    src_script = lang2script["en"]
    tgt_script = lang2script["zh"]
    char_filter = CharacterRatioFilter(scripts=(src_script, tgt_script), thresholds=(0.8, 0.8))
    print(char_filter.filter("a b cddd", "啊啊 啊啊啊啊+++++++"))
    print(char_filter.filter("a b cddd啊啊啊啊", "啊啊 啊啊啊啊"))

    print()
    src_script = lang2script["th"]
    tgt_script = lang2script["zh"]
    char_filter = CharacterRatioFilter(scripts=(src_script, tgt_script), thresholds=(0.8, 0.8))
    print(char_filter.filter("เบลเยียมและเนเธอแลนด", "日得拉"))
    print(char_filter.filter("DIW Continuous", "Taxpayer’s"))

    print()

    alphabet_filter = AlphabetRatioFilter(threshold=0.75, exclude_whitespace=True)
    print(alphabet_filter.filter("2000 나는 왜 권투 심판이 되려하는가", "2000在为什么我想成为一名拳击裁判?"))
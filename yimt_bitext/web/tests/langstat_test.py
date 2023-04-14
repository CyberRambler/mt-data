from yimt_bitext.web.base import BasicLangStat

if __name__ == "__main__":
    stat_f = "./d2h2lang2len.json"
    lang_stat = BasicLangStat(stat_f)
    lang_stat.update("http://www.abc.com/", {"zh": 100})
    assert lang_stat.stat_by_host("http://www.abc.com/") == {"zh": 100}

    lang_stat.update("http://en.abc.com/", {"en": 100})
    assert lang_stat.size() == 1
    assert len(lang_stat.hosts("abc.com")) == 2

    lang_stat.save()

from utils import dicts


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "error", "errorcheck") == "errorcheck"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"

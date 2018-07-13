from configs import lang

# TODO: Automate this process
# https://stackoverflow.com/questions/18090672/convert-dictionary-entries-into-variables-python
TAG_REQUIRED = lang['TAG_REQUIRED']
MEMBER_NOT_FOUND = lang['MEMBER_NOT_FOUND']
UNKNOWN_ERROR = lang['UNKNOWN_ERROR']
#
# locals().update(lang)
#
# for name, value in locals().copy().items():
#     print(name, value)

# __dict__ = lang

__dict__ = ['HEY_ALL']

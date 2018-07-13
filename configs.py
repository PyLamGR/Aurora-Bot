import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GenericConfig(metaclass=Singleton):
    name = 'generic_config'
    data = None
    # data_dot_seperated = None

    def __init__(self):
        self.load_config()
        print(self._init_message())

    def get_file_name(self):
        return '{}.json'.format(self.name)

    def load_config(self):
        with open(self.get_file_name()) as fp:
            self.data = json.load(fp)
    #     self.data_dot_seperated = GenericConfig.get_keys(self.data, '')
    #
    # @staticmethod
    # def get_keys(val, old="$"):
    #     if isinstance(val, dict):
    #         for k in val.keys():
    #             GenericConfig.get_keys(val[k], old + "." + str(k))
    #     elif isinstance(val, list):
    #         for i, k in enumerate(val):
    #             GenericConfig.get_keys(k, old + "." + str(i))
    #     else:
    #         print("{} : {}".format(old, str(val)))

    def _init_message(self):
        return '{} initialized ({})'.format(type(self).__name__, self.get_file_name())


class ConfConfig(GenericConfig):
    name = 'conf'


conf = ConfConfig().data


class LangConfig(GenericConfig):
    name = 'lang'

    def __init__(self, language=None):
        if not language:
            language = conf['lang']
        self.name = 'lang/{}'.format(language)
        super().__init__()


lang = LangConfig().data

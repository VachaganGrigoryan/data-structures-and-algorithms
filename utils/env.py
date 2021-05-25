from environment.property import read_env_file

# ToDo: Need to remove this file
class Env:

    TYPE = None
    URL = None
    HEADERS = {}

    @classmethod
    def set_env(cls, env_file, path='../environment'):
        env = read_env_file(path, env_file)
        cls.TYPE = env['graphql']['TYPE']
        cls.URL = env['graphql']['URL']
        cls.HEADERS = env['graphql']['HEADERS']

    def __str__(self):
        return f'''
        TYPE  {self.TYPE}
        URL  {self.URL}
        HEADERS   {self.HEADERS}
        '''

    @classmethod
    def set_headers(cls, headers):
        for key, value in headers.items():
            cls.HEADERS[key.lower()] = value




if __name__ == '__main__':

    Env.set_env("")
    print(Env.URL, Env.HEADERS)
    Env.set_headers()
    print(Env.URL, Env.HEADERS)



class vicks:
    def __init__(self,
                password,
                name = 'Anonymous',
                link = 'https://chatting-c937e-default-rtdb.firebaseio.com/',
                ):

        try:
            self.link = link
            self.name = name
            self.password = password

            from vicksbase import firebase as f
            self.firebase_obj = f.FirebaseApplication(self.link, None)

        except Exception as e:
            print(e)
            print('try: pip install imvickykumar999')

    def show(self):
        return self.link, self.name

    def pull(self,
             child = 'Group/Chat'):

        if self.password == '@Hey_Vicks':
            result = self.firebase_obj.get(f'{child}', None)
            return result

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def push(self, data = None,
                   child = 'Group/Chat'):

        if self.password == '@Hey_Vicks':
            if data == None:
                data = 0
            self.firebase_obj.put('/', child, data)

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def remove(self, child = 'A/B/C/led2'): # danger to run... loss of data.

        if self.password == '@Hey_Vicks':
            data = self.firebase_obj.delete('/', child)
            # return self.pull(child = '/')

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

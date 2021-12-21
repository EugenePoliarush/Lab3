class Validator:
 
    def check_value(self, val):
        try:
            value = int(val)
            return value
        except ValueError:
            print('{} shoud be int type'.format(val))
            return 0
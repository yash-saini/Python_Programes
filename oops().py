def oops():
    raise IndexError
def main():
    try:
        oops()
        print 'caught'
    except IndexError:
        print 'there is an error'


def oops():
    raise keyError
def main():
    try:
        oops()
        print 'caught'
    except IndexError:
        print 'there is an error'

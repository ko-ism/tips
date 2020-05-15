import re

# RE_STACK_ID = re.compile(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account>[\d]+)'
#             r':stack/(?P<stackname>[\w-]+)/[\w-]+')
RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):
    (?P<account>[\d]+)
    :stack/
    (?P<stackname>[\w-]+)/
    [\w-]+""", re.VERBOSE)


s = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
    'lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456')

print(s)

# m = re.match(
#             (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account>[\d]+)'
#             r':stack/(?P<stackname>[\w-]+)/[\w-]+')
#             , s)



try:
    m = RE_STACK_ID.match(s)
    if m:
        print(m.group('region'))
        print(m.group('account'))
        print(m.group('stackname'))
    else:
        raise Exception('Error')
except Exception as e:
    print(e)
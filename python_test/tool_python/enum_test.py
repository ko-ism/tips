import enum

db = {
    'stack1': 1,
    'stack2': 2
}

# STATUS_ACTIVE = 1
# STATUS_INACTIVE = 2
# if db['stack1'] == STATUS_ACTIVE:
#     print('shudwon')
# elif db['stack2'] == STATUS_INACTIVE:
#     print('terminate')

# @enum.unique
# class Status(enum.Enum):
class Status(enum.IntEnum):
    ACTIVE = 1
    # RENAME_ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

# print(Status.ACTIVE)
# print(repr(Status.ACTIVE))
# print(Status.ACTIVE.name)
# print(Status.ACTIVE.value)

if Status(db['stack1']) == Status.ACTIVE:
    print('shudwon')
elif Status(db['stack2']) == Status.INACTIVE:
    print('terminate')

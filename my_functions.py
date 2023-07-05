def hello():
    print("Hello, user!")


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)


# WHAT SHOULD BE PRINTED?
hello()
packed_list = pack("apple", "sandwich", "chips")
print("Packed list:", packed_list)
eat_lunch(["salad", "soup", "bread"])

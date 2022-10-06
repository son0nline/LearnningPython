def test_arg(*arg):
    for i in arg:
        print(i)

numbers = (1,2,3,4,5)
test_arg(numbers, "other")
test_arg(*numbers)
test_arg(1,2,3,4,5)
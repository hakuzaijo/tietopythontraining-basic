#!/usr/bin/env python3


def foo(*args, **kwargs):
    print("\nfoo called with:")
    print(args, kwargs)


def logger_wrapper(some_function, *args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print("- " + str(arg))
    print("")
    print("Keyword arguments:")
    for keyword, value in kwargs.items():
        print("- " + str(keyword) + " : " + str(value))

    some_function(args, kwargs)


def main():
    logger_wrapper(foo, 4, "arg", [2, 7, 5], key_arg=True, some_string="Hi")


if __name__ == "__main__":
    main()

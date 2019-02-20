def handle_error_by_throwing_exception():
    raise Exception("This isn't right!")


def handle_error_by_returning_none(input_data):
    if input_data != None:
        raise Exception("Result of valid input should not be None")


def handle_error_by_returning_tuple(input_data):
    pass


def filelike_objects_are_closed_on_exception(filelike_object):
    pass

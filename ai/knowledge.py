from ai.error_database import ERROR_DATABASE


def get_error_knowledge(error_type):

    for key, value in ERROR_DATABASE.items():

        if key in error_type:
            return value

    return None
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):

    # If an exception is thrown that we don't explicitly handle in our methods,
    # we delegate it to the default exception handler offered by DRF.
    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_validation_errors,
        'Http404': _handle404_error
    }
    # Identify the type of the current exception.
    exception_class = exc.__class__.__name__

    # If this exception is one that we can handle, handle it. Otherwise,
    # return the response generated earlier by the default exception 
    # handler.
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_validation_errors(exc, context, response):

    # Take the response generated by DRF and wrap it in the `errors` key.
    response.data = {
        'errors': response.data
    }

    return response


def _handle404_error(exc, context, response):
    # Take the response generated by DRF and decode the status_code
    # Override the response data with custom dict
    response.data = {
        'message': 'Not found'
    }
    return response

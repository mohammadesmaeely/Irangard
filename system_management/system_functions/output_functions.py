def process_response(message=None, data=None, errors=None):
    output = {}
    if message is not None:
        output.setdefault("message", message)
    if data is not None:
        output.setdefault("data", data)
    if errors is not None:
        output.setdefault("errors", errors)
    return output

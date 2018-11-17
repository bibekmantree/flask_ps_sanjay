def validate_book_obj(req_body):
    """

    :param req_body: Req object of a book
    :return: Bool: Valid or in valid
    """
    if ("name" in req_body
            and "bid" in req_body
            and "price" in req_body):
        return True
    else:
        return False


valid_obj = {
        "name": "SSH",
        "price": 45,
        "bid": 9
}


missing_name = {
        "price": 45,
        "bid": 9
}


missing_price = {
        "name": "SSH",
        "bid": 9
}


missing_bid = {
        "name": "SSH",
        "price": 45
}


junk = {
    "foo" : "bar"
}


empty = {}
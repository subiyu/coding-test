def solution(phone_book):
    hash_set = set()

    for number in phone_book:
        hash_set.add(number)

    for number in phone_book:
        target = ""
        for digit in number:
            target += digit
            if target in hash_set and target != number:
                return False

    return True
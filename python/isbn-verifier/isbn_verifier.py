def verify(isbn):
    """(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
    """
    # isbn_numeric=[int(c) if c != 'X' else int(c.replace('X', '10')) for c in isbn if c.isdigit() or c=='X']
    isbn=isbn.replace('-','')
    isbn_numeric = []
    for i, c in enumerate(isbn):
        if c.isdigit() or c == 'X':
            if c == 'X':
                if i!=9:
                    return False
                else:
                    c = '10'
            isbn_numeric.append(int(c))
    len_isbn = len(isbn_numeric)
    if len_isbn!=10:
        return False
    return (isbn_numeric[1-1] * 10 + isbn_numeric[2-1] * 9 + 
    isbn_numeric[3-1] * 8 + isbn_numeric[4-1] * 7 + 
    isbn_numeric[5-1] * 6 + isbn_numeric[6-1] * 5 + isbn_numeric[7-1] * 4 + 
    isbn_numeric[8-1] * 3 + isbn_numeric[9-1] * 2 + isbn_numeric[10-1] * 1) % 11 == 0


# import re
# import string


# def verify(isbn):
#     m = re.match(r'^\d-?\d{3}-?\d{5}-?[0-9X]$', isbn)
#     if not m:  # formal check first
#         return False
#     val = {
#         '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10
#     }
#     (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) = [
#         val[c] for c in isbn.replace("-", "")]
#     return (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) % 11 == 0

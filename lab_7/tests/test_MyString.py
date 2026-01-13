import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.MyString import MyString


def test_create_empty_string():
    ms = MyString('')
    assert len(ms) == 0


def test_create_from_string():
    ms = MyString('abc')
    assert len(ms) == 3
    assert ms.to_str() == 'abc'


def test_create_with_random():
    ms = MyString(initialize_with_random=True)
    assert len(ms) >= 1
    assert len(ms) <= 10


def test_create_with_uppercase_fails():
    try:
        ms = MyString('Abc')
        assert False
    except TypeError:
        assert True


def test_create_with_digit_fails():
    try:
        ms = MyString('abc123')
        assert False
    except TypeError:
        assert True


def test_getitem():
    ms = MyString('abcde')
    assert ms[0] == 'a'
    assert ms[2] == 'c'
    assert ms[-1] == 'e'


def test_setitem():
    ms = MyString('abc')
    ms[0] = 'z'
    assert ms[0] == 'z'
    assert ms.to_str() == 'zbc'


def test_setitem_uppercase_fails():
    ms = MyString('abc')
    try:
        ms[0] = 'A'
        assert False
    except TypeError:
        assert True


def test_setitem_digit_fails():
    ms = MyString('abc')
    try:
        ms[0] = '1'
        assert False
    except TypeError:
        assert True


def test_insert():
    ms = MyString('abc')
    ms.insert(1, 'z')
    assert ms.to_str() == 'azbc'


def test_insert_beyond_length():
    ms = MyString('abc')
    ms.insert(10, 'z')
    assert ms.to_str() == 'abcz'


def test_remove_character():
    ms = MyString('abcabc')
    ms.remove_character('b')
    assert ms.to_str() == 'acac'


def test_remove_with_start():
    ms = MyString('abcabc')
    ms.remove_character('b', start=2)
    assert ms.to_str() == 'abcac'


def test_remove_not_found_fails():
    ms = MyString('abc')
    try:
        ms.remove_character('z')
        assert False
    except ValueError:
        assert True


def test_replace():
    ms = MyString('abcabcabc')
    ms.replace('ab', 'xz', 2)
    assert ms.to_str() == 'xzcxzcabc'


def test_replace_all():
    ms = MyString('abcabcabc')
    ms.replace('ab', 'xy')
    assert ms.to_str() == 'xycxycxyc'


def test_find():
    ms = MyString('abcdef')
    assert ms.find('cd') == 2
    assert ms.find('xyz') == -1


def test_add():
    ms1 = MyString('abc')
    ms2 = MyString('def')
    ms3 = ms1 + ms2
    assert ms3.to_str() == 'abcdef'


def test_mul():
    ms = MyString('ab')
    ms2 = ms * 3
    assert ms2.to_str() == 'ababab'


def test_rotate():
    ms = MyString('abcde')
    ms.rotate(2)
    assert ms.to_str() == 'deabc'


def test_reverse_substring():
    ms = MyString('abcde')
    ms.reverse_substring(1, 3)
    assert ms.to_str() == 'adcbe'


def test_sliding_window():
    ms = MyString('aydzk')
    windows = ms.sliding_window(3, 2)
    assert windows == ['ayd', 'ydz', 'dzk']


def test_eq_ascii_sum():
    # Test equality based on ASCII sum
    # 'a' = 97, 'b' = 98, 'c' = 99
    # 'abc' sum = 97 + 98 + 99 = 294
    ms1 = MyString('abc')
    ms2 = MyString('abc')
    assert ms1 == ms2
    
    # Different strings with same ASCII sum
    # 'aac' = 97 + 97 + 99 = 293
    # 'abb' = 97 + 98 + 98 = 293
    ms3 = MyString('aac')
    ms4 = MyString('abb')
    assert ms3 == ms4
    
    # Different strings with different ASCII sum
    ms5 = MyString('abc')  # sum = 294
    ms6 = MyString('xyz')  # x=120, y=121, z=122, sum = 363
    assert not (ms5 == ms6)
    
    # Test with non-MyString type
    ms7 = MyString('abc')
    assert not (ms7 == "abc")
    assert not (ms7 == 123)


def test_all():
    test_create_empty_string()
    test_create_from_string()
    test_create_with_random()
    test_create_with_uppercase_fails()
    test_create_with_digit_fails()
    test_getitem()
    test_setitem()
    test_setitem_uppercase_fails()
    test_setitem_digit_fails()
    test_insert()
    test_insert_beyond_length()
    test_remove_character()
    test_remove_with_start()
    test_remove_not_found_fails()
    test_replace()
    test_replace_all()
    test_find()
    test_add()
    test_mul()
    test_rotate()
    test_reverse_substring()
    test_sliding_window()
    test_eq_ascii_sum()
    print("All tests passed!")


if __name__ == '__main__':
    test_all()

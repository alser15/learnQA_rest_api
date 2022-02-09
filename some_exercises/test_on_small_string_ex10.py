def test_ex10():
    phrase = input('Set a phrase: ')
    assert len(phrase) < 15, f'Введенная фраза {phrase} длиннее 15 символов.'

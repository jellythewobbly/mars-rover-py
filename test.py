from mars_rover import Marsrover


def test_correct_greeting():
    rover = Marsrover(4, 5, 'N')
    assert [4, 5, 'N'] == rover.return_coordinates()


# def test_fail():
#     thing = Thing("Albert")
#     assert "Wrong!" == thing.return_hello_name()

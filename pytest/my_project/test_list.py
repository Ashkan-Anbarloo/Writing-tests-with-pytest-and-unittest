from app import reverse_list

def test_reverse_list(sample_list):
    assert reverse_list(sample_list) == [5, 4, 3, 2, 1]

def test_list_length(sample_list):
    assert len(sample_list) == 5
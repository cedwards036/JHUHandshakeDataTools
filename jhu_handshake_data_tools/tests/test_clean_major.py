import unittest

from jhu_handshake_data_tools.src.clean_major import clean_major_with_colon_prefix
from jhu_handshake_data_tools.src.clean_major import clean_major_with_in_prefix
from jhu_handshake_data_tools.src.clean_major import clean_major_with_space_prefix
from jhu_handshake_data_tools.src.clean_major import make_major_cleaning_function


class TestCleanMajorWithColonPrefix(unittest.TestCase):

    def test_removes_text_before_the_first_colon(self):
        self.assertEqual('major', clean_major_with_colon_prefix('degree: major'))
        self.assertEqual('descriptor: major', clean_major_with_colon_prefix('degree: descriptor: major'))

    def test_does_not_remove_text_if_there_is_no_colon(self):
        self.assertEqual('degree in major', clean_major_with_colon_prefix('degree in major'))


class TestCleanMajorWithInPrefix(unittest.TestCase):

    def test_removes_lefthand_text_up_through_in_if_prefix_is_in_lookup(self):
        lookup = {'degree'}
        self.assertEqual('major', clean_major_with_in_prefix('degree in major', lookup))
        self.assertEqual('something in major', clean_major_with_in_prefix('degree in something in major', lookup))

    def test_does_not_remove_lefthand_text_if_prefix_is_not_in_lookup(self):
        lookup = {'credential'}
        self.assertEqual('degree in major', clean_major_with_in_prefix('degree in major', lookup))

    def test_does_not_remove_lefthand_text_if_major_does_not_have_the_word_in_in_it(self):
        lookup = {'MS'}
        self.assertEqual('MS', clean_major_with_in_prefix('MS', lookup))


class TestCleanMajorWithSpacePrefix(unittest.TestCase):

    def test_removes_lefthand_text_if_major_starts_with_a_prefix_in_the_lookup(self):
        lookup = ['degree', 'multi part degree']
        self.assertEqual('major', clean_major_with_space_prefix('degree major', lookup))
        self.assertEqual('complex major', clean_major_with_space_prefix('multi part degree complex major', lookup))

    def test_removes_first_matching_prefix_in_the_lookup_from_major(self):
        self.assertEqual('Global Finance', clean_major_with_space_prefix('MBA Global Finance', ['MBA', 'MBA Global']))
        self.assertEqual('Finance', clean_major_with_space_prefix('MBA Global Finance', ['MBA Global', 'MBA']))

    def test_does_not_remove_lefthand_text_if_prefix_is_not_in_lookup(self):
        lookup = ['credential']
        self.assertEqual('degree major', clean_major_with_space_prefix('degree major', lookup))

    def test_does_not_remove_lefthand_text_if_prefix_is_not_followed_by_whitespace(self):
        lookup = ['ME']
        self.assertEqual('MEDICINE', clean_major_with_space_prefix('MEDICINE', lookup))


class TestCleanMajor(unittest.TestCase):

    def test_cleans_major_with_colon_degree(self):
        clean_major = make_major_cleaning_function({''}, [])
        self.assertEqual('major', clean_major('degree: major'))

    def test_cleans_major_with_in_degree(self):
        clean_major = make_major_cleaning_function({'Certificate'}, [])
        self.assertEqual('major', clean_major('Certificate in major'))

    def test_cleans_major_with_space_degree(self):
        clean_major = make_major_cleaning_function({''}, ['MED'])
        self.assertEqual('major', clean_major('MED major'))

    def test_checks_major_for_colon_first(self):
        clean_major = make_major_cleaning_function({'MA'}, ['MA'])
        self.assertEqual('major', clean_major('MA in something: major'))

    def test_checks_major_for_in_prefix_before_checking_for_space_prefix(self):
        clean_major = make_major_cleaning_function({'MA'}, ['MA'])
        self.assertEqual('major', clean_major('MA in major'))

    def test_returns_the_original_major_of_no_degree_info_is_present(self):
        clean_major = make_major_cleaning_function({''}, [])
        self.assertEqual('major', clean_major('major'))

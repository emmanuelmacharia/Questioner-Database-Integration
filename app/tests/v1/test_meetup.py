
from .base_test import (
    BaseTest,
    CREATE_MEETUP_URL,
    ALL_MEETUPS_URL,
    SINGLE_MEETUP_URL
)


class TestMeetUps(BaseTest):
    '''tests all meetup endpoint'''
    def test_create_meetup(self):
        '''tests the create new event endpoint'''
        pass
    
    def test_missing_location(self):
        pass

    def test_missing_images(self):
        pass

    def test_missing_topic(self):
        pass

    def test_missing_date(self):
        pass

    def test_get_single_meetup(self):
        '''tests the get-single meetup  endpoint'''
        pass

    def test_no_meetup_found(self):
        pass

    def test_delete_meetup_success(self):
        '''tests the delete meetup endpoint'''
        pass

    def test_get_all_meetups(self):
        '''tests the get all meetups endpoint'''
        pass

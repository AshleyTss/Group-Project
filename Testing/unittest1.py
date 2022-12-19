# this is to test the clinet server and dycrpted file

import unittest
import sys
import unittest.mock


from unittest.mock import Mock


class TestClient(unittest.TestCase):


    # Check if dictionary exists
    mock = Mock()
    #from unittest.mock import patch
    #from socket_client import dic3
         
    @unittest.mock.patch('dic3.exists')
    @unittest.mock.patch('dic3.makedirs')
    def test_dict(self, mock_dic_dirs, mock_dic_exists):
        mock_dic_exists.return_value = True
        mock_dic_dirs('thing_to_create')
        mock_dic_dirs.assert_called_with('thing_to_create') 
    print("TBC")

    # test the enrypted original file    
    # actual = encrypt_data(original)
    # expected = 'encrypted_text!'
    #     self.assertEqual(actual, expected)

    def test_encrpyt(self):
        '''
        To test the serialisation process with no encrypt
        '''
        actual = no_encrypt(original)
        expected = '{1: 'Queen', 2: 'of', 3: 'UK'}'
        self.assertEqual(actual, expected,"serialise not successful")
        print("serialise checked")

    # def test_encrypt_input(self):
    #     encrypt = 'a'
    #     actual = 
    #     expected = 'Please enter y or n'
    #     if encrypt in ['y', 'n']:
    #         return
    #     else:
    #         print('Please enter y or n')
    #     self.assertEqual(actual, expected)

    def test_encrypt_json_pickling(self):
        '''
        To test if the pickling choice returns a json type
        '''
        pickling_type = 'json'
        if pickling_type == 'json':
            file_str = str(json.dumps(original))
        actual = file_str
        expected = '{1: 'Queen', 2: 'of', 3: 'UK'}'
        self.assertEqual(actual, expected, "pickling not successful")
        print("pickling checked")


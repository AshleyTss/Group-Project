# this is to test the clinet server and dycrpted file

import unittest
# import sys
import unittest.mock

from socket_server import *
from socket_client import *
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
    
    
    # test the enrypted outfile3    
    # actual = decryoted file
    # expected = 'encrypted_text as dict!'
    # self.assertEqual(actual, expected)
    
    def test_encrpyt(self):
        '''
        To test the serialisation process with no encrypt
        '''
        actual = decrypted
        expected = '{1: 'Queen', 2: 'of', 3: 'UK'}'
        self.assertEqual(actual, expected,"serialise not success")
        print("decrypted checked")

    # test the pickling orinigal
    

    def test_json_pickling(self):
        '''
        To test if the pickling choice returns a json type
        '''
        pickling_type = 'json'
        if pickling_type == 'json':
            file_str = str(json.dumps(original))
        actual = file_str
        expected = '{1: 'Queen', 2: 'of', 3: 'UK'}'
        self.assertEqual(actual, expected, "pickling not success")
        print("pickling checked")


if __name__ == '__main__':
    unittest.main()

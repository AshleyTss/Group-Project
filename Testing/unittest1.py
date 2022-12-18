# this is to test the clinet server

import unittest
import io
import os
import sys
import socketserver
import socket

from socket_client import Client
from mock import patch

"""
To capture standard output by just temporarily redirecting to a StringIO object
"""


class TestClient(unittest.TestCase):

    def test_help_list(self):
        # Capture everything sent to the console
        # Import StringIO from io and creat StringIO object
        # and redirect stdout.
        capturedOutput = io.StringIO()        
        sys.stdout = capturedOutput  

        #Class Under Test
        tick = Client()
        tick.help_list()
        sys.stdout = sys.__stdout__  # Reset redirect.

        # check if a particular string is present on the console (stdout)
        self.assertTrue("dict" in capturedOutput.getvalue())
        self.assertTrue("encrypt" in capturedOutput.getvalue())
        self.assertTrue("decrypt" in capturedOutput.getvalue())
        self.assertTrue("send-data" in capturedOutput.getvalue())
        self.assertTrue("send-data-encrypted" in capturedOutput.getvalue())
        self.assertTrue("exit" in capturedOutput.getvalue())
    print ("TBC")

    # Check if dictionary exists          
    @patch('dic3.exists')
    @patch('dic3.makedirs')
    def test_dict(self, dic3_dirs, dic3_exists):
        dic3_exists.return_value = True
        dic3_dirs('thing_to_create')
        dic3_dirs.assert_called_with('thing_to_create') 
   
  
    def test_serialise_dict(self):
        tick = Client()
        tick.serialise_dict('JSON')
  
        #check if files exists
        self.assertTrue(os.path.exists("dict.json"))


        #check if the file content json is correct
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        with open('dict.json', 'r') as f:
            print(f.read())
        self.assertTrue('{"name": "Queen", "of": "England"}' in capturedOutput.getvalue())
       
        self.assertTrue("<dictionary>" in capturedOutput.getvalue())
        self.assertTrue("<programme>" in capturedOutput.getvalue())
        sys.stdout = sys.__stdout__  # Reset stdout redirect.

        #cleanup files
        os.remove("dict.json")

if __name__ == '_main_':
    unittest.main()        
    
    print ("test ran successfully")

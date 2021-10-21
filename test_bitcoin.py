import unittest
from unittest import TestCase
from unittest.mock import patch 

import bitcoin


class TestBitcoin(TestCase):
    # test that a 200 res is returned
    @patch('bitcoin.request_coin_data')
    def test_getting_ok_response(self,mock_res):
        sample_json = {}
        with patch('bitcoin.request_coin_data') as mock_res:
            mock_res.return_value.status_code = 200
            
            
            mock_res.return_value.json.return_value = sample_json
            
            actual = bitcoin.request_coin_data()
            self.assertEqual(actual.status_code, 200)
            self.assertEqual(actual.json(), sample_json)
            # self.assertNotEqual(actual.json(),)
        
    

    @patch('bitcoin.request_coin_data')
    def test_bitcoin_to_dollars(self, mock_dollars):
        mock_dollars.return_value = {"bpi": {
                                "USD": {
                                    "code": "USD",
                                    "symbol": "&#36;",
                                    "rate": "66,062.1433",
                                    "description": "United States Dollar",
                                    "rate_float": 66062.1433
                                    },
                                
                                }
                                 }
        
        
        expected = 66062.1433
        convert = bitcoin.get_bitcoin_rate(1)
        self.assertEqual(expected,convert)
        
        
        

    
    
    @patch('bitcoin.request_coin_data')
    def test_bitcoin_to_dollar(self, mock_dollars):
        # example of res object
        example_api_res = {"bpi": {
                                "USD": {
                                    "code": "USD",
                                    "symbol": "&#36;",
                                    "rate": "66,062.1433",
                                    "description": "United States Dollar",
                                    "rate_float": 66062.1433
                                    },
                                
                                
                                }
                                 }
    
        
        mock_dollars.side_effect = [example_api_res]
        convert = bitcoin.get_bitcoin_rate(2)
        expected = 132124.2866
        self.assertEqual(expected,convert)
        
    
    

        
       
            


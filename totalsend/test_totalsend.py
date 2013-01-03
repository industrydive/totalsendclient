from totalsend import TotalSendClient, TotalSendError 
import unittest
import os

class TestTotalSend(unittest.TestCase):

    def setUp(self):
        self.ts = TotalSendClient()
        self.username = os.environ.get("TOTALSEND_API_USERNAME", None)
        self.password = os.environ.get("TOTALSEND_API_PASSWORD", None)
        if not self.username or not self.password:
            raise RuntimeError("Must create TOTALSEND_API_USERNAME and TOTALSEND_API_PASSWORD env variables first")

    # def test_login_fail(self):
    #     self.assertRaises(TotalSendError,self.ts.login('x','x'))

    def test_login_success(self):
        j = self.ts.login(self.username, self.password)
        sess_id = j['SessionID']
        # print sess_id
        self.assertGreater(len(sess_id),5)

    def test_campaigns(self):
        self.ts.login(self.username, self.password)
        camps = self.ts.get_campaigns()
        camp_id = camps['Campaigns'][0]['CampaignID']
        self.assertGreater(camp_id,0)
        camp = self.ts.get_campaign(camp_id)

if __name__ == '__main__':
    unittest.main()

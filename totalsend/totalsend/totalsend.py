import requests
import json

class TotalSendError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    def __str__(self):
        return "%s, %s" % (self.code, self.msg)

class TotalSendClient(object):
    session_id = None
    # def __init__(self, username, password):
    #   self.username
    #   self.login(user,password)
    def login(self, username, password):
        resp = self._fetch('User.Login', {'Username':username, 'Password':password})
        self.session_id = resp.get('SessionID')
        return resp

    def get_campaigns(self):
        resp = self._fetch('Campaigns.Get', {})
        return resp

    def get_campaign(self, campaign_id, retrieve_stats=False):
        resp = self._fetch('Campaign.Get', {'CampaignID':int(campaign_id), 'RetrieveStatistics':bool(retrieve_stats)})
        return resp

    def _fetch(self, command, params={}):
        url = 'https://app.totalsend.com/api.php?Command=%s&ResponseFormat=JSON' % (command,)
        if self.session_id:
            params['SessionID'] = self.session_id
        r = requests.get(url, params=params)
        j = r.json()
        if not j.get('Success',False):
            raise TotalSendError(j.get("ErrorCode"), j.get("ErrorText"))
        return j

# TODO： 网络传输分离
import json
import requests


def get(url, auth=None, body=None):
    try:
        if auth:
            header = {'Authorization': auth}
        else:
            header = None
        if body:
            res = requests.get(url, headers=header, data=json.dumps(body))
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['code'] == 1:
                    return data['data']
                else:
                    raise CodeError(data['message'])
            else:
                raise StatusError(str(res.status_code) + 'Error')
        else:
            res = requests.get(url, headers=header)
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['code'] == 1:
                    return data['data']
                else:
                    raise CodeError(data['message'])
            else:
                raise StatusError(str(res.status_code) + 'Error')
    except CodeError:
        return False
    except StatusError:
        return False


class CodeError(Exception):
    pass


class StatusError(Exception):
    pass



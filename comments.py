import requests

class comment_handler:
    def __init__(self, headers):
        self.headers = headers
        self.url = "https://api.usemotion.com/v1/comments"
        
    # NOT WORKING YET
    def create(self, task_id, content):
        data = {
            "taskId": task_id,
            "content": content,
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()

    def list(self, task_id, **kwargs):

        data = {
            "taskId": task_id,
            **kwargs
        }

        response = requests.get(self.url, headers=self.headers, params=data)


        return response.content


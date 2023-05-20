import requests

class project_handler:
    def __init__(self, headers, workspace_id):
        self.url = "https://api.usemotion.com/v1/projects"
        self.headers = headers
        self.workspace_id = workspace_id
        self.projects = {}

    # to do
    def retrieve(self, name):        
        response = requests.get(f"{self.url}/{self.projects[name]}", headers=self.headers)
        return response.json()
    
    def list(self, **kwargs):
        data = {
                 "workspaceId": self.workspace_id,
                 **kwargs
            }
        response = requests.get(self.url, headers=self.headers, params=data)
        return response.json()
        
    def create(self, name, **kwargs):
        self.name = name

        data = {
            "name": name,
            "workspaceId": self.workspace_id,
            **kwargs
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        self.projects.update({f"{self.name}": response.json().get('id')})

        return response.json()


    # NOT INCLUDED IN API
    #   
    # def delete(self, name):

    #     response = requests.delete(self.url, headers=self.headers, params=self.projects[name])
    #     return response.content


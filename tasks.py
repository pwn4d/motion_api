import requests

class task_handler:
    def __init__(self, workspace_id, headers):
        self.workspace_id = workspace_id
        self.headers = headers
        self.url = "https://api.usemotion.com/v1/tasks"
        self.task_data = ""
        self.task_id = ""
        self.tasks = {}

    def create(self, name, start_date=None, deadline_type=None, schedule=None, **kwargs):
        self.name = name
        self.data = kwargs

        data = {
            "name": self.name,
            "workspaceId": self.workspace_id,
            **self.data
        }

        response = requests.post(self.url, headers=self.headers, json=data)
        self.tasks.update({f"{self.name}": response.json().get('id')})

        return response.json()

    def delete(self, name):
        response = requests.delete(f"{self.url}/{self.tasks[name]}", headers=self.headers)
        return response.content

    def retrieve(self, name):
        response = requests.get(f"{self.url}/{self.tasks[name]}", headers=self.headers)
        return response.json()

    def update(self, name, start_date=None, deadline_type=None, schedule=None, **kwargs):
        data = {
            "name": name,
            **kwargs
        }

        response = requests.patch(f"{self.url}/{self.tasks[name]}", headers=self.headers, json=data)
        return response.json()
        

    def list(self, **kwargs):
        data = kwargs

        response = requests.get(f"{self.url}?workspaceId={self.workspace_id}", headers=self.headers, params=data)
        return response.json()
        

    def move_workspace(self, name, new_workspace_id, **kwargs):
        data = {
            "workspaceId": new_workspace_id,
            **kwargs
        }
        response = requests.patch(f"{self.url}/{self.tasks[name]}/move", headers=self.headers, json=data)
        return response.json()
    
    def create_reccuring(self, name, frequency, **kwargs):
        data = {
            "name": name,
            "workspaceId": self.workspace_id,
            "frequency": frequency,

            **kwargs 
        }
            
        response = requests.post("https://api.usemotion.com/v1/recurring-tasks", headers=self.headers,  json=data)
        return response.json()

    


    def list_recurring  (self, **kwargs):
        data = kwargs

        response = requests.get(f"https://api.usemotion.com/v1/recurring-tasks?workspaceId={self.workspace_id}", headers=self.headers, params=data)
        return response.json()
        
    def delete_recurring(self, name):
        response = requests.delete(f"https://api.usemo  tion.com/v1/recurring-tasks/{self.tasks[name]}", headers=self.headers)
        return response.content

  
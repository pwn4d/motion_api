import requests
import json
import tasks, comments, projects

USER_ID = "QvSMmuw9CvVvMbURk5LnT83xoEI3"
WORKSPACE_ID = "uSnaC83bpfEFT8uPF0gzL"

HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": "YLuP68mb3hA/egqsnMwi+eC3DctDEaGFLHZ0QYG/qOk="}

motion_task = tasks.task_handler(WORKSPACE_ID, headers=HEADERS)
motion_comments = comments.comment_handler(headers=HEADERS)
motion_project  = projects.project_handler(workspace_id=WORKSPACE_ID, headers=HEADERS)







print(motion_project.retrieve("2WOko-AgKiCYa4b5JBlM8    "))


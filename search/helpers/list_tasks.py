import json
import os


def get_files(folder):
    for f in os.listdir(folder):
        if f.endswith(".py"):
            yield f

    
if __name__ == '__main__':
    FOLDER = "docker_config/tasks"
    data = {
        "include": [
            {
                "taskfile": filename,
                "name": filename[:-3]
            }
            for filename in get_files(FOLDER)
        ]
    }

    data_json = json.dumps(data) 
    s = "::set-output name=matrix::%s" % data_json
    print(s)

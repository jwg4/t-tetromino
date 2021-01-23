import re
import subprocess


def get_commit_message():
    cmd = ['git', 'log', '-1', '--pretty=format:"%s"']
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode()


def get_tag(message):
    result = re.search("\[build(:([a-zA-Z0-9_-]*))?\]", message)
    if result:
        return result.group(2) or "vanilla"
    else:
        return None or "test"


if __name__ == '__main__':
    message = get_commit_message()
    tag_name = get_tag(message)
    s = "::set-output name=tag::%s" % (tag_name, )
    print(s)

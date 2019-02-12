# encoding: utf-8
import sys
from workflow import Workflow3, ICON_WEB, web
def main(wf):
    url = 'https://api.github.com/repos/robbyrussell/oh-my-zsh/contents/plugins'
    r = web.get(url)
    r.raise_for_status()

    contents = r.json()

    for content in contents:
        if content['type'] == 'dir':
            url = content['html_url']
            wf.add_item(title=content['name'], subtitle=url, arg=url, icon=ICON_WEB, valid=True)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3(libraries=['./lib'])
    sys.exit(wf.run(main))
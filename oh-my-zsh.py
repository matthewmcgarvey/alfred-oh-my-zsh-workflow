# encoding: utf-8
import sys
from workflow import Workflow3, ICON_WEB, web

def get_data():
    url = 'https://api.github.com/repos/robbyrussell/oh-my-zsh/contents/plugins'
    r = web.get(url)
    r.raise_for_status()
    return r.json()

def get_cache(wf):
    return wf.cached_data('data', get_data, max_age=0)

def main(wf):
    for content in get_cache(wf):
        if content['type'] == 'dir':
            url = content['html_url']
            wf.add_item(title=content['name'], subtitle=url, arg=url, icon=ICON_WEB, valid=True)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3(libraries=['./lib'])
    sys.exit(wf.run(main))
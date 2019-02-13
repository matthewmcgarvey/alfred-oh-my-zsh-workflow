# encoding: utf-8
import sys
from workflow import Workflow3, ICON_WEB, web

def get_plugins():
    url = 'https://api.github.com/repos/robbyrussell/oh-my-zsh/contents/plugins'
    r = web.get(url)
    r.raise_for_status()
    return r.json()

def get_data(wf):
    return wf.stored_data('data')

def save_data(wf, data):
    wf.store_data('data', data)

def clear_data(wf):
    wf.clear_data()

def main(wf):
    if len(wf.args) and wf.args[0] == 'refresh':
        clear_data(wf)
        save_data(wf, get_plugins())
        return
    
    data = get_data(wf)

    if data is None:
        data = get_plugins()
        save_data(wf, data)

    for content in data:
        if content['type'] == 'dir':
            url = content['html_url']
            wf.add_item(title=content['name'], subtitle=url, arg=url, icon=ICON_WEB, valid=True)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3(libraries=['./lib'])
    sys.exit(wf.run(main))
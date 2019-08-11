from pythonds9.Queue import Queue
from BuildGraph import build_graph
import requests
from io import StringIO

def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current_vert = vert_queue.dequeue()
        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('grey')
                nbr.set_pred(current_vert)
                vert_queue.enqueue(nbr)

        current_vert.set_color('black')

def traverse(y):
    x = y
    while x.get_pred():
        print(x.get_id())
        x = x.get_pred()

    print(x.get_id())

if __name__ == '__main__':
    url = 'http://www.webplaces.com/passwords/lists/4-letter-words-2478.txt'
    def get_words(url):
        req = requests.get(url)
        return StringIO(req.text)
    '''
    for line in get_words(url):
        print(line.strip())
    '''

    word_file = get_words(url)
    word_graph = build_graph(word_file)
    bfs(word_graph.get_vertex('sage'))

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from queue import Queue
import threading
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
     
        hostname = lambda url: url.split('/')[2]
        queue = Queue()
        seen = {startUrl}
        start_hostname = hostname(startUrl)
        seen_lock = threading.Lock()
        
        def worker():
            while True:
                url = queue.get()
                if url is None:
                    return

                for next_url in htmlParser.getUrls(url):
                    if next_url not in seen and hostname(next_url) == start_hostname:
                        seen_lock.acquire()
                        # Acquire lock to ensure urls are no enqueed multiple times
                        if next_url not in seen:
                            seen.add(next_url)
                            queue.put(next_url)
                        seen_lock.release()
                queue.task_done()
        
        num_workers = 8
        workers = []
        queue.put(startUrl)
        
        for i in range(num_workers):
            t = threading.Thread(target=worker)
            t.start()
            workers.append(t)
        
        # Wait until empty
        queue.join()
        
        for i in range(num_workers):
            queue.put(None)
        for t in workers:
            t.join()
        
        return list(seen)

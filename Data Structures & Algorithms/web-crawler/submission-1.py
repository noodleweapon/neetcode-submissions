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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hn = lambda x: x.split("/")[2]
        visited = set()
        def dfs(u):
            if u in visited:
                return
            visited.add(u)
            for v in htmlParser.getUrls(u):
                if hn(v) == hn(startUrl):
                    dfs(v)
        dfs(startUrl)
        return list(visited)

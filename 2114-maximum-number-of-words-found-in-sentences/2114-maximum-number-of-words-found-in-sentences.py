class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        def take_longer(item):
            long=item.split()
            return len(long)
        paragraph=sorted(sentences,key=take_longer,reverse=True)
        long=paragraph[0].split()
        return len(long)
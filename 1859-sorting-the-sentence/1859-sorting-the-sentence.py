class Solution:
    def sortSentence(self, s: str) -> str:
        def take_end(elem):
            return elem[-1]
        process_string=s.split(' ')
        processed_string=sorted(process_string, key=take_end )
        combined_words=processed_string[0][:-1]
        for i in range(1,len(processed_string)):
            combined_words+=' '+processed_string[i][:-1]
        return combined_words
            
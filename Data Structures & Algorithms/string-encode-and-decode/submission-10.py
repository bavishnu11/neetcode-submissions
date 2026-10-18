class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        l=[]
        a=0
        c=''
        while a<len(s):
            if s[a].isdigit():
                c+=s[a]
                a+=1
                if s[a]=='#':
                    l.append(s[a+1:a+1+int(c)])
                    a+=int(c)+1
                    c=''
        return l
                
            
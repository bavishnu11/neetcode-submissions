class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for i in strs:
            str1+=str(len(i))+'#'+i
        print(str1)
        return str1
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
                
            
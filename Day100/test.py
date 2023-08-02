import requests
import json

def main():

    with open ('a.txt','r',encoding='utf-8') as fff:
        f1=fff.read()
    b=eval(f1)
    print(b.get('code',11111))
        
    

if __name__=='__main__':
    main()

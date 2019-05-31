import requests

header ={
    'cookie':'SINAGLOBAL=222.168.127.150_1557889492.143167; SCF=AtdQS-vfp0297BjwwoLK2wqV6YZpSOSNmDBof0ObF5ryH-k1bXcSxg_duZ2BlPBaUY784HNPUSCe6ITUTQjtJEg.; Apache=222.168.127.150_1557918481.340758; ALF=1589456808; SUB=_2A25x34x4DeRhGeBN7FMZ9inPyzqIHXVTIxQwrDV_PUJbkNAKLRHmkW1NRFTUB0DSt5KCjPr_mLpqsFKZWGoN83xq; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW5o2Khqvv4LIR_4FP80jU55JpX5oz75NHD95Qce0Mp1hqNe05cWs4DqcjZTPSfdre_IsLV9Btt; U_TRS1=00000096.1d1025b8.5cdbfc81.08892aac; U_TRS2=00000096.1d1e25b8.5cdbfc81.f2976892; WEB2=bbe80e3d8b48fd0784febee3eab7ff98; bdshare_firstime=1557920899503; UOR=my.sina.com.cn,www.sina.com.cn,; ULV=1557920917734:1:1:1:222.168.127.150_1557918481.340758:',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',

}
response = requests.get("https://weibo.com/",headers=header)
print(response.status_code)
print(response.text)
with open("d:/a.html","w",encoding="utf-8") as f:
    f.write(response.text)
st={
    "id1":{"Name":"Jadan","class":"V","subject":"Math"},
    "id2":{"Name":"Jeremy","class":"V","subject":"Math"},
    "id3":{"Name":"Zara","class":"V","subject":"Math"},
    "id4":{"Name":"Jadan","class":"V","subject":"Math"}
}
rt={}
seen_keys=[]

for st_id, details in st.items():
    unique_key=(details["Name"],details["class"],details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        rt[st_id]=details

for k,v in rt.items():
    print(k,":",v)
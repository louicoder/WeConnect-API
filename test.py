 
reviews = [
        {
            "1fa0cd8e-a166-4a7a-b15a-7fc7356aa77c": [
                "403343af-d217-4b6e-822b-160538134562",
                "last review but not really last!"
            ]
        },
        {
            "6f8b328a-1a34-4b03-9592-c6d257a7e247": [
                "403343af-d217-4b6e-822b-160538134562",
                "this is another review!"
            ]
        },
        {
            "fa003968-b054-4055-af4a-4db460a27898": [
                "403343af-d217-4b6e-822b-160538134562",
                "review!"
            ]
        },
        {
            "5bc9f4e9-9fae-4522-93d0-82fcf75587cf": [
                "403343af-d217-4b6e-822b-160538134562",
                "review last!"
            ]
        }
    ]
    

ls= []

for x in reviews:
    for k, v in x.items():
        if v[0] == '403343af-d217-4b6e-822b-160538134562':
            ls.append(v)
    
print(ls)
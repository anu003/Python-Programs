def split_tags(ip_tag):
    selector_count = {"#":0, ".":0, "tag_name_count":0, "*":0}
    
    for ch in ip_tag:
        if ch in selector_count:
            ip_tag = ip_tag.replace(ch, " " + ch)
            
    tags_list = ip_tag.split()
    
    for tag in tags_list:
        if tag[0] in selector_count:
            selector_count[tag[0]] += 1
        else:
            selector_count["tag_name_count"] += 1           
    return selector_count

def compare(a, b):
    tags = ["#",".","tag_name_count","*"]
    a_tags = split_tags(a)
    b_tags = split_tags(b)

    for item in tags:
        if a_tags[item] != b_tags[item]:
            return a if a_tags[item] > b_tags[item] else b
    return b

print compare("hello.tag #pig.pig", "b")


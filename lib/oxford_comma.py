def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    items[len(items)-1] = "and " + items[len(items)-1]
    if len(items) > 2:
        return ", ".join(items)
    else:
        return " ".join(items)
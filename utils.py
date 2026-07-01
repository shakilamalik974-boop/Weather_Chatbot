def extract_city(text):

    words_to_remove = [
        "weather",
        "forecast",
        "temperature",
        "today",
        "tomorrow",
        "yesterday",
        "in",
        "of",
        "for"
    ]


    text = text.lower()


    for word in words_to_remove:
        text = text.replace(word, "")


    city = text.strip()


    return city.title()
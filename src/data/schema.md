**See last block in .gitignore to prevent leaking before embargo**

In order to compress the file as tight as possible we're abbreviating most of the keys and keeping the tabular data as an array of arrays (one array for current year, one array for previous year).


{
    "n": "School Name (string)",
    "d": "District (string)",
    "s": "Stars (number)",
    "c": "Classification (string) {optional}",
    "t": [
        []
    ]
}
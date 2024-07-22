## CHASM AREA ##

## Imported Modules ##

import msvcrt
from game_files.areas.temple_area import paragraph_100

## Paragraphs ##

def paragraph_80():
    print("Paragraph 80")
    print("Press any key to continue...")
    msvcrt.getch()
    paragraph_100()

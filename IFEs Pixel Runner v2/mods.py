
def fullrep(self: str,tb_rep: list[str]) -> str:
    for i in tb_rep:
        self = self.replace(i,'')
    return self

def file_read(opened: str) -> str:
    from pathlib import Path
    file_path = Path(opened)

    with file_path.open(mode='r') as file:
        lines = file.readlines()
        lines = ''.join(lines)
        
    return lines

def file_write(opened: str, __input: str) -> str:
    from pathlib import Path
    file_path = Path(opened)
    
    file_path.write_text(__input)

def position(txt: str,width: int,font_size: int,put_left: bool):
    if put_left:
        pos = int(((width-(width/2))-(len(txt)*font_size))/4)
    else:
        pos = int(((width*3)-(len(txt)*font_size))/4)
    return pos

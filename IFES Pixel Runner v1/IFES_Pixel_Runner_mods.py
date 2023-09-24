'''
 This module gives access to some specific mathematical and string-based functions

                                  Important note
                                  --------------
             This module was made by a 14 year old and is still in development

                                      ENJOY
                                      -----
'''
def fullrep(self: str,tb_rep: list[str]) -> str:
    '''
    Replaces every occurence of the strings in the list tb_rep\n
    
    Example:\n
    foo = '[eggs]'\n
    foo = fullrep(foo,['[',']'])\n
    
    foo -> eggs\n
    '''
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
    '''
    Overwrites the content of the file opened\n
    and replaces it with the input str and returns the file
    '''
    from pathlib import Path
    file_path = Path(opened)
    
    file_path.write_text(__input)
    with file_path.open(mode='r') as file:
        line = file.readlines()
        line = ''.join(line)
        
    return line
def approx(number: str, midpoint: int) -> list:
    '''
    Takes a string and returns the approximated integer of the value \n
    with the midpoint or highest approximable point being at the midpoint\n
    area
    
    '''
    number = str(number)
    number = number.split('.')
    ind,index1 = number[1],int(number[0])
    mod = len(ind)-1
    index2 = int(ind)-(int(ind)%(10**mod))
    index2 = str(index2).replace('0','')
    if index2 == '':
        index2 = '1'
    index2 = int(index2)
    
    if index2 < midpoint:
        pass
    else:
        index1 = int(number[0]) + 1

    return index1

def assign(val: list[object],tot_val: object):
    var = []
    for i in val:
        i = tot_val
        var.append(i)

    return var

def estim(number: str, __index: int) -> int:
        try:
            number = str(number)
            __index = int(__index)
            number = number.split('.')
            b = number[__index]
            c = int(b)
        except IndexError:
            raise IndexError('Index out of range, input should be in the range of value before the Proj.seperation point')

        return c
def number_gen(start: int,count: int,end: int) -> list[int]:
    '''
    Arithimetic Progression Generator
    ---------------------------------
    This functions takes the first param and returns a list of\n
    numbers incremented by the second param till it reaches the\n
    third
    
    Note
    ----        
    It is a bit technical and raises an error if the difference of the\n
    beginning and the end is not divisible by the common difference\n
    of the progression
    '''
    
    numslist = []
    new_start = start
    
    if (end - start)%count != 0:
        raise ValueError(
            'Ending parameter must be divisible by the positive difference between end and start'
        )
    else:
        while start != end:
            start = start + count
            num = int(start)
            numslist.append(num)
            
        numslist.insert(0, new_start)
            
    return numslist
def proj_file(open: str,split: str) -> str:
    import random
    from pathlib import Path
    file_path = Path(open)
    with file_path.open(mode='r') as file:
        lines = file.readlines()
        
    for l in lines:
        l = l.split(split)
    n_l = random.choice(l)

    return n_l
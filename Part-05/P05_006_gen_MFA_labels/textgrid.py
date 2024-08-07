##############################################################################
# The MIT License (MIT)
# 
# Copyright (c) 2016 Kyler Brown
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##############################################################################

#!/usr/bin/python

from collections import namedtuple
# from language_util import _SILENCE

Entry = namedtuple("Entry", ["start",
                             "stop",
                             "name",
                             "tier"])

def write_file(filename,results):
    with open(filename,'w',encoding='utf-8') as wid:
        wid.writelines([x +'\n' for x in results])

def read_file(filename):
    contents = []
    with open(filename,encoding='utf-8') as fid:
        contents=[x.strip()for x in fid.readlines()]
        return contents
    
def read_textgrid(filename):
    """
    Reads a TextGrid file into a dictionary object
    each dictionary has the following keys:
    "start"
    "stop"
    "name"
    "tier"

    Points and intervals use the same format, 
    but the value for "start" and "stop" are the same
    """
    content = read_file(filename)
    interval_lines = [i for i, line in enumerate(content)
                      if line.startswith("intervals [")
                      or line.startswith("points [")]
    tier_lines = []
    tiers = []
    for i, line in enumerate(content):
        if line.startswith("name ="):
            tier_lines.append(i)
            tiers.append(line.split('"')[-2])

    for i, line in enumerate(content):
        if line.startswith("xmax = "):
            time_array = line.split()
            time_array = [item for item in filter(lambda x: x.strip() != '', time_array)]
            duration = float(time_array[-1])
            break

    interval_tiers = _find_tiers(interval_lines, tier_lines, tiers)
    assert len(interval_lines) == len(interval_tiers)
    # adjust_list_phons= _adjust_Entry_phon([_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'phones'],duration)
    # adjust_list_words= _adjust_Entry_word([_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'words'],duration)
    adjust_list_phons= [_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'phones']
    adjust_list_words= [_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'words']
    adjust_list_tones= [_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'tones']
    adjust_list_breaks= [_build_entry(i, content, t) for i, t in zip(interval_lines, interval_tiers) if t == 'breaks']
    return adjust_list_phons,adjust_list_tones,adjust_list_words,adjust_list_breaks

def write_textgrid(filename,_list):
    """
    Reads a TextGrid file into a dictionary object
    each dictionary has the following keys:
    "start"
    "stop"
    "name"
    "tier"

    Points and intervals use the same format, 
    but the value for "start" and "stop" are the same
    File type ="ooTextFile"
    Object class = "TextGrid"

    xmin = 0.0
    xmax = 1.3750625
    tiers?<exists>
    size = 2
    item[]:
    """
    results = []
    results.append('File type = "ooTextFile"')
    results.append('Object class = "TextGrid"')
    results.append('')
    results.append('xmin = 0')
    results.append('xmax = ' + str(_list[0][-1].stop))
    results.append('tiers? <exists>')
    results.append('size = '+ str(len(_list)))
    results.append('item []:')
    """
    interval [1]:
        xmin = 0.0
        xmax = 0.090
        text =""
    """
    for i in range(len(_list)):
        results.append("    item [" + str(i + 1) + "]:")
        results.append('        class = "IntervalTier"')
        results.append('        name = \"' +_list[i][0].tier + '\"')
        results.append('        xmin = 0' )
        results.append('        xmax = ' + str(_list[0][-1].stop))
        results.append('        intervals: size = ' + str(len(_list[i])))
        results.extend(['        intervals [' + str(j+1)+']:\n'
                        + '            xmin = ' + str(entry.start) +'\n'
                        +'            xmax = ' + str(entry.stop)+'\n'
                        +'            text = \"' + entry.name.replace('"','""')+'\"'
                        for j, entry in enumerate(_list[i])])
        
        write_file(filename,results)
    
        
    


def _find_tiers(interval_lines, tier_lines, tiers):
    tier_pairs = zip(tier_lines, tiers)
    tier_pairs = iter(tier_pairs)
    cur_tline, cur_tier = next(tier_pairs)
    next_tline, next_tier = next(tier_pairs, (None, None))
    tiers = []
    for il in interval_lines:
        if next_tline is not None and il > next_tline:
            cur_tline, cur_tier = next_tline, next_tier
            next_tline, next_tier = next(tier_pairs, (None, None))           
        tiers.append(cur_tier)
    return tiers 


def _read(f):
    return [x.strip() for x in f.readlines()]


def _adjust_Entry_phon(textgrid_list, _duration):
    """adjust the textgrid_list, expecially the start and end:
    Start:
        label[0]=="" and lable[1]=="sp"  -----   merge, label[0]=="sil"
        label[0]<>"" and label[0]<>"sp"  -----   add, label[0]==”sil"
        label[0]=="" and label[1]<>"sp"  -----   change, label[0]=="sil"
        #label[0]=="sp" and label[1]<>"sp"-----   change, label[0]=="sil"
    End:
        label[-1]=="" and lable[-2]=="sp"  -----   merge, label[-1]=="sil"
        label[-1]<>"" and label[-1]<>"sp"  -----   add, label[-1]==”sil"
        label[-1]=="" and label[-2]<>"sp"  -----   change, label[-1]=="sil"
        #label[-1]=="sp" and label[-2]<>"sp"-----   change, label[-1]=="sil"
    """
    textgrid_list_new = textgrid_list
    #if len(textgrid_list_new) > 1:
    if textgrid_list_new[0].name == "" and textgrid_list_new[1].name in ['silv','sil','sp']:
        textgrid_list_new[1] = textgrid_list_new[1]._replace(name="sil")._replace(start=0)
        textgrid_list_new.pop(0)
    if textgrid_list_new[0].name != "" and textgrid_list_new[0].name not in ['silv','sil','sp']:
        textgrid_list_new.insert(0, Entry(start=0, stop=0.001, name="sil", tier="phones"))
        textgrid_list_new[1] = textgrid_list_new[1]._replace(start=0.001)
    if textgrid_list_new[0].name in ["", "sp"] and textgrid_list_new[1].name not in ['silv','sil','sp'] and textgrid_list_new[1].name != "":
        textgrid_list_new[0] = textgrid_list_new[0]._replace(name="sil")

    if textgrid_list_new[-1].name == "" and textgrid_list_new[-2].name in ['silv','sil','sp']:
        textgrid_list_new[-2] = textgrid_list_new[-2]._replace(name="sil")._replace(stop=_duration)
        textgrid_list_new.pop()
    if textgrid_list_new[-1].name != "" and textgrid_list_new[-1].name not in ['silv','sil','sp']:
        tmp_time = textgrid_list_new[-1].stop - 0.001
        textgrid_list_new.append(Entry(start=tmp_time, stop=_duration, name="sil", tier="phones"))
        textgrid_list_new[-2] = textgrid_list_new[-2]._replace(stop=tmp_time)
    if textgrid_list_new[-1].name in ["", "sp"] and textgrid_list_new[-2].name not in ['silv','sil','sp'] and textgrid_list_new[-2].name != "":
            textgrid_list_new[-1] = textgrid_list_new[-1]._replace(name="sil")
    return textgrid_list_new

def _adjust_Entry_word(textgrid_list, _duration):
    """adjust the textgrid_list, expecially the start and end:
    Start:
        label[0]=="" and lable[1]<>""  -----   delete,label[0]
    Middle:
        label[i]<>"" and label[i+1]==""-----   delete,label[i+1]
    End:
        label[-2]<>"" and lable[-1]==""  -----   delete,label[i+1]

    """
    textgrid_list_new = textgrid_list
    #if len(textgrid_list_new) > 1:
    if not textgrid_list_new[0].name and textgrid_list_new[1].name:
        textgrid_list_new[1] = textgrid_list_new[1]._replace(start=0)
        textgrid_list_new.pop(0)
    i=0
    tmp_length =len(textgrid_list_new)-1
    while i <tmp_length:
        if textgrid_list_new[i].name and not textgrid_list_new[i+1].name:
            textgrid_list_new[i] = textgrid_list_new[i]._replace(stop=textgrid_list_new[i+1].stop)
            textgrid_list_new.pop(i+1)
            tmp_length = len(textgrid_list_new)-1
        i+=1
    return textgrid_list_new
    



def write_csv(textgrid_list, filename=None, sep=",", header=True, save_gaps=False, meta=True):
    """
    Writes a list of textgrid dictionaries to a csv file.
    If no filename is specified, csv is printed to standard out.
    """
    columns = list(Entry._fields)
    if filename:
        f = open(filename, "w")
    if header:
        hline = sep.join(columns)
        if filename:
            f.write(hline + "\n")
        else:
            print(hline)
    for entry in textgrid_list:
        # if entry.name or save_gaps:  # skip unlabeled intervals
        #     row = sep.join(str(x) for x in list(entry))
        #     if filename:
        #         f.write(row + "\n")
        #     else:
        #         print(row)
        row = sep.join(str(x) for x in list(entry)[:-1])
        if filename:
            f.write(row + "\n")
        else:
            print(row)
    if filename:
        f.flush()
        f.close()
    if meta:
        with open(filename + ".meta", "w") as metaf:
            metaf.write("""---\nunits: s\ndatatype: 1002\n""")


def _build_entry(i, content, tier):
    """
    takes the ith line that begin an interval and returns
    a dictionary of values
    """
    start = _get_float_val(content[i + 1])  # addition is cheap typechecking
    if content[i].startswith("intervals ["):
        offset = 1
    else:
        offset = 0  # for "point" objects
    stop = _get_float_val(content[i + 1 + offset])
    label = _get_str_val(content[i + 2 + offset])
    return Entry(start=start, stop=stop, name=label, tier=tier)


def _get_float_val(string):
    """
    returns the last word in a string as a float
    """
    return float(string.split()[-1])


def _get_str_val(string):
    """
    returns the last item in quotes from a string
    """
    string = string.replace('text = ','')
    string = string.strip('"').replace('"','""')
    return string


def textgrid2csv():
    import argparse
    parser = argparse.ArgumentParser(description="convert a TextGrid file to a CSV.")
    parser.add_argument("TextGrid",
                        help="a TextGrid file to process")
    parser.add_argument("-o", "--output", help="(optional) outputfile")
    parser.add_argument("--sep", help="separator to use in CSV output",
                        default=",")
    parser.add_argument("--noheader", help="no header for the CSV",
                        action="store_false")
    parser.add_argument("--savegaps", help="preserves intervals with no label",
            action="store_true")
    args = parser.parse_args()
    tgrid = read_textgrid(args.TextGrid)
    write_csv(tgrid, args.output, args.sep, args.noheader, args.savegaps)


if __name__ == "__main__":
    #textgrid2csv()
    grid_file = r'C:\Users\shao\Desktop\data\A0.TextGrid'
    csv_file = r'C:\Users\shao\Desktop\data\A0.csv'
    tgrid = read_textgrid(grid_file)
    write_csv(tgrid, csv_file, sep=' ', header=False, meta=False)

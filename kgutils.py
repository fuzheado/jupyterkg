"""
Support functions for creating Wikidata Knowledge Graphs in Jupyter Widgets
"""

import csv 
import re

def sparql_qidlist_to_values_string(inlist: list) -> str:
    """
    Converts a list of Q numbers to a VALUES string used for SPARQL query

    Parameters
    ----------
    inlist : list
        List of format ['wd:Q123', 'wd:Q456', 'wd:Q789']

    Returns a string of format: '{wd:Q123 wd:Q456 wd:Q789}'
    """
    try:
        _values_string ='{' + ' '.join(x for x in inlist) + '}'
        return _values_string
    except:
        print ('Error: making values string')
        return None

def create_widget_tuple_list (labels: list, values: list) -> list:
    """
    Converts two lists into the list of tuples needed for Jupyter Widgets
    
    Parameters
    ----------
    labels : list like ['Label1', 'Label2'...]
    values : list like ['Value1', 'Value2'...]
    
    Output:
        [('Label1', 'Value1'),...]
    """
    _merged = tuple(zip(labels, values))
    return _merged

def read_wd_selector_list(filename: str) -> list:
    """
    Reads a CSV file of format 'Q842858,Nationalmuseum,123" and
    return a list of tuples, that can be used right away for a Jupyter Widgets selector

    Output list: [('Any', 'Any'), ('Nationalmuseum (123)', 'wd:Q842858'), ...

    Parameters
    ----------
    filename : str
        CSV file
    """

    ilist = [tuple(['Any','Any'])]
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Process label
                # If there is a count, like 'Q123,Man,456'
                if len(row) > 2:  
                    _label = '{} ({})'.format(row[1], str(row[2]))
                else:
                    _label = row[1]

                # Process QID
                # We should accept only strings that are of format:
                #   Q506
                #   http://www.wikidata.org/entity/Q506
                _result = re.search('(Q[0-9]+)', row[0])
                if _result:
                    _qid = _result.group(1)
                    _wdqid = 'wd:'+_qid
                
                    # Add to list
                    ilist += [tuple([_label, _wdqid])]
        return ilist
    except FileNotFoundError:
        return []

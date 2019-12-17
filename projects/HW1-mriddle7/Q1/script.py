import http.client
import json
import time
import timeit
import sys
import collections
from pygexf.gexf import *
import urllib.request
from pprint import pprint as pp


# implement your data retrieval code here
#api_key = sys.argv[1]
base_url = 'https://rebrickable.com/api/v3/lego/'
key_base = '?key='
key = sys.argv[1]
data_url = 'https://rebrickable.com/api/v3/lego/sets/?key=' + key
other_url = 'https://rebrickable.com/api/v3/lego/sets/?key=' + key + '&page=1&page_size=300&ordering=-num_parts'

set_data = urllib.request.Request(other_url)
set_data = urllib.request.urlopen(set_data)
set_data = set_data.read()
set_data = json.loads(set_data)

# complete auto grader functions for Q1.1.b,d
def min_parts():
    """
    Returns an integer value
    """
    return 1094

def lego_sets():
    """
    return a list of lego sets.
    this may be a list of any type of values
    but each value should represent one set

    e.g.,
    biggest_lego_sets = lego_sets()
    print(len(biggest_lego_sets))
    > 280
    e.g., len(my_sets)
    """
    return [sets for sets in set_data['results']]

#returns a list of parts for a given lego set
def get_part_list(lego_set):
    set_url = base_url +'sets/' + lego_set['set_num'] + '/parts/' + key_base + key + '&page_size=1000'
    data = urllib.request.Request(set_url)
    data = urllib.request.urlopen(data)
    data = data.read()
    data = json.loads(data)
    part_list = data['results']
    return part_list

#takes a list of parts, sorts by the quantity of those parts present in a set, and returns at most 20 elements from the new ordered list
def sort_parts(part_list):
    sort_by_quantity = sorted(part_list, key = lambda x: x['quantity'], reverse = True)
    try:
        return sort_by_quantity[0:20]
    except:
        return sort_by_quantity[0:len(sort_by_quantity)]

#creates a new id for each part(dictionary form) based on combination of number and color (as specified in directions)
def id_construct(part):
    part['unique_id'] = part['part']['part_num'] + part['color']['rgb']

#creates part lists for each set in a list
def get_parts(set_list):
    list_of_lists_of_parts = []
    for a_set in set_list:
        parts = get_part_list(a_set)
        top_parts = sort_parts(parts)
        list_of_list_of_parts.append(top_parts)
    return list_of_list_of_parts



lego_sets_info = lego_sets()

def big_request_function():
    for lego_set in lego_sets_info:
        time = time()
        lego_set_parts = get_part_list(lego_set)
        time2 = time()
        wait_time = int(time2 - time)
        if wait_time < 1:
            time.sleep(1 - wait_time)
        lego_set_parts = sort_parts(lego_set_parts)
        for part in lego_set_parts:
            id_construct(part)
            part_list.append(part)


#make a graph of sets and associated parts
def gexf_graph():
    
    start = time.time()
    """
    return the completed Gexf graph object
    """
    # you must replace these lines and supply your own graph
    gexf = Gexf("Matthew Riddle", "Lego Bricks in Sets")
    graph = gexf.addGraph("undirected", "static", "A graph of Lego Sets and their Parts.")

    graph.addNodeAttribute(title = 'Type', type = 'string', force_id = 0, defaultValue = 'set')
    #att.declareAttribute(type = 'string', attClass = 'node', defaultValue = 'set', title = 'Type')
    
    for a_set in lego_sets_info:
        node = graph.addNode(a_set['set_num'], a_set['name'], r = '0', g = '0', b = '0')
        node.addAttribute(id = '0', value = 'set')
        
    #for part in part_list:
        #graph.addNode(part['unique_id'], part['part']['name'], r = str(part['color'][0]), g = str(part['color'][1]), b = str(part['color'][2]))

    edge_id = 1
    for a_set in lego_sets_info:
        time1 = time.time()
        lego_set_parts = get_part_list(a_set)
        lego_set_parts = sort_parts(lego_set_parts)
        
        for part in lego_set_parts:
            id_construct(part)
            
        convert_color_val(lego_set_parts)
        
        for part in lego_set_parts:
            node = graph.addNode(part['unique_id'], part['part']['name'], r = str(part['color'][0]), g = str(part['color'][1]), b = str(part['color'][2]))
            node.addAttribute(id = '0', value = 'part')
            graph.addEdge(edge_id, source = a_set['set_num'], target = part['unique_id'], weight = part['quantity'])
            edge_id += 1
            
        time2 = time.time()
        wait_time = int(time2 - time1)
        if wait_time < 1:
            time.sleep(1 - wait_time)
            
    #graph.addEdge(uniqueid, set_num, uniquepartid, partquantity)

    
    output_file=open("bricks_graph.gexf","wb")
    gexf.write(output_file)
    output_file.close()
    end = time.time()
    print("Runtime:" + str(int(end - start)))
    
    return gexf.graphs[0]

def hex_to_rgb(hex_code):
    hex_strip = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_strip[i:i+2], 16) for i in (0, 2, 4))
    return rgb_code

def convert_color_val(parts_list):
    for part in parts_list:
        part['color'] = hex_to_rgb(part['color']['rgb'])


# complete auto-grader functions for Q1.2.d
def avg_node_degree():
    """
    hardcode and return the average node degree
    (run the function called “Average Degree”) within Gephi
    """
    # you must replace this value with the avg node degree
    return 5.577

def graph_diameter():
    """
    hardcode and return the diameter of the graph
    (run the function called “Network Diameter”) within Gephi
    """
    # you must replace this value with the graph diameter
    return 8

def avg_path_length():
    """
    hardcode and return the average path length
    (run the function called “Avg. Path Length”) within Gephi
    :return:
    """
    # you must replace this value with the avg path length
    return 4.395

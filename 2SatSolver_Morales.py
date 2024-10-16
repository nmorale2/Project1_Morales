#!/usr/bin/env python3

import csv
from collections import defaultdict
import sys

def tarjan_scc(graph, n):
    """Tarjan's algorithm to find strongly connected components."""
    index = 0
    stack = []
    indices = [-1] * (2 * n)  # To store the discovery time of nodes
    lowlink = [-1] * (2 * n)  # The lowest point reachable from the node
    on_stack = [False] * (2 * n)  # To track nodes in the recursion stack
    sccs = []
    
    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in graph[v]:
            if indices[w] == -1:  # If w has not yet been visited
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:  # If w is in the stack, it's part of the current SCC
                lowlink[v] = min(lowlink[v], indices[w])
        
        # If v is a root node, pop the stack and generate an SCC
        if lowlink[v] == indices[v]:
            scc = []
            while stack:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)
    
    for v in range(2 * n):
        if indices[v] == -1:
            strongconnect(v)
    
    return sccs

def add_implication(graph, x, y):
    """Adds implication ¬x → y and ¬y → x."""
    graph[negate(x)].append(y)
    graph[negate(y)].append(x)

def negate(literal):
    """Negates the literal, flipping between x and ¬x."""
    return literal ^ 1

def two_sat_solver(n, clauses):
    """Solves a 2-SAT problem with n variables and a list of clauses."""
    graph = defaultdict(list)

    for x, y in clauses:
        add_implication(graph, x, y)
    
    # Find SCCs using Tarjan's algorithm
    sccs = tarjan_scc(graph, n)
    
    # Check if a variable and its negation are in the same SCC
    assignment = [None] * n
    component = [-1] * (2 * n)  # Component identifier
    for idx, scc in enumerate(sccs):
        for node in scc:
            component[node] = idx
            if component[node] == component[negate(node)]:
                return False, None  # Unsatisfiable

    # Extract solution from topologically sorted SCCs
    for scc in reversed(sccs):
        for node in scc:
            var = node // 2
            if assignment[var] is None:
                assignment[var] = node % 2 == 0
    
    return True, assignment

def read_clauses_from_csv(filename):
    """Reads clauses from a CSV file and returns a list of clauses."""
    all_blocks = []
    current_clauses = []
    current_num_vars = 0
    
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Remove BOM if present (occurs at the start of the file)
            if row and '\ufeff' in row[0]:
                row[0] = row[0].replace('\ufeff', '')
            
            # Ignore comment and problem lines (e.g., starting with 'c' or 'p')
            if not row or row[0].startswith('c'):
                continue
            if row[0].startswith('p'):
                # New problem line starts a new block
                if current_clauses:
                    all_blocks.append((current_num_vars, current_clauses))
                    current_clauses = []
                current_num_vars = int(row[2])  # Number of variables in this block
                continue

            # Process the actual clauses
            clause = [int(literal) for literal in row if literal.strip() != '' and int(literal) != 0]
            current_clauses.append(clause)
        
        # Don't forget to add the last block after the loop finishes
        if current_clauses:
            all_blocks.append((current_num_vars, current_clauses))
    
    return all_blocks

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print("Usage: python3 2SatSolver.py <csv_filename> [--block <block_number>]")
        sys.exit(1)
    
    csv_filename = sys.argv[1]
    all_blocks = read_clauses_from_csv(csv_filename)

    if len(sys.argv) == 4 and sys.argv[2] == '--block':
        block_number = int(sys.argv[3])
        n, clauses = all_blocks[block_number - 1]  # Adjust for 0-based indexing
        print(f"Processing block {block_number}:")
        satisfiable, solution = two_sat_solver(n, clauses)
        if satisfiable:
            print(f"  Block {block_number} is satisfiable with solution:", solution)
        else:
            print(f"  Block {block_number} is unsatisfiable")
    else:
        for block_num, (n, clauses) in enumerate(all_blocks):
            print(f"Processing block {block_num + 1}:")
            satisfiable, solution = two_sat_solver(n, clauses)
            if satisfiable:
                print(f"  Block {block_num + 1} is satisfiable with solution:", solution)
            else:
                print(f"  Block {block_num + 1} is unsatisfiable")

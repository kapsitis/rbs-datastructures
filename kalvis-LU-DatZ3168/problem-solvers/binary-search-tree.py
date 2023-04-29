import copy
import math
import sys

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
# from Tools.scripts.lll import lll
from scipy.optimize import _root_scalar


def get_left_idx(nn):
    result = 2*nn + 1
    return result

def get_right_idx(nn):
    result = 2*nn+2
    return result

def get_parent_idx(nn):
    if nn==0:
        return -1
    else:
        return (nn-1)//2

def insert_node(tt, nn):
    idx = 0
    while idx<len(tt) and tt[idx] > -1:
        if nn == tt[idx]:
            #print('Skipping insert {}'.format(nn))
            return
        elif nn < tt[idx]:
            newIdx = get_left_idx(idx)
            #print('GO LEFT  (nn,idx,newIdx) = ({},{},{})'.format(nn,idx,newIdx))
            idx = newIdx
        else:
            newIdx = get_right_idx(idx)
            #print('GO RIGHT (nn,idx,newIdx) = ({},{},{})'.format(nn,idx,newIdx))
            idx = newIdx
    if idx < len(tt):
        tt[idx] = nn
    else:
        for jj in range(len(tt),idx+1):
            if jj == idx:
                tt.append(nn)
            else:
                tt.append(-1)


################ 
# Return index of the value 'nn' and also the path [L/R]-list
################
def search_idx(tt,nn):
    curr = 0
    path = list()
    while curr<len(tt) and tt[curr] > -1:
        if nn == tt[curr]:
            return (curr,path)
        elif nn < tt[curr]:
            curr = get_left_idx(curr)
            path.append('L')
        else: 
            curr = get_right_idx(curr)
            path.append('R')
    return (-1,list())

def set_node(tt,node_path):
    val = node_path[0]
    path = node_path[1]
    idx = 0
    for ch in path:
        if ch == 'L':
            idx = get_left_idx(idx)
        if ch == 'R':
            idx = get_right_idx(idx)
    tt[idx] = val

def cleanup(tt):
    lastNonEmpty = 0
    for i in range(0,len(tt)):
        if tt[i] > -1:
            lastNonEmpty = i
    #print('DEBUG 11: lastNonEmpty = {}'.format(lastNonEmpty))
    if lastNonEmpty < len(tt)-1:
        base = len(tt)-1
        for j in range(0,(len(tt)-1 - lastNonEmpty)):
            tt.pop(base - j)
    
# return sublist of all nonempty nodes (BFS order).
# Each node consists of a value and path, e.g. (20,[]) or (10,['L']). 
def get_bfs_subtree(tt,root,path):
    #print('DEBUG 12, get_bfs_subtree({},{},{})'.format(tt,root,path))
    result = [(tt[root],path,root)]
    pointer = 0
    while pointer < len(result):
        curr = result[pointer][2]
        currL = get_left_idx(curr)
        currR = get_right_idx(curr)
        if currL < len(tt):
            #print('result,pointer = {}[{}]'.format(result,pointer))
            myList1 = copy.deepcopy(result[pointer][1])
            myList1.append('L')
            result.append((tt[currL], myList1,currL))
        if currR < len(tt):
            myList2 = copy.deepcopy(result[pointer][1])
            myList2.append('R')
            result.append((tt[currR],myList2,currR))
        pointer += 1
    return result 

    
    
#    result = [root]
#    pointer = 0
#    while pointer < len(result):
#        curr = result[pointer]
#        currL = get_left_idx(curr)
#        currR = get_right_idx(curr)
#        if currL < len(tt) and tt[currL] > -1:
#            result.append(currL)
#        if currR < len(tt) and tt[currR] > -1:
#            result.append(currR)
#        pointer += 1
#    return result 

# Set all values under root to -1 (including 'root' itself)
def clear_under(tt,root):
    result = [root]
    pointer = 0
    while pointer < len(result):
        tt[result[pointer]] = -1
        currL = get_left_idx(result[pointer])
        currR = get_right_idx(result[pointer])
        if currL < len(tt):
            result.append(currL)
        if currR < len(tt):
            result.append(currR)
        pointer += 1

def inorder_list(tt,root):
    result = list()
    left_idx = get_left_idx(root)
    right_idx = get_right_idx(root)
    if left_idx < len(tt) and tt[left_idx] > -1: 
        result.extend(inorder_list(tt,left_idx))
    result.append(root)
    if right_idx < len(tt) and tt[right_idx] > -1: 
        result.extend(inorder_list(tt,right_idx))
    return result

####
# Return the value of the node that immediately precedes the given value.
# Return -1, if predecessor does not exist.
####
def get_inorder_pred_val(tt,idx):
    theOrder = inorder_list(tt,0)
    print('theOrder = {}'.format(theOrder))
    print('idx = {}'.format(idx))
    for i in range(1,len(theOrder)):
        if theOrder[i] == idx:
            return tt[theOrder[i-1]]
    return -1

####
# Return the value of the node that immediately precedes the given value.
# Return -1, if predecessor does not exist.
####
def get_inorder_succ_val(tt,idx):
    theOrder = inorder_list(tt,0)
    for i in range(0,len(theOrder)-1):
        if theOrder[i] == idx:
            return tt[theOrder[i+1]]
    return -1


# https://www.techiedelight.com/deletion-from-bst/
def delete_node(tt,root,nn,mode):
    idx_path = search_idx(tt,nn)
    nn_idx = idx_path[0]
    nn_path = idx_path[1]
    print('DEBUG 30, idx_path = {}'.format(idx_path))
    print('DEBUG31  delete_node({},{},{},{})'.format(tt,root,nn,mode))
    if nn_idx == -1:
        return 
    aa_left = get_left_idx(nn_idx)
    aa_right = get_right_idx(nn_idx)
    leftExists = aa_left < len(tt) and tt[aa_left] > -1
    rightExists = aa_right < len(tt) and tt[aa_right] > -1
    
    #print('DELETE  (tt,root,nn,mode) = ({},{},{},{})'.format(tt,root,nn,mode))
    #print('DELETE  (nn_idx,aa_left,aa_right,leftExists,rightExists) = ({},{},{},{},{})'.format(nn_idx,aa_left,aa_right,leftExists,rightExists))
    ## CASE 1
    if ((not leftExists) and (not rightExists)):
        tt[nn_idx] = -1
        cleanup(tt)
    ## CASE 2A
    ####
    ## NICE! Move the whole subtree up. 
    ####
    elif ((not leftExists) and rightExists):
        # delete one step to the right!
        #nn_path.append('R')        
        all_nodes = get_bfs_subtree(tt,aa_right,nn_path)
        #print('DEBUG 31, all_nodes = {}'.format(all_nodes))        
        clear_under(tt,aa_right)
        for node_path in all_nodes:
            set_node(tt,node_path)
        cleanup(tt)
    ## CASE 2B
    ####
    ## NICE! Move the whole subtree up. 
    ####
    elif (leftExists and (not rightExists)):
        # delete one step to the left!
        #nn_path.append('L')
        all_nodes = get_bfs_subtree(tt,aa_left,nn_path)
        clear_under(tt,aa_left)
        for node_path in all_nodes:
            set_node(tt,node_path)
        cleanup(tt)
    ## CASE 3
    else:
        if mode=='pred':
            pred = get_inorder_pred_val(tt,nn_idx)
            #print('DELETE (pred = {})'.format(pred))
            delete_node(tt,aa_left,pred,mode)
            tt[nn_idx] = pred
        else:
            succ = get_inorder_succ_val(tt,nn_idx)
            #print('DELETE (succ = {})'.format(succ))
            #print('CALL DELETE (tt,aa_right,succ,mode) = ({},{},{},{})'.format(tt,aa_right,succ,mode))
            delete_node(tt,aa_right,succ,mode)
            tt[nn_idx] = succ
        cleanup(tt)    
        
        
            

def get_depth(tree):
    return math.floor(math.log2(len(tree)))
    


def circle(ax,x, y, txt, radius=0.04):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)
    text(ax,x,y,txt)
    
def text(ax,x, y, text, col='blue'):
    ax.text(x, y+0.015, text, backgroundcolor="white", fontsize=10,
            ha='center', va='top', weight='normal', color=col)

def get_offsets_x():
    result = list()
    stepX = 0.24
    for i in range(0,9):
        initX = 0
        stepCurrent = stepX
        for k in range(0,i):
            initX = initX - stepCurrent
            stepCurrent = stepCurrent/2
        diffX =stepX/(2**(i-2))
        xx = initX 
        for j in range(0,2**i):
            if i < 4:
                result.append(xx) 
            else: 
                if j%2 == 0:
                    result.append(xx-0.012)
                else:
                    result.append(xx+0.012)
            xx += diffX
    return result

def get_offsets_y():
    result = list()
    stepY = 0.125
    yy = -0.05
    for i in range(0,9):        
        for j in range(0,2**i):
            result.append(yy)
        yy -= stepY
    return result



def pretty_print(ax,fig,tree,initX,initY):
    
    xx = get_offsets_x()
    yy = get_offsets_y()
    for i in range(0,len(tree)):
        if tree[i] > -1:
            circle(ax, initX+xx[i], initY+yy[i], str(tree[i]))
            iParent = get_parent_idx(i)
            if iParent >-1:            
                lin = mlines.Line2D([initX+xx[i],initX+xx[iParent]], 
                                    [initY+yy[i],initY+yy[iParent]])
                ax.add_line(lin)    

    

def main():
    mode = 'pred'
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: python script_md6.py <a> <b> [<pred>|<succ>]')
        sys.exit(0)
    else: 
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if len(sys.argv) == 4:
            mode = sys.argv[3]
    
    
    # theTree = [20,10,30,-1,16,21,-1,-1,-1,13,17,-1,25] 
    theTree = [20,10,30,5,-1,24,-1, -1, 8, -1, -1, 21, 25]
    
    #a = 1
    #b = 7
    S = 3*b
    T = 25+a
    U = 2*a
    X = a
    Y = (a+b) % 10
    Z = (5*(a+b)) % 40
    

    print('S = {}'.format(S))
    print('T = {}'.format(T))
    print('U = {}'.format(U))
    print('X = {}'.format(X))
    print('Y = {}'.format(Y))
    print('Z = {}'.format(Z))
    print('')
    
    print('Insert {}'.format(S))
    print('Insert {}'.format(T))
    print('Delete {}'.format(20))
    print('Show')
    print('Insert {}'. format(U))
    print('Insert {}'.format(X))
    print('Delete {}'.format(25))
    print('Show')
    print('Insert {}'.format(Y))
    print('Insert {}'.format(Z))
    print('Delete {}'.format(S))
    print('Show')
    
    
    ### Just so
    #insert_node(theTree,22)
    #insert_node(theTree,24)


    
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set(xlim=(-1, 1), ylim = (-1, 1))
    
    text(ax,-0.95,1.05,'AB={}{}'.format(a,b),'green')
    text(ax,-0.5,1.05,'S={}, T={}, U={}, X={}, Y={}, Z={}'.format(S,T,U,X,Y,Z),'green')
    
    pretty_print(ax,fig,theTree,-0.5,1)
        
    insert_node(theTree,S)
    insert_node(theTree,T)
    print('DEBUG 1, n = {}({})'.format(theTree,len(theTree)))
    
    myList = inorder_list(theTree,0)
    myZeroIdx = search_idx(theTree,20)
    mySucc = get_inorder_succ_val(theTree, myZeroIdx)
    print('DEBUG 2, myList,myZeroIdx,mySucc = {},{},{}'.format(myList,myZeroIdx,mySucc))        
    delete_node(theTree,0,20,mode)
    #print('DEBUG 3, n = {}({})'.format(theTree,len(theTree)))
    #print('DEBUG 4, n = {}'.format(inorder_list(theTree,0)))
    #print('DEBUG 5, pred ={}'.format(get_inorder_pred_val(theTree,0)))
    
    text(ax,0.11,0.95,'Insert  {}'.format(S),'red')
    text(ax,0.11,0.90,'Insert  {}'.format(T),'red')
    text(ax,0.11,0.85,'Delete  {}'.format(20),'red')
    
    pretty_print(ax,fig,theTree,0.5,1)
       

    insert_node(theTree,U)
    insert_node(theTree,X)
    delete_node(theTree,0,25,mode)
    #print('Show2,n = {}({})'.format(theTree,len(theTree)))
    text(ax,-0.89,0.00,'Insert  {}'.format(U),'red')
    text(ax,-0.89,-0.05,'Insert  {}'.format(X),'red')
    text(ax,-0.89,-0.10,'Delete  {}'.format(25),'red')
    pretty_print(ax,fig,theTree,-0.5,0)
    
    #print('DEBUG 6, n = {}({})'.format(theTree,len(theTree)))
    insert_node(theTree,Y)
    #print('DEBUG 7, n = {}({})'.format(theTree,len(theTree)))
    
    insert_node(theTree,Z)
    delete_node(theTree,0,S,mode)
    #print('Show3,n = {}({})'.format(theTree,len(theTree)))
    
    text(ax,0.11,0.00,'Insert  {}'.format(Y),'red')
    text(ax,0.11,-0.05,'Insert  {}'.format(Z),'red')
    text(ax,0.11,-0.10,'Delete  {}'.format(S),'red')
    pretty_print(ax,fig,theTree,0.5,0)    
    plt.show()



if __name__ == '__main__':
    main()    


## now, try to delete 20 :)
# [20, 10, 30, -1, 16, 21, -1, -1, -1, 13, 17, -1, 25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23](26)


## [20, 10, 30, -1, 16, 21, -1, -1, -1, 13, 17, -1, 25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24]
## Try deleting 20.

# python .\script_md6.py 8 4 succ



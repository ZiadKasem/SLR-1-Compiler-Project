# SLR(1)
import copy
import re
import graphviz
import os

ID = re.compile(r"[A-Za-z]+[0-9|A-Z|a-z]*")
NUM = re.compile(r"[0-9]+")
assignment = re.compile(":=")
semi_col = re.compile(";")
tokensID = (':=', ';')
tokensLoop = ('repeat', 'Until')
rep = "repeat"
repeat = re.compile(rep)
Unt = "Until"
Until = re.compile(Unt)


def check_statment(code_in):
    code_in = code_in.split()

    if code_in[0] == tokensLoop[0] and len(code_in) > 1:  # if it starts with repeat
        i = 1

        while code_in[i] != tokensLoop[1] and i < len(code_in) and len(code_in) >3:
            if (re.fullmatch(ID, code_in[i])) and (re.fullmatch(assignment, code_in[i + 1])) and (
                    re.fullmatch(ID, code_in[i + 2]) or re.fullmatch(NUM, code_in[i + 2])) and (
                    code_in[i + 3] == tokensID[1]):
                i += 4

            else:
                return 'Invalid statement'

        if i > len(code_in):
            return 'Invalid statement'
        elif (i + 3 < len(code_in)):

            return 'Invalid statement'
        elif (code_in[i] == tokensLoop[1]) and (re.fullmatch(ID, code_in[i + 1])) and i + 2 == len(code_in):

            return "valid"

        else:

            return "Invalid statement"


    else:

        return "Invalid statement"


def statment_accept(code_in):
    code_in = code_in.split()
    tokens = []
    for tok in code_in:
        if code_in is None:
           # l=tk.Label(root, text='inValid statement', bg='red').grid(row=4,column=1)
            return None
        else:
            if re.fullmatch(Unt, tok):

                tokens.append(tok)
            elif re.fullmatch(rep, tok):

                tokens.append(tok)
            elif re.fullmatch(ID, tok):

                tokens.append('Identifier')
            elif re.fullmatch(NUM, tok):

                tokens.append('Number')
            elif re.fullmatch(assignment, tok):

                tokens.append(tok)
            elif re.fullmatch(semi_col, tok):

                tokens.append(tok)

    return tokens

def stackimp(input_string):
    global Table

    i = 0
    stack = ['0']
    buffer = []
    colomB = ['Identifier','Number',':=','repeat','Until' , ';' , '$' ,  'stmt-seq' ,'statement','repeat-stmt','assign-stmt', 'factor']
    buffer =  input_string + ['$']
    print(buffer)
    print("stack content")
    # pointer ar first input element
    counter =0
    validFlag = True
    # aabb
    while validFlag:

        nextInputchar = buffer[counter]

        # end loop if all symbols matched
        if nextInputchar == '%':
            # hnzwd valid zyada
            return "\ninValid String!"
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'Accept':
            return "\nValid String!"
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S1 ':

            stack.append(nextInputchar)
            stack.append('1')
            counter=counter+1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S2 ':

            stack.append(nextInputchar)
            stack.append('2')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S3 ':

            stack.append(nextInputchar)
            stack.append('3')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S4 ':

            stack.append(nextInputchar)
            stack.append('4')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S5 ':

            stack.append(nextInputchar)
            stack.append('5')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S6 ':

            stack.append(nextInputchar)
            stack.append('6')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S7 ':

            stack.append(nextInputchar)
            stack.append('7')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S8 ':

            stack.append(nextInputchar)
            stack.append('8')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S9 ':

            stack.append(nextInputchar)
            stack.append('9')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S10 ':


            stack.append(nextInputchar)
            stack.append('10')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S11 ':

            stack.append(nextInputchar)
            stack.append('11')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S12 ':
            print(nextInputchar)
            stack.append(nextInputchar)
            stack.append('12')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S13 ':

            stack.append(nextInputchar)
            stack.append('13')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S14 ':

            stack.append(nextInputchar)
            stack.append('14')
            counter = counter + 1
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'S15 ':

            stack.append(nextInputchar)
            stack.append('15')
            counter = counter + 1

            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R1 ':
            popList=[]
            stack.pop(stack.__len__() - 1)
            popList.append(addNode(stack.pop(stack.__len__() - 1)))
            stack.pop(stack.__len__() - 1)
            popList.append(addNode(stack.pop(stack.__len__()-1)))

            parent = addNode('stmt-seq')
            stack.append('stmt-seq')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('stmt-seq')])
            for child in popList:
                addEgde(parent, child)

            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R2 ':
            popList = []
            stack.pop(stack.__len__()-1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('stmt-seq')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('stmt-seq')])
            parent = addNode('stmt-seq')
            for child in popList:
                addEgde(child,parent)


            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R3 ':
            popList = []
            stack.pop(stack.__len__()-1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('statement')
            parent = addNode('statement')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('statement')])
            for child in popList:
                addEgde(parent, child)
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R4 ':
            popList = []
            stack.pop(stack.__len__()-1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('statement')
            parent = addNode('statement')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('statement')])
            for child in popList:
                addEgde(parent, child)
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R5 ':
            popList = []
            stack.pop(stack.__len__()-1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('repeat-stmt')
            parent = addNode('repeat-stmt')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('repeat-stmt')])
            for child in popList:
                addEgde(parent, child)
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R6 ':
            popList = []
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            print(popList)
            parent = addNode('assign-stmt')
            stack.append('assign-stmt')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('assign-stmt')])
            for child in popList:
                addEgde(parent, child)
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R7 ':
            popList = []
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('factor')
            parent = addNode('factor')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('factor')])
            for child in popList:
                addEgde(parent, child)
            print(stack)
        elif Table[ int(stack[stack.__len__()-1]) ][colomB.index(nextInputchar)] == 'R8 ':
            popList = []
            stack.pop(stack.__len__() - 1)
            popList.append(stack.pop(stack.__len__() - 1))
            stack.append('factor')
            parent = addNode('factor')
            stack.append(Table[int(stack[stack.__len__()-2])][colomB.index('factor')])
            for child in popList:
                addEgde(parent,child)
            print(stack)

def addNode(state):
    global NodeUniqueName , name_list
    name = str(NodeUniqueName)
    dot.node(name,state)

    name_list.append(state)

    name_list = [name for name in name_list if not name.isnumeric()]
    NodeUniqueName +=1
    return name

def addEgde(preState,currentState):
    dot.edge(preState,currentState)



# perform grammar augmentation
def grammarAugmentation(rules, nonterm_userdef,
                        start_symbol):
    # newRules stores processed output rules
    newRules = []

    # create unique 'symbol' to
    # - represent new start symbol
    newChar = start_symbol + "'"
    while (newChar in nonterm_userdef): #whyy comma
        newChar += "'"

    # adding rule to bring start symbol to RHS
    newRules.append([newChar,
                     ['.', start_symbol]])

    # new format => [LHS,[.RHS]],
    # can't use dictionary since
    # - duplicate keys can be there
    for rule in rules:

        # split LHS from RHS
        k = rule.split("->")
        lhs = k[0].strip()
        rhs = k[1].strip()

        # split all rule at '|'
        # keep single derivation in one rule
        multirhs = rhs.split('|')
        for rhs1 in multirhs:
            rhs1 = rhs1.strip().split()

            # ADD dot pointer at start of RHS
            rhs1.insert(0, '.')
            newRules.append([lhs, rhs1])
    return newRules


# find closure
def findClosure(input_state, dotSymbol):
    global start_symbol, \
        seperatedRulesList, \
        statesDict

    # closureSet stores processed output
    closureSet = []

    # if findClosure is called for
    # - 1st time i.e. for I0,
    # then LHS is received in "dotSymbol",
    # add all rules starting with
    # - LHS symbol to closureSet
    if dotSymbol == start_symbol:
        for rule in seperatedRulesList:
            if rule[0] == dotSymbol:
                closureSet.append(rule)
    else:
        # for any higher state than I0,
        # set initial state as
        # - received input_state
        closureSet = input_state

    # iterate till new states are
    # - getting added in closureSet
    prevLen = -1
    while prevLen != len(closureSet):
        prevLen = len(closureSet)

        # "tempClosureSet" - used to eliminate
        # concurrent modification error
        tempClosureSet = []

        # if dot pointing at new symbol,
        # add corresponding rules to tempClosure
        for rule in closureSet:
            indexOfDot = rule[1].index('.')
            if rule[1][-1] != '.':
                dotPointsHere = rule[1][indexOfDot + 1]
                for in_rule in seperatedRulesList:
                    if dotPointsHere == in_rule[0] and \
                            in_rule not in tempClosureSet:
                        tempClosureSet.append(in_rule)

        # add new closure rules to closureSet
        for rule in tempClosureSet:
            if rule not in closureSet:
                closureSet.append(rule)
    return closureSet


def compute_GOTO(state):
    global statesDict, stateCount

    # find all symbols on which we need to
    # make function call - GOTO
    generateStatesFor = []
    for rule in statesDict[state]:
        # if rule is not "Handle"
        if rule[1][-1] != '.':
            indexOfDot = rule[1].index('.')
            dotPointsHere = rule[1][indexOfDot + 1]
            if dotPointsHere not in generateStatesFor:
                generateStatesFor.append(dotPointsHere)

    # call GOTO iteratively on all symbols pointed by dot
    if len(generateStatesFor) != 0:
        for symbol in generateStatesFor:
            GOTO(state, symbol)
    return


def GOTO(state, charNextToDot):
    global statesDict, stateCount, stateMap

    # newState - stores processed new state
    newState = []
    for rule in statesDict[state]:
        indexOfDot = rule[1].index('.')
        if rule[1][-1] != '.':
            if rule[1][indexOfDot + 1] == \
                    charNextToDot:
                # swapping element with dot,
                # to perform shift operation
                shiftedRule = copy.deepcopy(rule) # copy      s -> A.A
                shiftedRule[1][indexOfDot] = \
                    shiftedRule[1][indexOfDot + 1]
                shiftedRule[1][indexOfDot + 1] = '.' # s-> AA.
                newState.append(shiftedRule)

    # add closure rules for newState
    # call findClosure function iteratively
    # - on all existing rules in newState

    # addClosureRules - is used to store
    # new rules temporarily,
    # to prevent concurrent modification error
    addClosureRules = []
    for rule in newState:
        indexDot = rule[1].index('.')
        # check that rule is not "Handle"
        if rule[1][-1] != '.':
            closureRes = \
                findClosure(newState, rule[1][indexDot + 1])
            for rule in closureRes:
                if rule not in addClosureRules \
                        and rule not in newState:
                    addClosureRules.append(rule)

    # add closure result to newState
    for rule in addClosureRules:
        newState.append(rule)

    # find if newState already present
    # in Dictionary
    stateExists = -1
    for state_num in statesDict:
        if statesDict[state_num] == newState:
            stateExists = state_num
            break

    # stateMap is a mapping of GOTO with
    # its output states
    if stateExists == -1:

        # if newState is not in dictionary,
        # then create new state
        stateCount += 1
        statesDict[stateCount] = newState
        stateMap[(state, charNextToDot)] = stateCount
    else:

        # if state repetition found,
        # assign that previous state number
        stateMap[(state, charNextToDot)] = stateExists
    return


def generateStates(statesDict):
    prev_len = -1
    called_GOTO_on = []

    # run loop till new states are getting added
    while (len(statesDict) != prev_len):
        prev_len = len(statesDict)
        keys = list(statesDict.keys())

        # make compute_GOTO function call
        # on all states in dictionary
        for key in keys:
            if key not in called_GOTO_on:
                called_GOTO_on.append(key)
                compute_GOTO(key)
    return


# calculation of first
# epsilon is denoted by '#' (semi-colon)

# pass rule in first function
def first(rule):
    global rules, nonterm_userdef, \
        term_userdef, diction, firsts

    # recursion base condition
    # (for terminal or epsilon)
    if len(rule) != 0 and (rule is not None):
        if rule[0] in term_userdef:
            return rule[0]
        elif rule[0] == '#':
            return '#'

    # condition for Non-Terminals
    if len(rule) != 0:
        if rule[0] in list(diction.keys()):

            # fres temporary list of result
            fres = []
            rhs_rules = diction[rule[0]]

            # call first on each rule of RHS
            # fetched (& take union)
            for itr in rhs_rules:
                indivRes = first(itr)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)

            # if no epsilon in result
            # - received return fres
            if '#' not in fres:
                return fres
            else:

                # apply epsilon
                # rule => f(ABC)=f(A)-{e} U f(BC)
                newList = []
                fres.remove('#')
                if len(rule) > 1:
                    ansNew = first(rule[1:])
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList

                # if result is not already returned
                # - control reaches here
                # lastly if eplison still persists
                # - keep it in result of first
                fres.append('#')
                return fres


# calculation of follow
def follow(nt):
    global start_symbol, rules, nonterm_userdef, \
        term_userdef, diction, firsts, follows

    # for start symbol return $ (recursion base case)
    solset = set()
    if nt == start_symbol:
        # return '$'
        solset.add('$')

    # check all occurrences
    # solset - is result of computed 'follow' so far

    # For input, check in all rules
    for curNT in diction:
        rhs = diction[curNT]

        # go for all productions of NT
        for subrule in rhs:
            if nt in subrule:

                # call for all occurrences on
                # - non-terminal in subrule
                while nt in subrule:
                    index_nt = subrule.index(nt)
                    subrule = subrule[index_nt + 1:]

                    # empty condition - call follow on LHS
                    if len(subrule) != 0:

                        # compute first if symbols on
                        # - RHS of target Non-Terminal exists
                        res = first(subrule)

                        # if epsilon in result apply rule
                        # - (A->aBX)- follow of -
                        # - follow(B)=(first(X)-{ep}) U follow(A)
                        if '#' in res:
                            newList = []
                            res.remove('#')
                            ansNew = follow(curNT)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:

                        # when nothing in RHS, go circular
                        # - and take follow of LHS
                        # only if (NT in LHS)!=curNT
                        if nt != curNT:
                            res = follow(curNT)

                    # add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)


def createParseTable(statesDict, stateMap, T, NT):
    global seperatedRulesList, diction,Table

    # create rows and cols
    rows = list(statesDict.keys())
    cols = T + ['$'] + NT

    # create empty table
    Table = []
    tempRow = []
    for y in range(len(cols)):
        tempRow.append('')
    for x in range(len(rows)):
        Table.append(copy.deepcopy(tempRow))


    # make shift and GOTO entries in table
    for entry in stateMap:
        state = entry[0]
        symbol = entry[1]
        # get index
        a = rows.index(state)
        b = cols.index(symbol)
        if symbol in NT:
            Table[a][b] = Table[a][b] \
                          + f"{stateMap[entry]} "
        elif symbol in T:
            Table[a][b] = Table[a][b] \
                          + f"S{stateMap[entry]} "

    # start REDUCE procedure

    # number the separated rules
    numbered = {}
    key_count = 0
    for rule in seperatedRulesList:
        tempRule = copy.deepcopy(rule)
        tempRule[1].remove('.')
        numbered[key_count] = tempRule
        key_count += 1

    # start REDUCE procedure
    # format for follow computation
    addedR = f"{seperatedRulesList[0][0]} -> " \
             f"{seperatedRulesList[0][1][1]}"
    rules.insert(0, addedR)
    for rule in rules:
        k = rule.split("->")

        # remove un-necessary spaces
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multirhs = rhs.split('|')

        # remove un-necessary spaces
        for i in range(len(multirhs)):
            multirhs[i] = multirhs[i].strip()
            multirhs[i] = multirhs[i].split()
        diction[k[0]] = multirhs

    # find 'handle' items and calculate follow.
    for stateno in statesDict:
        for rule in statesDict[stateno]:
            if rule[1][-1] == '.':

                # match the item
                temp2 = copy.deepcopy(rule)
                temp2[1].remove('.')
                for key in numbered:
                    if numbered[key] == temp2:

                        # put Rn in those ACTION symbol columns,
                        # who are in the follow of
                        # LHS of current Item.
                        follow_result = follow(rule[0])
                        for col in follow_result:
                            index = cols.index(col)
                            if key == 0:
                                Table[stateno][index] = "Accept"
                            else:
                                Table[stateno][index] = \
                                    Table[stateno][index] + f"R{key} "

    # printing table
    print("\nSLR(1) parsing table:\n")
    frmt = "{:>8}" * len(cols)
    print(" ", frmt.format(*cols), "\n")
    ptr = 0
    j = 0
    for y in Table:
        frmt1 = "{:>8}" * len(y)
        print(f"{{:>3}} {frmt1.format(*y)}"
              .format('I' + str(j)))
        j += 1



def printResult(rules):
    for rule in rules:
        print(f"{rule[0]} ->"
              f" {' '.join(rule[1])}")


def printAllGOTO(diction):
    for itr in diction:
        print(f"GOTO ( I{itr[0]} ,"
              f" {itr[1]} ) = I{stateMap[itr]}")


# * MAIN * - Driver Code ================================================================================================

# uncomment any rules set to test code
# follow given format to add -
# user defined grammar rule set
# rules section - START

# example sample set 01



user_input = input("enter tokens")
# for parse tree
NodeUniqueName = 0
dot = graphviz.Digraph('The Round Table', filename='parseTree.gv')
name_list =[]
if check_statment(user_input) == 'valid':
    print(statment_accept(user_input))
    my_tokens = statment_accept(user_input)

else:
    print('invalid state')
    exit()




rules=["stmt-seq -> stmt-seq statement | statement",
       "statement -> repeat-stmt | assign-stmt",
       "repeat-stmt -> repeat stmt-seq until Identifier",
       "assign-stmt -> Identifier := factor ;",
       " factor -> Identifier | Number"
    ]
nonterm_userdef = ["stmt-seq", "statement", "repeat-stmt", "assign-stmt", "factor"]
term_userdef = ['Identifier', 'Number', ':=', 'repeat', 'until', ';']
start_symbol = nonterm_userdef[0]



# rules section - END
print("\nOriginal grammar input:\n")
for y in rules:
    print(y)

# print processed rules
print("\nGrammar after Augmentation: \n")
seperatedRulesList = \
    grammarAugmentation(rules,
                        nonterm_userdef,
                        start_symbol)
printResult(seperatedRulesList)

# find closure
start_symbol = seperatedRulesList[0][0]
print("\nCalculated closure: I0\n")
I0 = findClosure(0, start_symbol)
printResult(I0)

# use statesDict to store the states
# use stateMap to store GOTOs
statesDict = {}
stateMap = {}
Table = []

# add first state to statesDict
# and maintain stateCount
# - for newState generation
statesDict[0] = I0
stateCount = 0

# computing states by GOTO
generateStates(statesDict)

# print goto states
print("\nStates Generated: \n")
for st in statesDict:
    print(f"State = I{st}")
    printResult(statesDict[st])
    print()

print("Result of GOTO computation:\n")
printAllGOTO(stateMap)

# "follow computation" for making REDUCE entries
diction = {}

# call createParseTable function
createParseTable(statesDict, stateMap,
                 term_userdef,
                 nonterm_userdef)
print(stackimp(my_tokens))
dot.view()

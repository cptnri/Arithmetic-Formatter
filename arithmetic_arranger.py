def arithmetic_arranger(problems):
    
    dig1 = list()
    dig2 = list()
    sumdif = list()
    d1 = list()
    d2 = list()
    sd = list()
    op = list()
    line = list()
    newl = list()
    larger = 0
    space = ' '
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for p in problems:
        d = p.split()
        if len(d) != 3:
            return "Error: Must only contain 2 numbers and 1 operator."
        elif len(d[0]) > 4 or len(d[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif d[1] != '+' and d[1] != '-':
            return "Error: Operator must be '+' or '-'."

        try:
            x = int(d[0])
            y = int(d[2])
            if d[1] == '+':
                z = x + y
                sumdif.append(str(z))
            else:
                z = x - y
                sumdif.append(str(z))
        except ValueError:
            return "Error: Numbers must only contain digits."
        
        dig1.append(d[0])
        dig2.append(d[2])
        op.append(d[1])
        
        if len(d[0]) > len(d[2]): larger = d[0]
        elif len(d[0]) < len(d[2]): larger = d[2]
        else:
            larger = d[2]
        
        l = str(larger)
        #dig1[d[0]] = l
        #dig2[d[2]] = l
        #op[d[1]] = l

        line.append(l)
    
    for i in range(len(dig1)):
        numspace = (len(line[i]) + 2) - len(dig1[i])
        sp = space * numspace
        if i == (len(dig1) - 1):
            nums = [sp,dig1[i]]
        else:
            nums = [sp,dig1[i],'    ']
        d1.extend(nums)
        
    d1.append('\n')
    dig1.clear()
    delimiter = ''
    dig1 = delimiter.join(d1)
    
    for i in range(len(dig2)):
        
        if line[i] == dig2[i]:
            if i == (len(dig2) - 1):
                nums = [op[i],' ',dig2[i]]
            else:
                nums = [op[i],' ',dig2[i],'    ']
            d2.extend(nums)
        else:
            numspace = (len(line[i]) + 1) - len(dig2[i])
            sp = ' ' * numspace
            if i == (len(dig2) - 1):
                nums = [op[i],sp,dig2[i]]
            else:
                nums = [op[i],sp,dig2[i],'    ']
            d2.extend(nums)
    
    d2.append('\n')
    dig2.clear()
    dig2 = delimiter.join(d2)
    
    for i in range(len(sumdif)):
        numspace = (len(line[i]) + 2) - len(sumdif[i])
        sp = space * numspace
        
        nums = [sp,sumdif[i],'    ']
        sd.extend(nums)
    
    for i in range(len(line)):
        dash = '-'
        sp = (len(line[i]) + 2) * dash
        if i == (len(line) - 1):
            nums = [sp]
        else:
            nums = [sp,'    ']
        newl.extend(nums)
    
    #newl.append('\n')
    line.clear()
    line = delimiter.join(newl)
    
    sd.append('\n')
    sumdif.clear()
    sumdif = delimiter.join(sd)
    
    problems.clear()
    problems = [dig1,dig2,line]
    
    probs = delimiter.join(problems)
    arranged_problems = str(probs)
    
    return arranged_problems
    

#!/usr/bin/python3
"""This is the documentation for the module. Necessary
I honestly do not know what is failing at this point.
"""


count = 0
total = 0
possible = [200, 301, 400, 401, 403, 404, 405, 500]
pr_list = {x: 0 for x in possible}

try:
    while True:
        line = input()
        line_arr = line.split("\"GET /projects/260 HTTP/1.1\"")
        if len(line_arr) < 2:
            continue

        line_arr = line_arr[1].split()
        if len(line_arr) < 2:
            continue

        stc = int(line_arr[0])
        fls = int(line_arr[1])
        total += fls
        if count % 10 == 0:
            for each in sorted(pr_list.keys()):
                if pr_list[each] == 0:
                    continue
                print(f"{each:d} : {pr_list[each]:d}")

            print("File size: {:d}".format(total))

        if stc in possible:
            pr_list[stc] += 1
        count += 1

except Exception:
    pass

finally:
    for each in sorted(pr_list.keys()):
        if pr_list[each] == 0:
            continue
        print(f"{each:d} : {pr_list[each]:d}")

    print("File size: {:d}".format(total))

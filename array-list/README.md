# Array List

|  |Method                      |Description|
|--|----------------------------|---|
|✅|```__contains__(e)```       |*e in s*|
|  |```__getitem__(p)```        |Retreive element at the position *p*|
|  |```__len__()```             |Number of items|
|  |```append(e)```             |Add element to the end|
|  |```clear()```               |Remove all items|
|  |```copy()```                |Shallow copy|
|  |```index(e)```              |Index of the first occurence of *e*|
|  |```insert(e, p)```          |Insert element *e* before item at position *p*|
|  |```reverse()```             |Reverse all items|
|  |```sort([key], [reverse])```|Sort items in place with *key* and in *reverse* order|

This collection is implemented using the array. Increase factor is 2. Sorting
is implemented using Timsort algorithm.
